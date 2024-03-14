import wx
app = wx.App()
import wx.html2 as webview
import requests, time
from pynput.mouse import Listener

icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)


init_frame = None
def init_dialog():
    global init_frame

    dpi = wx.ScreenDC().GetPPI()[0]
    
    def get_px(cm):
        return round(cm * dpi / 2.54)
    
    init_frame = wx.Frame(None, title='', size=(get_px(8),get_px(5)), style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX  ^ wx.CLOSE_BOX)
    init_frame.SetSizeHints(get_px(8),get_px(5), get_px(8),get_px(5))
    init_frame.SetIcon(icon)
    
    panel = wx.Panel(init_frame)
    panel.SetBackgroundColour((255, 255, 255)) # White background
    label = wx.StaticText(panel, label='\n\n   正在加载中，请稍后…', style=wx.ALIGN_CENTER)
    label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    panel_size = panel.GetClientSize()
    label.SetPosition(((panel_size.width - label.GetSize().width) / 2, (panel_size.height - label.GetSize().height) / 2))
    
    def OnClose(event):
        pass
    init_frame.Bind(wx.EVT_CLOSE, OnClose)
    
    init_frame.Center()
    
    init_frame.Show()
    
    app.MainLoop()
    
    
    







def diary_window():
    dpi = wx.ScreenDC().GetPPI()[0]
    def get_px(cm):
        return round(cm * dpi / 2.54)

    frame = wx.Frame(None, title='程序日志', size=(get_px(20),get_px(16)), style=wx.DEFAULT_FRAME_STYLE)
    frame.SetIcon(icon)
    sizer = wx.BoxSizer(wx.VERTICAL)
    
    label = wx.StaticText(frame, label='当程序出错时，请将以下日志发送给开发者', style=wx.ALIGN_CENTER)
    label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    content = wx.TextCtrl(frame, style=wx.TE_MULTILINE | wx.TE_READONLY)
    copy = wx.Button(frame, label="复制")
    copy.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    
    
    try:
        with open("log.txt", "r", encoding="utf-16") as f:
            text = f.read()
            content.SetValue(text[-5000:])
    except Exception as e:
        print("发生了异常：", e)
        
        
    def copy_to_clipboard(event):
        text_data = wx.TextDataObject(content.GetValue())
        
        clipboard = wx.Clipboard.Get()
        clipboard.Open()
        clipboard.SetData(text_data)
        clipboard.Close()
    copy.Bind(wx.EVT_BUTTON, copy_to_clipboard)  
    
    
    sizer.Add(label, 0, flag=wx.ALL | wx.ALIGN_CENTER, border=0)
    sizer.Add(content, 1, flag=wx.ALL | wx.EXPAND, border=0)
    sizer.Add(copy, 0, flag=wx.ALL | wx.ALIGN_CENTER, border=0)
    frame.SetSizer(sizer)
    
    frame.Show()
    

zoom = 100
    
