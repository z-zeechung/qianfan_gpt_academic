import os
import threading
import requests, time
from toolbox import get_conf
from toolbox import update_ui

model_list = {
              "文心一言-4.0（ERNIE-Bot 4.0）": "completions_pro",
              "文心一言（ERNIE-Bot）": "completions",
              "文心一言-涡轮-0922（ERNIE-Bot-turbo-0922）": "eb-instant",
              "文心一言-快速（ERNIE-Speed）": "ernie_speed",
              "绽放Z-70亿（BLOOMZ-7B）": "bloomz_7b1",
              "大羊驼-2-70亿-聊天（Llama-2-7B-Chat）": "llama_2_7b",
              "大羊驼-2-130亿-聊天（Llama-2-13B-Chat）": "llama_2_13b",
              "大羊驼-2-700亿-聊天（Llama-2-70B-Chat）": "llama_2_70b",
              "千帆-绽放Z-70亿-压缩（Qianfan-BLOOMZ-7B-compressed）": "qianfan_bloomz_7b_compressed",
              "千帆-中文大羊驼-2-70亿（Qianfan-Chinese-Llama-2-7B）": "qianfan_chinese_llama_2_7b",
              "智谱2-60亿-32千（ChatGLM2-6B-32K）": "chatglm2_6b_32k",
              "天鹰-70亿（AquilaChat-7B）": "aquilachat_7b",
              "文心一言-8千（ERNIE-Bot-8k）": "ernie_bot_8k",
              "千帆-中文大羊驼-2-130亿（Qianfan-Chinese-Llama-2-13B）": "qianfan_chinese_llama_2_13b",
              "SQL代码-70亿（SQLCoder-7B）": "sqlcoder_7b",
              "代码大羊驼-70亿-指令（CodeLlama-7B-Instruct）": "codellama_7b_instruct",
              "轩辕-700亿-聊天-4比特（XuanYuan-70B-Chat-4bit）": "xuanyuan_70b_chat",
              "法律（ChatLaw）": "chatlaw",
              "零一万物-340亿-聊天（Yi-34B-Chat）": "yi_34b_chat",
              "冬风-8×70亿-指令（Mixtral-8x7B-Instruct）": "mixtral_8x7b_instruct",
              "文心一言-3.5-4千-0205（ERNIE-3.5-4K-0205）": "ernie-3.5-4k-0205",
              "文心一言-3.5-8千-0205（ERNIE-3.5-8K-0205）": "ernie-3.5-8k-0205"
            }

def check_website_availability(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
def open_browser():
    while True:
        if check_website_availability("http://127.0.0.1:5000"):
            break
    import webbrowser
    webbrowser.open_new_tab("http://127.0.0.1:5000")
        
def ppt(llm_kwargs):
    try:
        current_dir = os.getcwd()
        tardir = os.path.dirname(current_dir)
        pydir = os.path.join(tardir, "python", "python")
        tardir = os.path.join(tardir, "Auto-PPT")
        os.chdir(tardir)
        BAIDU_CLOUD_API_KEY, BAIDU_CLOUD_SECRET_KEY = get_conf('BAIDU_CLOUD_API_KEY', 'BAIDU_CLOUD_SECRET_KEY')
        MODEL = model_list[llm_kwargs['llm_model']]
        os.system(f"{pydir} application.py --QIANFAN_AK {BAIDU_CLOUD_API_KEY} --QIANFAN_SK {BAIDU_CLOUD_SECRET_KEY} --QIANFAN_MODEL {MODEL}")
    except:
        ...

def 生成PPT(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, user_request):

    chatbot.append([
        "生成PPT文档",
        "正在启动Auto PPT……程序作者：limaoyi1"])
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面
    
    if not check_website_availability("http://127.0.0.1:5000"):
        ppt_t = threading.Thread(target=ppt, args=(llm_kwargs,))
        ppt_t.daemon = True
        ppt_t.start()
    
    open_browser_t = threading.Thread(target=open_browser)
    open_browser_t.daemon = True
    open_browser_t.start()