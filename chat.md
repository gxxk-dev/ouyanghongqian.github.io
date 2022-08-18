# 摸鱼联盟聊天室

Welcome to the chatroom！

如果这个链接在输入密码后没有正常运作，那大概是_CSP_的问题，试试[这个链接](http://ouyanghongqian.top/chat)吧！

请在遵守[摸鱼联盟群规](https://ouyanghongqian.top/HostingOfOtherPages/moyulianmong/qungui)的群规下进入聊天室

请注意，此聊天室为匿名聊天室，请在遵守相关法律法规的情况下聊天，同时，本站也使用了一些技术手段您（或用户）不会受到来自其他用户的恶意信息


同时，本站拒绝他人在此在线聊天室上交流八卦，但本站十分欢迎分享作业答案

一切解释权归站长所有

十分感谢[未来邮局](http://topurl.cn)站长开发的嵌入式聊天系统

在您阅读完以上内容并同意之后，请按下下面的按钮，你需要提供一个正确的密码
<script>
    function checkpwd(){
        var pwd=document.getElementById('pwdinput').value;
        if(pwd=='145140'){
            alert('密码正确 Welcome to the chatroom! 愿风神护佑你');
            document.getElementById('tag').innerHTML='';
            var s=document.createElement("script");
            s.src="//topurl.cn/chat.js";
            document.body.append(s);
        }else{
            alert('密码不对，给老子爬！');
        }
    }
</script>
密码：<input type="text" id="pwdinput"/><button onclick="checkpwd()">GO!</button>
<p id="tag">如果密码正确，这句话将消失，同时右下角将会显示聊天框</p>
