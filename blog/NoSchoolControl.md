# 解除机房控制
破解学校机房方法1：
新建扩展名为.bat的文件，在里面写入以下内容：
```
:start
taskkill /f /im _
goto start
```
然后把_换成机房控制的进程名，假设我的机房控制进程名是notepad.exe那么就把_换成notepad.exe，然后保存，编码选择ANSI，运行，等个10秒，机房控制的进程就没了
破解学校机房方法2：
在<https://ouyhq.lanzoui.com/iU1ufuh7sda#95pi>下载文件，运行后输入{机房控制的进程名}，回车，等个10秒，机房控制的进程就没了
