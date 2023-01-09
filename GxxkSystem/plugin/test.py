from mpython import *
import time
info=["测试-文字显示","0f永蓝"]
def start():
    oled.fill(0)
    oled.DispChar("Hello World!",0,0)
    oled.show()
    time.sleep(1)