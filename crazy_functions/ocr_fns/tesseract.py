import subprocess, os, urllib.request
#from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive, get_conf

#TESSERACT_PATH = get_conf("TESSERACT_PATH")
TESSERACT_PATH = "E:\\Coding\\Environments\\Tesseract-OCR\\tesseract.exe"

lang_list = ["afr","amh","ara","asm","aze","aze_cyrl","bel","ben","bod","bos","bre","bul","cat","ceb","ces","chi_sim","chi_sim_vert","chi_tra","chi_tra_vert","chr","cos","cym","dan",
             "deu","div","dzo","ell","eng","enm","epo","equ","est","eus","fao","fas","fil","fin","fra","frk","frm","fry","gla","gle","glg","grc","guj","hat","heb","hin","hrv","hun",
             "hye","iku","ind","isl","ita","ita_old","jav","jpn","jpn_vert","kan","kat","kat_old","kaz","khm","kir","kmr","kor","kor_vert","lao","lat","lav","lit","ltz","mal","mar",
             "mkd","mlt","mon","mri","msa","mya","nep","nld","nor","oci","ori","pan","pol","por","pus","que","ron","rus","san","sin","slk","slv","snd","spa","spa_old","sqi","srp",
             "srp_latn","sun","swa","swe","syr","tam","tat","tel","tgk","tha","tir","ton","tur","uig","ukr","urd","uzb","uzb_cyrl","vie","yid","yor"]
             
def download_lang(lang):
    #从码云的某个仓库下载，github太慢
    url = f"https://gitee.com/dalaomai/tessdata_fast/raw/main/{lang}.traineddata"
    
    path = os.path.dirname(TESSERACT_PATH)
    path = os.path.join(path, "tessdata")
    path = os.path.join(path, f"{lang}.traineddata")
    
    response = urllib.request.urlopen(url)
    if response.status == 200:
        # 打开文件用于写入
        with open(path, 'wb') as file:
            # 将响应数据写入文件
            file.write(response.read())
            print(f'已将{lang}语言包下载至{path}')
    else:
        print('未能成功从{url}下载语言包')
             
def lang_exists(lang):
    path = os.path.dirname(TESSERACT_PATH)
    path = os.path.join(path, "tessdata")
    path = os.path.join(path, f"{lang}.traineddata")
    return os.path.isfile(path)
    
def ensure_lang_valid(lang):
    text = lang.split("+")
    lang = []
    for t in text:
        if lang_exists(t):
            lang.append(t)
        else:
            try:
                download_lang(t)
                lang.append(t)
            except Exception as e:
                print(f"下载语言包失败: {e}")
    if lang.__len__() == 0:
        lang = ["chi_sim", "eng"]
    return "+".join(lang)
    
def reconize(img_path, output_path, lang):
    subprocess.run(f"\"{TESSERACT_PATH}\" \"{img_path}\" \"{output_path}\" -l {lang}")
    if os.path.isfile(output_path):
        os.remove(output_path)
    os.rename(output_path+".txt", output_path)

def is_valid_demand(text):
    text = text.replace(" ", "").replace("\n", "")
    langs = text.split("+")
    for lang in langs:
        if lang not in lang_list:
            return None
    return "+".join(langs)
#根据用户的输入，智能判断用户想要哪种语言
def detect_language_from_users_demand(text, llm_kwargs, chatbot, system_prompt):
        if text=="":
            print("未检测到用户输入，默认使用chi_sim+eng")
            lang = ["chi_sim", "eng"]
            return "+".join(lang)
            
        if (lang:=is_valid_demand(text)) != None:
            return lang
    
        if llm_kwargs==None or chatbot==None or system_prompt==None:
            print("未检测到用户输入，默认使用chi_sim+eng")
            lang = ["chi_sim", "eng"]
            return "+".join(lang)
    
        prompt = f"""
                      你是一个被置于ocr程序输入端的智能机器人，任务是根据用户提出的要求，判断用户指定了哪些语言进行识别。
                      有效的语言代码如下所示：
                          {str(lang_list)}
                      用户提出要求识别的语言有：{text}
                      请你根据用户要求，判断用户需要使用哪些语种。输出所需语种的语言代码。请注意，输出的必须是有效的语言代码。
                  """
        
        #codes = yield from request_gpt_model_in_new_thread_with_ui_alive(prompt, "正在解析所需的语言包……", llm_kwargs, chatbot, history=[], sys_prompt=system_prompt)
        lang = []
        gpt_say = None
        for l in lang_list:
            if l in codes:
                lang.append(l)
        if lang.__len__() == 0:
            print("未能成功分析出用户需要的语言，默认使用chi_sim+eng")
            gpt_say = "未能成功分析出用户需要的语言，默认使用chi_sim+eng"
            lang = ["chi_sim", "eng"]
        else:
            gpt_say = "+".join(lang)
            print("分析得用户需要的语言为：{gpt_say}")
        history.append("正在解析所需的语言包……"); history.append("分析得用户需要的语言为：{gpt_say}")
        #yield from update_ui(chatbot=chatbot, history=history)
        lang = "+".join(lang)
        return lang
    
def batch_tesseract_ocr(input, output, lang, llm_kwargs, chatbot, system_prompt):
    lang = detect_language_from_users_demand(lang, llm_kwargs, chatbot, system_prompt)
    lang = ensure_lang_valid(lang)
    
    [reconize(i, o, lang) for i, o in zip(input, output)]

def tesseract_ocr(input, output, lang, llm_kwargs=None, chatbot=None, system_prompt=None):
    if type(input) == list:
        batch_tesseract_ocr(input, output, lang, llm_kwargs, chatbot, system_prompt)
    
    lang = detect_language_from_users_demand(lang, llm_kwargs, chatbot, system_prompt)
    lang = ensure_lang_valid(lang)
    
    reconize(input, output, lang)
    
if __name__ == "__main__":
    tesseract_ocr("C:\\Users\\***\\Desktop\\chi test.png", "C:\\Users\\***\\Desktop\\o1.txt", "chi_sim")
    tesseract_ocr("C:\\Users\\***\\Desktop\\eng test.png", "C:\\Users\\***\\Desktop\\o2.txt", "eng")
    tesseract_ocr("C:\\Users\\***\\Desktop\\chi+eng test.png", "C:\\Users\\***\\Desktop\\o3.txt", "chi_sim+eng")
    tesseract_ocr("C:\\Users\\***\\Desktop\\chi vert test.jpg", "C:\\Users\\***\\Desktop\\o4.txt", "chi_tra_vert")