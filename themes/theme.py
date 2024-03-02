import pickle
import base64
import uuid
from toolbox import get_conf

"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 1 部分
加载主题相关的工具函数
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


def load_dynamic_theme(THEME):
    adjust_dynamic_theme = None
    if THEME == "Chuanhu-Small-and-Beautiful":
        from .green import adjust_theme, advanced_css

        theme_declaration = (
            '<h2 align="center"  class="small">[Chuanhu-Small-and-Beautiful主题]</h2>'
        )
    elif THEME == "High-Contrast":
        from .contrast import adjust_theme, advanced_css

        theme_declaration = ""
    elif "/" in THEME:
        from .gradios import adjust_theme, advanced_css
        from .gradios import dynamic_set_theme

        adjust_dynamic_theme = dynamic_set_theme(THEME)
        theme_declaration = ""
    else:
        from .default import adjust_theme, advanced_css

        theme_declaration = ""
    return adjust_theme, advanced_css, theme_declaration, adjust_dynamic_theme


adjust_theme, advanced_css, theme_declaration, _ = load_dynamic_theme(get_conf("THEME"))


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 2 部分
cookie相关工具函数
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

def init_cookie(cookies):
    # 为每一位访问的用户赋予一个独一无二的uuid编码
    cookies.update({"uuid": uuid.uuid4()})
    return cookies


def to_cookie_str(d):
    # Pickle the dictionary and encode it as a string
    pickled_dict = pickle.dumps(d)
    cookie_value = base64.b64encode(pickled_dict).decode("utf-8")
    return cookie_value


def from_cookie_str(c):
    # Decode the base64-encoded string and unpickle it into a dictionary
    pickled_dict = base64.b64decode(c.encode("utf-8"))
    return pickle.loads(pickled_dict)


"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
第 3 部分
内嵌的javascript代码
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

js_code_for_css_changing = """(css) => {
    var existingStyles = document.querySelectorAll("body > gradio-app > div > style")
    for (var i = 0; i < existingStyles.length; i++) {
        var style = existingStyles[i];
        style.parentNode.removeChild(style);
    }
    var existingStyles = document.querySelectorAll("style[data-loaded-css]");
    for (var i = 0; i < existingStyles.length; i++) {
        var style = existingStyles[i];
        style.parentNode.removeChild(style);
    }
    var styleElement = document.createElement('style');
    styleElement.setAttribute('data-loaded-css', 'placeholder');
    styleElement.innerHTML = css;
    document.body.appendChild(styleElement);
}
"""


js_code_for_toggle_darkmode = """() => {
    if (document.querySelectorAll('.dark').length) {
        setCookie("js_darkmode_cookie", "False", 365);
        document.querySelectorAll('.dark').forEach(el => el.classList.remove('dark'));
    } else {
        setCookie("js_darkmode_cookie", "True", 365);
        document.querySelector('body').classList.add('dark');
    }
    document.querySelectorAll('code_pending_render').forEach(code => {code.remove();})
}"""


js_code_for_persistent_cookie_init = """(py_pickle_cookie, cookie) => {
    return [getCookie("py_pickle_cookie"), cookie];
}
"""


js_code_reset = """
(a,b,c)=>{
    return [[], [], "已重置"];
}
"""


js_code_clear = """
(a,b)=>{
    return ["", ""];
}
"""


js_code_show_or_hide = """
(display_panel_arr)=>{
setTimeout(() => {
    // get conf
    display_panel_arr = get_checkbox_selected_items("cbs");

    ////////////////////// 输入清除键 ///////////////////////////
    let searchString = "输入清除键";
    let ele = "none";
    if (display_panel_arr.includes(searchString)) {
        let clearButton = document.getElementById("elem_clear");
        let clearButton2 = document.getElementById("elem_clear2");
        clearButton.style.display = "block";
        clearButton2.style.display = "block";
        setCookie("js_clearbtn_show_cookie", "True", 365);
    } else {
        let clearButton = document.getElementById("elem_clear");
        let clearButton2 = document.getElementById("elem_clear2");
        clearButton.style.display = "none";
        clearButton2.style.display = "none";
        setCookie("js_clearbtn_show_cookie", "False", 365);
    }

    ////////////////////// 基础功能区 ///////////////////////////
    searchString = "基础功能区";
    if (display_panel_arr.includes(searchString)) {
        ele = document.getElementById("basic-panel");
        ele.style.display = "block";
    } else {
        ele = document.getElementById("basic-panel");
        ele.style.display = "none";
    }

    ////////////////////// 函数插件区 ///////////////////////////
    searchString = "函数插件区";
    if (display_panel_arr.includes(searchString)) {
        ele = document.getElementById("plugin-panel");
        ele.style.display = "block";
    } else {
        ele = document.getElementById("plugin-panel");
        ele.style.display = "none";
    }

}, 50);
}
"""



js_code_show_or_hide_group2 = """
(display_panel_arr)=>{
setTimeout(() => {
    // console.log("display_panel_arr");
    // get conf
    display_panel_arr = get_checkbox_selected_items("cbsc");

    ////////////////////// 添加Live2D形象 ///////////////////////////
    let searchString = "添加Live2D形象";
    let ele = "none";
    if (display_panel_arr.includes(searchString)) {
        setCookie("js_live2d_show_cookie", "True", 365);
        loadLive2D();
    } else {
        setCookie("js_live2d_show_cookie", "False", 365);
        $('.waifu').hide();
    }


}, 50);
}
"""
