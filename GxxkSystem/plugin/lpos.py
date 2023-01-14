from mpython import *

import network

my_wifi = wifi()
import GxxkSystem.config
config=GxxkSystem.config.getConfig()
my_wifi.connectWiFi(config[3], config[4])

import ntptime

from mpython_ble.application import HID

from mpython_ble.hidcode import Mouse

def _ble_hid_connect_callback(_1, _2, _3):pass

list = None

xuanquruanjian2 = None

WENBEN = None

C = None

word = None

A = None

H = None

M = None

USER = None

jibu = None

xuenquruanjian = None

kaishicaidanxuanquruanjian = None

shibiejieguo = None

import time

def WLAN():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        if touchpad_p.is_pressed():
            _ble_hid.mouse_click(Mouse.LEFT)
        elif touchpad_y.is_pressed():
            _ble_hid.mouse_click(Mouse.RIGHT)

def clock():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        if M < 0:
            M = 59
        elif M > 59:
            M = 0
        if H < 0:
            H = 23
        elif H > 23:
            H = 0
        if A < 0:
            A = 0
        elif A > 1:
            A = 1
        if accelerometer.get_x() < -0.3:
            if A == 0:
                H = H + 1
            elif A == 1:
                M = M + 5
        elif accelerometer.get_x() > 0.3:
            if A == 0:
                H = H + -1
            elif A == 1:
                M = M + -5
        if accelerometer.get_y() > 0.3:
            A = A + -1
        elif accelerometer.get_y() < -0.3:
            A = A + 1
        if A == 0:
            oled.DispChar(str('时'), 15, 26, 1)
            oled.show()
        elif A == 1:
            oled.DispChar(str('分'), 15, 26, 1)
            oled.show()
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str(str('闹钟:') + str((str(str('时') + str(str(H) + str('/'))) + str(str('分') + str(M))))), 15, 11, 1)
        oled.show()

def on_button_b_pressed(_):
    global shibiejieguo, xuenquruanjian, kaishicaidanxuanquruanjian, USER, word, C, jibu, WENBEN, A, xuanquruanjian2, H, list, M, UDP
    _E5_88_A4_E6_96_AD_E4_B8_BB_E7_95_8C_E9_9D_A2()

button_b.event_pressed = on_button_b_pressed

def _E8_AE_BE_E7_BD_AE():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str('A键连接'), 15, 10, 1)
        oled.DispChar(str('P键断开'), 15, 26, 1)
        oled.show()
        if button_a.is_pressed():
            _ble_hid = HID(name=bytes('mpy_hid', 'utf-8'), battery_level=100)
            _ble_hid.hid_device.connection_callback(_ble_hid_connect_callback)
        if touchpad_p.is_pressed():
            _ble_hid.disconnect()

import audio

import urequests

def _E8_AF_AD_E9_9F_B3_E8_AF_86_E5_88_AB():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str('按A键识别'), 15, 11, 1)
        oled.show()
        if button_a.is_pressed():
            rgb[0] = (int(255), int(0), int(0))
            rgb.write()
            time.sleep_ms(1)
            audio.recorder_init(i2c)
            audio.record('1.wav', 2)
            audio.recorder_deinit()
            rgb[0] = (int(51), int(255), int(51))
            rgb.write()
            time.sleep_ms(1)
            xunfei_params = {"APPID":'', "APISecret":'', "APIKey":''}
            _rsp = urequests.post("http://119.23.66.134:8085/xunfei_iat", files={"file":('1.wav', "audio/wav")}, params=xunfei_params)
            try:
                xunfei_iat_result = _rsp.json()
            except:
                xunfei_iat_result = {"text":""}
            while not touchpad_p.is_pressed():
                if (xunfei_iat_result["text"]) == '关灯':
                    oled.DispChar(str((xunfei_iat_result["text"])), 15, 26, 1)
                    oled.DispChar(str('按P键返回'), 15, 41, 1)
                    oled.show()
                    rgb.fill( (0, 0, 0) )
                    rgb.write()
                    time.sleep_ms(1)
                elif (xunfei_iat_result["text"]) == '开灯':
                    oled.DispChar(str((xunfei_iat_result["text"])), 15, 26, 1)
                    oled.DispChar(str('按P键返回'), 15, 41, 1)
                    oled.show()
                    rgb.fill((int(255), int(255), int(255)))
                    rgb.write()
                    time.sleep_ms(1)
                else:
                    oled.DispChar(str((xunfei_iat_result["text"])), 15, 26, 1)
                    oled.DispChar(str('按P键返回'), 15, 41, 1)
                    oled.show()

