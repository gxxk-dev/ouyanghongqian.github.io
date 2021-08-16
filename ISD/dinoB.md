# Chrome浏览器离线小恐龙游戏刷分bug
离线小恐龙传送门：<chrome://dino>
<kbd>F12</kbd>打开<kbd>开发者工具</kbd>-><kbd>console</kbd>->输入如下代码，分数要多少有多少<br>
Runner.instance_.setSpeed(99999);// 刷分模式<br>
Runner.instance_.gameOver = function(){}// 不会死亡<br>
按<kbd>F5</kbd>恢复更改
