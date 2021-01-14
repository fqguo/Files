### seeyonAjaxGetshell 致远OAseeyon未授权漏洞+文件上传批量getshell

#### 转载自：https://github.com/flywuhu/seeyonAjaxGetshell ，感谢大佬分享。

Note：
    为了方便(懒比)直接调用curl，因此请在Linux下运行。
    ip.txt --> 待检测IP
    shell.txt --> shell

shell：http://127.0.0.1/seeyon/SeeyonUpdate1.jspx 密码：rebeyond 冰蝎3连接

2020年1月9日，阿里云应急响应中心监控到致远OA ajaxAction 文件上传漏洞利用代码披露。
漏洞描述

致远OA是一套办公协同软件。近日，阿里云应急响应中心监控到致远OA ajaxAction 文件上传漏洞利用代码披露。由于致远OA旧版本某些ajax接口存在未授权访问，攻击者通过构造恶意请求，可在无需登录的情况下上传恶意脚本文件，从而控制服务器。致远OA官方已针对该漏洞提供补丁，该漏洞利用代码已在互联网上公开流传。阿里云应急响应中心提醒致远OA用户尽快采取安全措施阻止漏洞攻击。