def _E8_AE_A1_E6_AD_A5():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(10, 10, 100, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        oled.DispChar(str(str('步数：') + str(jibu)), 15, 11, 1)
        oled.show()
        if accelerometer.get_y() > 0.8:
            jibu = jibu + 1

import machine

def _E5_BC_80_E5_A7_8B():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(30, 0, 55, 45, 0)
        oled.RoundRect(30, 0, 60, 45, 10, 1)
        oled.vline(40, 48, 30, 1)
        oled.vline(60, 48, 30, 1)
        oled.DispChar(str('重启（N）'), 35, 4, 1)
        oled.hline(0, 48, 150, 1)
        oled.show()
        if touchpad_n.is_pressed():
            machine.reset()
        if button_a.is_pressed():
            if kaishicaidanxuanquruanjian == True:
                _E8_AE_BE_E7_BD_AE()
            elif kaishicaidanxuanquruanjian == False:
                pass
        if accelerometer.get_y() < -0.3:
            oled.fill_rect(60, 48, 30, 20, 1)
            oled.show()
            kaishicaidanxuanquruanjian = True
        else:
            oled.fill_rect(60, 48, 30, 20, 0)
            oled.DispChar(str('              LP  设置'), 0, 48, 1)
            oled.show()
            kaishicaidanxuanquruanjian = False

UDP = None

def _E5_88_A4_E6_96_AD_E4_B8_BB_E7_95_8C_E9_9D_A2():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    UDP = False
    while True:
        if list == 0:
            my_1()
        elif list == 1:
            my_2()

import music

def my_1():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not list == 1:
        oled.fill(0)
        oled.DispChar(str('语音识别'), 3, 2, 1)
        oled.DispChar(str('设置'), 61, 2, 1)
        oled.DispChar(str('闹钟'), 3, 21, 1)
        oled.DispChar(str('计步'), 41, 21, 1)
        oled.DispChar(str('BLE'), 76, 21, 1)
        oled.rect(2, 2, 50, 15, 1)
        oled.rect(60, 2, 30, 15, 1)
        oled.rect(2, 20, 30, 15, 1)
        oled.rect(40, 20, 30, 15, 1)
        oled.rect(75, 20, 30, 15, 1)
        oled.DispChar(str('              LP  设置'), 0, 48, 1)
        oled.hline(0, 48, 150, 1)
        oled.vline(40, 48, 30, 1)
        oled.vline(60, 48, 30, 1)
        oled.vline(90, 48, 30, 1)
        oled.show()
        if touchpad_p.is_pressed():
            _E5_BC_80_E5_A7_8B()
        if xuenquruanjian < 0:
            xuenquruanjian = 4
        elif xuenquruanjian > 4:
            xuenquruanjian = 0
        if accelerometer.get_y() > 0.3:
            xuenquruanjian = xuenquruanjian + -1
        elif accelerometer.get_y() < -0.3:
            xuenquruanjian = xuenquruanjian + 1
        if button_a.is_pressed():
            if xuenquruanjian == 0:
                _E8_AF_AD_E9_9F_B3_E8_AF_86_E5_88_AB()
            elif xuenquruanjian == 1:
                _E8_AE_BE_E7_BD_AE()
            elif xuenquruanjian == 2:
                clock()
            elif xuenquruanjian == 3:
                _E8_AE_A1_E6_AD_A5()
            elif xuenquruanjian == 4:
                WLAN()
        if xuenquruanjian == 0:
            oled.fill_rect(2, 2, 50, 15, 1)
            oled.show()
        elif xuenquruanjian == 1:
            oled.fill_rect(60, 2, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 2:
            oled.fill_rect(2, 20, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 3:
            oled.fill_rect(40, 20, 30, 15, 1)
            oled.show()
        elif xuenquruanjian == 4:
            oled.fill_rect(75, 20, 30, 15, 1)
            oled.show()
        if time.localtime()[3] == H and time.localtime()[4] == M and my_wifi.sta.isconnected():
            music.play(music.DONG_FANG_HONG, wait=False, loop=False)
        if accelerometer.get_x() < -0.3:
            list = list + -1
        elif accelerometer.get_x() > 0.3:
            list = list + 1

def _E5_85_B3_E4_BA_8E_E6_88_91_E4_BB_AC():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        oled.fill_rect(5, 5, 110, 50, 0)
        oled.RoundRect(10, 10, 100, 50, 10, 1)
        myUI.qr_code('https://labplus.cn/people/5f25063fb9c98651f298dfcf', 20, 20, scale=1)
        myUI.qr_code('d110101010101@outlook.com', 60, 20, scale=1)
        oled.show()

def my_2():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not list == 0:
        oled.fill(0)
        oled.DispChar(str('              LP  设置'), 0, 48, 1)
        oled.DispChar(str('关于我们'), 3, 2, 1)
        oled.DispChar(str('Light'), 71, 2, 1)
        oled.rect(70, 2, 30, 15, 1)
        oled.rect(2, 2, 60, 15, 1)
        oled.hline(0, 48, 150, 1)
        oled.vline(40, 48, 30, 1)
        oled.vline(60, 48, 30, 1)
        oled.vline(90, 48, 30, 1)
        oled.show()
        if button_a.is_pressed():
            if xuanquruanjian2 == 0:
                _E5_85_B3_E4_BA_8E_E6_88_91_E4_BB_AC()
            elif xuanquruanjian2 == 1:
                my_func()
        if touchpad_p.is_pressed():
            _E5_BC_80_E5_A7_8B()
        if xuanquruanjian2 < 0:
            xuanquruanjian2 = 1
        elif xuanquruanjian2 > 1:
            xuanquruanjian2 = 0
        if accelerometer.get_y() > 0.3:
            xuanquruanjian2 = xuanquruanjian2 + -1
        elif accelerometer.get_y() < -0.3:
            xuanquruanjian2 = xuanquruanjian2 + 1
        if my_wifi.sta.isconnected() and time.localtime()[3] == H and time.localtime()[4] == M:
            music.play(music.DONG_FANG_HONG, wait=False, loop=False)
        if xuanquruanjian2 == 0:
            oled.fill_rect(2, 2, 60, 15, 1)
            oled.show()
        elif xuanquruanjian2 == 1:
            oled.fill_rect(70, 2, 30, 15, 1)
            oled.show()
        if accelerometer.get_x() < -0.3:
            list = list + -1
        elif accelerometer.get_x() > 0.3:
            list = list + 1

def my_func():
    global UDP, M, list, H, xuanquruanjian2, A, WENBEN, jibu, C, word, USER, kaishicaidanxuanquruanjian, xuenquruanjian, shibiejieguo
    while not button_b.is_pressed():
        if button_a.is_pressed():
            rgb.fill((int(255), int(255), int(255)))
            rgb.write()
            time.sleep_ms(1)
        elif touchpad_p.is_pressed():
            rgb.fill( (0, 0, 0) )
            rgb.write()
            time.sleep_ms(1)

myUI = UI(oled)
ntptime.settime(8, "time.windows.com")
_ble_hid = HID(name=bytes('LP OS', 'utf-8'), battery_level=100)
_ble_hid.hid_device.connection_callback(_ble_hid_connect_callback)
list = 0
xuanquruanjian2 = 0
WENBEN = 15
C = False
word = 0
A = 0
H = 0
M = 0
USER = 'LP'
jibu = 0
xuenquruanjian = 0
kaishicaidanxuanquruanjian = False
shibiejieguo = '空'
oled.fill(0)
oled.DispChar(str('              LP MADE'), 0, 0, 1)
oled.DispChar(str('              WELCOME'), 0, 16, 1)
oled.show()
time.sleep(3)
_E5_88_A4_E6_96_AD_E4_B8_BB_E7_95_8C_E9_9D_A2()
