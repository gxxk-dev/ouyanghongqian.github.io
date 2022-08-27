# 摸鱼联盟聊天室

Welcome to the chatroom！

如果这个链接在输入密码后没有正常运作，那大概是CSP的问题，试试[这个链接](http://ouyanghongqian.top/chat)吧！

请在遵守[摸鱼联盟群规](https://ouyanghongqian.top/HostingOfOtherPages/moyulianmong/qungui)的群规下进入聊天室

请注意，此聊天室为匿名聊天室，请在遵守相关法律法规的情况下聊天，同时，本站也使用了一些技术手段您（或用户）不会受到来自其他用户的恶意信息

同时，本站拒绝他人在此在线聊天室上交流八卦，但本站十分欢迎分享作业答案

一切解释权归站长所有

十分感谢[未来邮局](http://topurl.cn)站长开发的嵌入式聊天系统

在您阅读完以上内容并同意之后，请按下下面的按钮，你需要提供一个正确的密码

<script>
    pwd='131477'   //此处的密码经过hash
    function checkpwd(){  
        userpwd=prompt('来，给爷pwd，给了就进聊天室')
        if(userpwd==pwd){
            alert('密码正确 Welcome to the chatroom! 愿风神护佑你');
            console.log('用户密码正确')
            document.getElementById('tag').innerHTML='旅行者，你的身上似乎有了风的气息呢（下次进入时，会自动识别身份并开启聊天，一直到站长更改进入密码）';
            console.log('pwd='+pwd+';islogin=t')
            document.cookie='pwd='+pwd+';islogin=t';
        }else{
            alert('密码不对，给老子爬！');
            window.location.href="https://www.bilibili.com/video/BV1uT4y1P7CX"
        }
    }
    var cookielist=document.cookie.split(';')
    var cookievalue = cookielist[0].split("=")[1];
    if (cookievalue==pwd){
        console.log('cookie正确 注入代码中...')
        console.log('usercookieis ')
        console.log(cookievalue)
        alert('Welcome to the chatroom!')
    }else{   //无用的水代码时间！ 哈哈哈
        if(cookielist[1]=='islogin=t'){
            console.log('用户cookie不正确，但以前登陆过，判定为改密码了')
            alert('hey 站长改密码了 gkd 找他要去');
            checkpwd()
        }else{
            console.log('用户为新用户')
            checkpwd()
        }
    }
</script>

<p id="tag"></p>

<p id="tag2"><script src="//topurl.cn/chat.js" async="async"></script></p>
