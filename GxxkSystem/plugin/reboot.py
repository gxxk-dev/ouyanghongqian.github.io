info=["重启","0f永蓝"]
import time
import machine
from mpython import *
def start():
    oled.fill(0)
    oled.DispChar("将在2s后重启...",0,0)
    oled.DispChar("重启后长按B可进入REPL",0,16,auto_return=True)
    oled.show()
    time.sleep(2)
    machine.reset()