# encoding: utf-8
# @Time   : 2023/12/25
# @Author : Spike
# @Descr   :
import json
import os
import re
import requests
from typing import List, Dict, Tuple
from toolbox import get_conf, encode_image, get_pictures_list, to_markdown_tabs

proxies, TIMEOUT_SECONDS = get_conf("proxies", "TIMEOUT_SECONDS")

"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第五部分 一些文件处理方法
files_filter_handler 根据type过滤文件
input_encode_handler 提取input中的文件，并解析
file_manifest_filter_html 根据type过滤文件, 并解析为html or md 文本
link_mtime_to_md 文件增加本地时间参数，避免下载到缓存文件
html_view_blank 超链接
html_local_file 本地文件取相对路径
to_markdown_tabs 文件list 转换为 md tab
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


def files_filter_handler(file_list):
    new_list = []
    filter_ = [
        "png",
        "jpg",
        "jpeg",
        "bmp",
        "svg",
        "webp",
        "ico",
        "tif",
        "tiff",
        "raw",
        "eps",
    ]
    for file in file_list:
        file = str(file).replace("file=", "")
        if os.path.exists(file):
            if str(os.path.basename(file)).split(".")[-1] in filter_:
                new_list.append(file)
    return new_list


def input_encode_handler(inputs, llm_kwargs):
    if llm_kwargs["most_recent_uploaded"].get("path"):
        image_paths = get_pictures_list(llm_kwargs["most_recent_uploaded"]["path"])
    md_encode = []
    for md_path in image_paths:
        type_ = os.path.splitext(md_path)[1].replace(".", "")
        type_ = "jpeg" if type_ == "jpg" else type_
        md_encode.append({"data": encode_image(md_path), "type": type_})
    return inputs, md_encode


def file_manifest_filter_html(file_list, filter_: list = None, md_type=False):
    new_list = []
    if not filter_:
        filter_ = [
            "png",
            "jpg",
            "jpeg",
            "bmp",
            "svg",
            "webp",
            "ico",
            "tif",
            "tiff",
            "raw",
            "eps",
        ]
    for file in file_list:
        if str(os.path.basename(file)).split(".")[-1] in filter_:
            new_list.append(html_local_img(file, md=md_type))
        elif os.path.exists(file):
            new_list.append(link_mtime_to_md(file))
        else:
            new_list.append(file)
    return new_list


def link_mtime_to_md(file):
    link_local = html_local_file(file)
    link_name = os.path.basename(file)
    a = f"[{link_name}]({link_local}?{os.path.getmtime(file)})"
    return a


def html_local_file(file):
    base_path = os.path.dirname(__file__)  # 项目目录
    if os.path.exists(str(file)):
        file = f'file={file.replace(base_path, ".")}'
    return file


def html_local_img(__file, layout="left", max_width=None, max_height=None, md=True):
    style = ""
    if max_width is not None:
        style += f"max-width: {max_width};"
    if max_height is not None:
        style += f"max-height: {max_height};"
    __file = html_local_file(__file)
    a = f'<div align="{layout}"><img src="{__file}" style="{style}"></div>'
    if md:
        a = f"![{__file}]({__file})"
    return a



class GoogleChatInit:
    def __init__(self):
        self.url_gemini = "https://generativelanguage.googleapis.com/v1beta/models/%m:streamGenerateContent?key=%k"

    def generate_chat(self, inputs, llm_kwargs, history, system_prompt):
        headers, payload = self.generate_message_payload(
            inputs, llm_kwargs, history, system_prompt
        )
        response = requests.post(
            url=self.url_gemini,
            headers=headers,
            data=json.dumps(payload),
            stream=True,
            proxies=proxies,
            timeout=TIMEOUT_SECONDS,
        )
        return response.iter_lines()

    def __conversation_user(self, user_input, llm_kwargs):
        what_i_have_asked = {"role": "user", "parts": []}
        if "vision" not in self.url_gemini:
            input_ = user_input
            encode_img = []
        else:
            input_, encode_img = input_encode_handler(user_input, llm_kwargs=llm_kwargs)
        what_i_have_asked["parts"].append({"text": input_})
        if encode_img:
            for data in encode_img:
                what_i_have_asked["parts"].append(
                    {
                        "inline_data": {
                            "mime_type": f"image/{data['type']}",
                            "data": data["data"],
                        }
                    }
                )
        return what_i_have_asked

    def __conversation_history(self, history, llm_kwargs):
        messages = []
        conversation_cnt = len(history) // 2
        if conversation_cnt:
            for index in range(0, 2 * conversation_cnt, 2):
                what_i_have_asked = self.__conversation_user(history[index], llm_kwargs)
                what_gpt_answer = {
                    "role": "model",
                    "parts": [{"text": history[index + 1]}],
                }
                messages.append(what_i_have_asked)
                messages.append(what_gpt_answer)
        return messages

    def generate_message_payload(
        self, inputs, llm_kwargs, history, system_prompt
    ) -> Tuple[Dict, Dict]:
        messages = [
            # {"role": "system", "parts": [{"text": system_prompt}]},  # gemini 不允许对话轮次为偶数，所以这个没有用，看后续支持吧。。。
            # {"role": "user", "parts": [{"text": ""}]},
            # {"role": "model", "parts": [{"text": ""}]}
        ]
        self.url_gemini = self.url_gemini.replace(
            "%m", llm_kwargs["llm_model"]
        ).replace("%k", get_conf("GEMINI_API_KEY"))
        header = {"Content-Type": "application/json"}
        if "vision" not in self.url_gemini:  # 不是vision 才处理history
            messages.extend(
                self.__conversation_history(history, llm_kwargs)
            )  # 处理 history
        messages.append(self.__conversation_user(inputs, llm_kwargs))  # 处理用户对话
        payload = {
            "contents": messages,
            "generationConfig": {
                # "maxOutputTokens": 800,
                "stopSequences": str(llm_kwargs.get("stop", "")).split(" "),
                "temperature": llm_kwargs.get("temperature", 1),
                "topP": llm_kwargs.get("top_p", 0.8),
                "topK": 10,
            },
        }
        return header, payload


if __name__ == "__main__":
    google = GoogleChatInit()
    # print(gootle.generate_message_payload('你好呀', {},  ['123123', '3123123'], ''))
    # gootle.input_encode_handle('123123[123123](./123123), ![53425](./asfafa/fff.jpg)')
