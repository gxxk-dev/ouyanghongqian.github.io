# 解决网站提示HSTS错误的问题
最近给网站加了HSTS，访问时提示HSTS错误：
```
攻击者可能会试图从 https://ouyanghongqian.top 窃取您的信息（例如：密码、通讯内容或信用卡信息）。
NET::ERR_CERT_COMMON_NAME_INVALID

自动向 Google 报告可能出现的安全事件的详细信息。隐私权政策 重新加载 隐藏详情
https://ouyanghongqian.top 通常会使用加密技术来保护您的信息。Google Chrome 此次尝试连接到 https://ouyanghongqian.top 时，此网站发回了异常的错误凭据。这可能是因为有攻击者在试图冒充 https://ouyanghongqian.top，或 Wi-Fi 登录屏幕中断了此次连接。请放心，您的信息仍然是安全的，因为 Google Chrome 尚未进行任何数据交换便停止了连接。
您目前无法访问 https://ouyanghongqian.top ，因为此网站使用了 HSTS。网络错误和攻击行为通常是暂时的，因此，此网页稍后可能就会恢复正常。了解详情。
```
# 解决方法
打开<chrome://net-internals/#hsts>，滑到最底下Delete domain security policies处输入无法访问的域名，点击Delete后，刷新一下无法访问的网站即可打开。不行就多点Delete几下。
<div id="cc-myssl-id" style="position: fixed;right: 0;bottom: 0;width: 65px;height: 65px;z-index: 99;">
    <a href="https://myssl.com/ouyanghongqian.top?from=mysslid"><img src="https://static.myssl.com/res/images/myssl-id.png" alt="" style="width:100%;height:100%" /></a>
</div>
