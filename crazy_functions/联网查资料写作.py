from crazy_functions.crazy_utils import request_gpt_model_in_new_thread_with_ui_alive
import requests
from bs4 import BeautifulSoup



def get_bg_from_baidu(query):
    try:
        url = f"https://www.baidu.com/s?wd={query}&ie=UTF-8&tn=62095104_28_oem_dg&ch=1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
        response = requests.get(url, headers=headers)

        res = []
        soup = BeautifulSoup(response.text, 'html.parser')
        for paragraph in soup.find_all('span'):
            if paragraph.text.__len__() > 15:
                res.append(paragraph.text)
        return "\n".join(res)
    except:
        return ""



def 联网查资料写作(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, user_request):

    inputs = f"""
                  你是一个写作机器人，请根据用户的写作要求，列出文章提纲。
                  
                  用户要求写作的主题为：{txt}
                  
                  关于用户的写作主题，我们有如下资料提供：
                  {get_bg_from_baidu(txt)}
                  
                  现在，请你根据用户要求：“{txt}”，列出文章提纲。请注意，在你列出文章提纲时，你输出的每一行能且只能是提纲当中的一条，不得输出正文内容，也不得输出额外信息。
              """

    tigang = yield from request_gpt_model_in_new_thread_with_ui_alive(
        inputs=txt,                        # 提问的内容，给chatgpt看的
        inputs_show_user="给出文章提纲",   # 提问的内容，给用户看的（可以隐藏啰嗦的细节）
        llm_kwargs=llm_kwargs,             # 无聊的chatgpt内部参数
        chatbot=chatbot,                   # 聊天框句柄，原样传递
        history=[],                   # 之前的聊天内容，只有之前的聊天内容中有值得抽取的信息时，才是必要的
        sys_prompt=system_prompt
    )
    
    lns = tigang.split("\n")
    
    res = []
    
    for ln in lns:
        if ln == "":
            continue
        input = f"""
                     你是一个写作机器人，正在基于以下提纲进行写作：
                     {tigang}
                     
                     当前，你正在撰写提纲的这个部分：{ln}
                     
                     对于你正在撰写的部分，我们有如下背景信息提供：
                     {get_bg_from_baidu(ln)}
                     
                     请注意，对于提纲中的每个要点，你应当只撰写一个自然段，而不是多个自然段。
                     
                     现在，请基于提纲要求及我们提供的信息，围绕“{ln}”这一段展开写作，要求前后文连贯。
                 """
        ln = yield from request_gpt_model_in_new_thread_with_ui_alive(
            inputs=input,                        # 提问的内容，给chatgpt看的
            inputs_show_user=f"撰写文段：{ln}",   # 提问的内容，给用户看的（可以隐藏啰嗦的细节）
            llm_kwargs=llm_kwargs,             # 无聊的chatgpt内部参数
            chatbot=chatbot,                   # 聊天框句柄，原样传递
            history=history[-3:],                   # 之前的聊天内容，只有之前的聊天内容中有值得抽取的信息时，才是必要的
            sys_prompt=txt
        )
        
        res.append(ln)
        
    chatbot.append((
        "输出最终结果", 
        "\n\n".join(res)))
    yield from update_ui(chatbot=chatbot, history=history)