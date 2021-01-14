### seeyonAjaxGetshell 致远OAseeyon未授权+文件上传批量getshell

影响版本：

    V8.0
    V7.1,V7.1SP1
    V7.0,V7.0SP1,V7.0SP2,V7.0SP3
    V6.0,V6.1SP1,V6.1SP2
    V5.x
    
漏洞危害：
致远OA旧版本某些ajax接口存在未授权访问，攻击者通过构造恶意请求，可在无需登录的情况下上传恶意脚本文件，从而控制服务器。

Note：
    为了方便(懒比)直接调用curl，因此请在Linux下运行。
    
    ip.txt --> 待检测IP
    shell.txt --> shell

shell：http://127.0.0.1/seeyon/SeeyonUpdate1.jspx 密码：rebeyond 冰蝎3连接

#### 转载自：https://github.com/flywuhu/seeyonAjaxGetshell ，感谢大佬分享。