def web():

    button_height = 0.8
    
    
    
    dpi = wx.ScreenDC().GetPPI()[0]
    def get_cm(pixels):
        return pixels / dpi * 2.54
        
    def get_px(cm):
        return cm * dpi / 2.54
        
        
    
    # 创建框架
    frame = wx.Frame(None, title='聊天机器人-学术版', size=(800,600))
    frame.SetIcon(icon)
    frame.Maximize(True)
    
    # 创建Web视图
    browser = webview.WebView.New(frame)
    browser.LoadURL("http://localhost:40329/")
    
    
    buttons = wx.Panel(frame)
    buttons_sizer = wx.GridSizer(rows=1, cols=2, hgap=0, vgap=0)
    
    diary = wx.Button(buttons, label="程序日志", size=(-1, round(get_px(button_height))))
    diary.Hide()
    diary.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    buttons_sizer.Add(diary, flag=wx.ALL, border=0)
    
    right = wx.Panel(buttons)
    right_sizer = wx.BoxSizer(wx.HORIZONTAL)
    enlarge = wx.Button(right, label="放大", size=(-1, round(get_px(button_height))))
    ensmall = wx.Button(right, label="缩小", size=(-1, round(get_px(button_height))))
    enlarge.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    ensmall.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    show_size = wx.StaticText(right, label="缩放：100% ", size=(-1, round(get_px(button_height))))
    show_size.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    space = wx.Panel(right)
    right_sizer.Add(space, 1, flag=wx.ALL | wx.EXPAND, border=0)
    right_sizer.Add(show_size, 0, flag=wx.ALL, border=0)
    right_sizer.Add(ensmall, 0, flag=wx.ALL, border=0)
    right_sizer.Add(enlarge, 0, flag=wx.ALL, border=0)
    right.SetSizer(right_sizer)
    
    buttons_sizer.Add(right, flag=wx.ALL | wx.EXPAND, border=0)
    
    buttons.SetSizer(buttons_sizer)
    
    
    # 使用sizer布局
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(buttons, round(button_height*100), wx.EXPAND | wx.ALL)
    sizer.Add(browser, round((get_cm(frame.GetSize()[1])-button_height)*100), wx.EXPAND | wx.ALL)
    frame.SetSizer(sizer)
    
    
    def open_diary(event):
        diary_window()
    diary.Bind(wx.EVT_BUTTON, open_diary)  
    
    
    def inc_zoom():
        global zoom
        if(zoom < 200):
            zoom += 10
        return zoom
        
    def dec_zoom():
        global zoom
        if(zoom > 50):
            zoom -= 10
        return zoom
    
    def enlarge_web(event):
        zoom = inc_zoom()
        browser.SetZoomFactor(zoom/100)  
        show_size.SetLabel(f"缩放：{zoom}% ")
    enlarge.Bind(wx.EVT_BUTTON, enlarge_web)  
        
    def ensmall_web(event):
        zoom = dec_zoom()
        browser.SetZoomFactor(zoom/100)  
        show_size.SetLabel(f"缩放：{zoom}% ")
    ensmall.Bind(wx.EVT_BUTTON, ensmall_web)  
    
    def is_ctrl_pressed():
        return wx.GetKeyState(wx.WXK_CONTROL) != 0
    def adjust_web(x, y, dx ,dy):
        if is_ctrl_pressed():
             if dy > 0:
                zoom = inc_zoom()
             elif dy < 0:
                zoom = dec_zoom()
             show_size.SetLabel(f"缩放：{zoom}% ")
    def regist_mouse_listener():
        with Listener(on_scroll=adjust_web) as listener:
            listener.join()
    t = threading.Thread(target=regist_mouse_listener)
    t.daemon = True
    t.start()
    '''def adjust_web(event):
            new_size = int(browser.GetZoomFactor()*100+0.5)-10
            print(browser.GetZoomFactor())
            new_size = int(new_size/10)*10
            browser.SetZoomFactor(new_size/100)  
            show_size.SetLabel(f"缩放：{new_size}% ")
    browser.Bind(wx.EVT_MOUSEWHEEL, adjust_web)'''
    
    import wx.html2 as wx2
    import webbrowser
    def OnNavigating(event):
        url = event.GetURL()
        webbrowser.open_new_tab(url)
    browser.Bind(wx2.EVT_WEBVIEW_NEWWINDOW, OnNavigating)
    
    # 显示框架
    frame.Show()
    
    # 进入应用程序事件循环
    app.MainLoop()
    
    
    
    
    
    
    

from main import main
import threading, sys

backend_t = threading.Thread(target=main)
backend_t.daemon = True
backend_t.start()

init_t = threading.Thread(target=init_dialog)
init_t.daemon = True
init_t.start()

def check_website_availability(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
while True:
    if check_website_availability("http://localhost:40329/"):
        break
    time.sleep(0.1)
init_frame.Destroy()

web()