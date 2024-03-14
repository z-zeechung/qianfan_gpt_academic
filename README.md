# GPT学术优化（千帆接口版）使用手册

本项目基于[`GPT 学术优化 (GPT Academic)`](https://github.com/binary-husky/gpt_academic?tab=readme-ov-file)二次开发，系该项目针对百度千帆大模型平台接口的特化版本（别骂我是度孝子，我没精力为所有平台都适配接口）。相比于原项目，该特化版本更加容易安装、使用，对非程序员人群较为友好。

本项目主要功能包括：

+ 基本的大语言模型对话功能，包括闲聊、写作、知识查询、翻译、角色扮演等

+ PDF文档总结、翻译、问答，图像型PDF总结，Word文档总结

+ PPT生成

+ 思维导图绘制

+ GPT联网回答问题

+ 代码解析

尚在开发中的功能：

+ 视频/音频总结

+ 文生图

+ 知识库问答

+ 联网查资料写作/基于知识库写作

要使用该项目，需要首先注册千帆大模型平台账户，并下载对应操作系统的软件包。

## 目录

[**注册千帆大模型平台账户**](#注册千帆大模型平台账户)

[**𝚆𝚒𝚗𝚍𝚘𝚠𝚜端安装**](#𝚆𝚒𝚗𝚍𝚘𝚠𝚜端安装)

[**模型介绍与资费列表**](#模型介绍与资费列表)

## 注册千帆大模型平台账户

**请注意：千帆大模型平台的调用是有偿的，具体资费见文末**

+ 进入[https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application)， 注册/登录账户

+ ![](https://raw.githubusercontent.com/z-zeechung/qianfan_gpt_academic/main/docs\2024-03-14-18-38-54-image.png)
  
  在“应用接入”界面中点击“创建应用”

+ ![](https://raw.githubusercontent.com/z-zeechung/qianfan_gpt_academic/main/docs/2024-03-14-18-40-09-image.png)
  
  输入应用名称和应用描述，服务配置依照默认即可，之后点“确定”

+ ![](https://raw.githubusercontent.com/z-zeechung/qianfan_gpt_academic/main/docs/2024-03-14-18-42-45-image.png)
  
  记下API Key（账户）和Serect Key（密码），待会有用

## 𝚆𝚒𝚗𝚍𝚘𝚠𝚜端安装

+ 下载安装包
  
  下载地址：[](https://github.com/z-zeechung/qianfan_gpt_academic/releases/download/2024%E5%B9%B43%E6%9C%8814%E6%97%A5/Windows.zip)
  
  备用下载地址：[](https://hub.nuaa.cf/z-zeechung/qianfan_gpt_academic/releases/download/2024%E5%B9%B43%E6%9C%8814%E6%97%A5/Windows.zip)

+ 解压安装包

+ ![](https://raw.githubusercontent.com/z-zeechung/qianfan_gpt_academic/main/docs/2024-03-14-18-47-26-image.png)
  
  通过exe启动程序

+ ![](https://raw.githubusercontent.com/z-zeechung/qianfan_gpt_academic/main/docs/2024-03-14-18-49-55-image.png)
  
  在左上角“更换模型”选项卡中填入刚刚记下的API Key（账户）和Serect Key（密码）。

## 模型介绍与资费列表

#### 模型介绍：[API列表 - 千帆大模型平台 | 百度智能云文档](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu)

#### 资费列表：

<table style="table-layout: auto;"><colgroup><col><col style="width: 120px;"><col style="width: 120px;"><col><col style="width: 200px;"><col style="width: 155px;"><col style="width: 90px;"></colgroup><thead class="acud-table-thead"><tr><th class="acud-table-cell">服务名称</th><th class="acud-table-cell">状态</th><th class="acud-table-cell">服务类型</th><th class="acud-table-cell">付费描述</th><th class="acud-table-cell">价格</th><th class="acud-table-cell">开通时间</th><th class="acud-table-cell">操作</th></tr></thead><tbody class="acud-table-tbody"><tr data-row-key="1306" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-4.0-8K大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-4.0-8K模型服务调用时输入、输出token分别计费</td><td class="acud-table-cell"><div class="discont-price"><div>输入：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.12</span>元/千tokens</span><span class="original">¥0.15元/千tokens</span></div></div><div class="discont-price"><div>输出：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.12</span>元/千tokens</span><span class="original">¥0.3元/千tokens</span></div></div></td><td class="acud-table-cell">2024-02-25 16:14:58</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1191" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-3.5-8K大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-3.5-8K模型服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.012元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:54</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1219" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-Bot-turbo-0922大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-Bot-turbo模型服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.008元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:54</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1378" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-Speed-8K大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-Speed-8K模型服务调用时输入、输出token分别计费</td><td class="acud-table-cell"><div class="discont-price"><div>输入：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.004</span>元/千tokens</span></div></div><div class="discont-price"><div>输出：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.008</span>元/千tokens</span></div></div></td><td class="acud-table-cell">2024-02-25 16:15:01</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1230" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">BLOOMZ-7B大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">BLOOMZ-7B模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:55</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1231" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Embedding-V1公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Embedding-V1型服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.002元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:55</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1232" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Prompt模板</td><td class="acud-table-cell"><div class="status normal"><div>免费使用</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">调用时无需计费</td><td class="acud-table-cell">-</td><td class="acud-table-cell">-</td><td class="acud-table-cell">无需开通</td></tr><tr data-row-key="1268" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Llama-2-7B-Chat大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Llama-2-7B-Chat模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:55</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1269" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Llama-2-13B-Chat大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Llama-2-13B-Chat模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.006元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:55</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1270" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Llama-2-70B-Chat大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Llama-2-70B-Chat模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.035元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:56</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1271" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Qianfan-BLOOMZ-7B-compressed大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Qianfan-BLOOMZ-7B-compressed模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:56</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1272" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Qianfan-Chinese-Llama-2-7B大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Qianfan-Chinese-Llama-2-7B模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:56</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1273" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ChatGLM2-6B-32K大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ChatGLM2-6B-32K模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:57</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1274" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">AquilaChat-7B大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">AquilaChat-7B模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:57</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1276" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">bge-large-zh公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">bge-large-zh模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.002元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:57</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1277" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">bge-large-en公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">bge-large-en模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.002元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:57</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1318" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-Bot-8k大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-Bot-8k模型服务调用时输入、输出token分别计费</td><td class="acud-table-cell"><div class="discont-price"><div>输入：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.024</span>元/千tokens</span></div></div><div class="discont-price"><div>输出：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.048</span>元/千tokens</span></div></div></td><td class="acud-table-cell">2024-02-25 16:14:58</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1315" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Stable-Diffusion-XL大模型公有云在线调用-公共资源池算力体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Stable-Diffusion-XL模型服务体验时，平台按公共资源池算力预计占用时长计费。根据图片尺寸不同，算力预计计费时长包含3秒/张、4秒/张、6秒/张和8秒/张四个档位，详情参考价格文档</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.02元/秒</span></td><td class="acud-table-cell">2024-02-25 16:14:58</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1319" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">tokenizer公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">tokenizer服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.0006元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:59</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1358" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE Speed-AppBuilder</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE Speed-AppBuilder基于文心高性能大语言模型ERNIE-Bot-turbo，针对企业级智能客服、内容创作、知识问答等多个任务进行了场景效果和输出格式的优化，需配合“百度智能云千帆AppBuilder” （https://console.bce.baidu.com/ai_apaas/app）产品进行应用开发调试。</td><td class="acud-table-cell"><div class="discont-price"><div>输入：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.004</span>元/千tokens</span></div></div><div class="discont-price"><div>输出：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.008</span>元/千tokens</span></div></div></td><td class="acud-table-cell">2024-02-25 16:14:59</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1359" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Qianfan-Chinese-Llama-2-13B大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Qianfan-Chinese-Llama-2-13B模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.006元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:59</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1360" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">SQLCoder-7B大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">SQLCoder-7B模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:14:59</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1361" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">CodeLlama-7B-Instruct大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">CodeLlama-7B-Instruct模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.004元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:00</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1362" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">XuanYuan-70B-Chat-4bit大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">XuanYuan-70B-Chat-4bit模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.035元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:00</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1370" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ChatLaw公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ChatLaw模型服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.008元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:00</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1363" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Yi-34B-Chat</td><td class="acud-table-cell"><div class="status normal"><div>免费使用</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Yi-34B-Chat模型服务体验时应用此计费项，平台提供算力支持（限时免费）</td><td class="acud-table-cell">-</td><td class="acud-table-cell">-</td><td class="acud-table-cell">无需开通</td></tr><tr data-row-key="1373" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">tao-8k公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">tao-8k模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.002元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:01</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1390" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">Mixtral-8x7B-Instruct大模型公有云在线调用体验服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">Mixtral-8x7B-Instruct模型服务体验时应用此计费项，平台提供算力支持</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.035元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:01</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1421" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-3.5-4K-0205大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-3.5-4K-0205模型服务调用时应用此计费项</td><td class="acud-table-cell"><span class="price" style="color: red;">¥0.012元/千tokens</span></td><td class="acud-table-cell">2024-02-25 16:15:01</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr><tr data-row-key="1422" class="acud-table-row acud-table-row-level-0"><td class="acud-table-cell">ERNIE-3.5-8K-0205大模型公有云在线调用服务</td><td class="acud-table-cell"><div class="status normal"><div>付费使用中</div></div></td><td class="acud-table-cell">预置服务</td><td class="acud-table-cell">ERNIE-3.5-8K-0205模型服务调用时输入、输出token分别计费</td><td class="acud-table-cell"><div class="discont-price"><div>输入：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.024</span>元/千tokens</span></div></div><div class="discont-price"><div>输出：</div><div class="discont-price price-item"><span><span style="color: red;">¥0.048</span>元/千tokens</span></div></div></td><td class="acud-table-cell">2024-02-25 16:15:03</td><td class="acud-table-cell"> <a class="table-action">终止付费</a></td></tr></tbody></table>
