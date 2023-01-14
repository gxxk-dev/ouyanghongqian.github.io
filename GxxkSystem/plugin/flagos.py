#mPythonType:0
from mpython import *

import network

my_wifi = wifi()
import GxxkSystem.config
config=GxxkSystem.config.getConfig()
my_wifi.connectWiFi(config[3], config[4])

import ntptime

YeMianShuXianZhi = None

YeMianShu = None

import framebuf

import font.digiface_21

import font.digiface_11

import time

def _E5_BC_80_E6_9C_BA():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    ntptime.settime(8, "time.windows.com")
    YeMianShuXianZhi = 2
    YeMianShu = 1
    display_font(font.digiface_21, 'Flag OS', 30, 20, False, 2)
    display_font(font.digiface_11, 'Beta', 55, 40, False, 2)
    oled.show()
    time.sleep(4)

import music

def _E7_94_B5_E5_AD_90_E9_92_A2_E7_90_B4():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    while not button_a.is_pressed():
        if touchpad_p.is_pressed():
            music.play('C4:2')
            oled.fill(0)
            oled.DispChar(str('1'), 63, 32, 1)
            oled.show()
        if touchpad_y.is_pressed():
            music.play('D4:2')
            oled.fill(0)
            oled.DispChar(str('2'), 63, 32, 1)
            oled.show()
        if touchpad_t.is_pressed():
            music.play('E4:2')
            oled.fill(0)
            oled.DispChar(str('3'), 63, 32, 1)
            oled.show()
        if touchpad_h.is_pressed():
            music.play('F4:2')
            oled.fill(0)
            oled.DispChar(str('4'), 63, 32, 1)
            oled.show()
        if touchpad_o.is_pressed():
            music.play('G4:2')
            oled.fill(0)
            oled.DispChar(str('5'), 63, 32, 1)
            oled.show()
        if touchpad_n.is_pressed():
            music.play('A4:2')
            oled.fill(0)
            oled.DispChar(str('6'), 63, 32, 1)
            oled.show()
        if button_b.is_pressed():
            music.play('B4:2')
            oled.fill(0)
            oled.DispChar(str('7'), 63, 32, 1)
            oled.show()
    _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()

def _E7_94_B5_E5_AD_90_E7_83_9F_E8_8A_B1():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    while not button_a.is_pressed():
        for i in range(60, 31, -3):
            oled.fill(0)
            oled.vline(60, i, 3, 1)
            oled.show()
        oled.fill(0)
        for j in range(3, 28):
            oled.circle(64, 32, j, 1)
            oled.show()
        for j in range(3, 28):
            oled.circle(64, 32, j, 0)
            oled.show()
    _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()

second = None

minute = None

hour = None

def _E6_97_B6_E9_92_9F():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    while not button_a.is_pressed():
        oled.fill(0)
        my_clock.settime()
        my_clock.drawClock()
        oled.show()
        second = time.localtime()[0]
        minute = time.localtime()[0]
        hour = time.localtime()[0] % 12 + time.localtime()[0] // 12
        time.sleep(1)
    _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()

import json

import urequests

def _E4_BB_8A_E6_97_A5_E5_A4_A9_E6_B0_94():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    while not button_a.is_pressed():
        w1 = get_seni_weather("https://api.seniverse.com/v3/weather/now.json?key=SI9mELqugg0ma-J0v", "ip")
        oled.DispChar(str(('地区：' + str(w1["results"][0]["location"]["name"]))), 0, 0, 1)
        oled.DispChar(str(('天气：' + str(w1["results"][0]["now"]["text"]))), 0, 16, 1)
        oled.DispChar(str(('温度：' + str(w1["results"][0]["now"]["temperature"]))), 0, 32, 1)
        oled.show()
        oled.fill(0)
    _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()

def _E5_9B_BE_E5_BD_A2_E5_8C_96_E6_93_8D_E4_BD_9C_E7_95_8C_E9_9D_A2():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    while not button_b.is_pressed():
        oled.fill(0)
        Time__E5_88_A4_E6_96_AD()
        display_font(font.digiface_21, (''.join([str(x) for x in [h, ':', min, ':', s]])), 28, 10, False, 2)
        display_font(font.digiface_11, (''.join([str(x) for x in [time.localtime()[0], '.', time.localtime()[1], '.', time.localtime()[2]]])), 40, 35, False, 2)
        oled.DispChar(str('                 你好'), 0, 48, 1)
        oled.show()
    _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()

h = None

min = None

s = None

def Time__E5_88_A4_E6_96_AD():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    if len(str(time.localtime()[3])) == 11:
        h = '0' + str(time.localtime()[3])
    else:
        h = str(time.localtime()[3])
    if len(str(time.localtime()[4])) == 1:
        min = '0' + str(time.localtime()[4])
    else:
        min = str(time.localtime()[4])
    if len(str(time.localtime()[5])) == 1:
        s = '0' + str(time.localtime()[5])
    else:
        s = str(time.localtime()[5])

tqx0 = None

tqx = None

tqy = None

tqxx = None

tqyy = None

dbxzb = None

df = None

tqyxks = None

import random

def _E5_BC_B9_E7_90_83_E6_B8_B8_E6_88_8F():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    tqx0 = 0
    tqx = 0
    tqy = 0
    tqxx = 0
    tqyy = 1
    dbxzb = 0
    df = 0
    tqyxks = 0
    while True:
        if button_a.is_pressed():
            _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()
        if touchpad_t.is_pressed():
            rgb[0] = (int(255), int(0), int(0))
            rgb.write()
            time.sleep_ms(1)
            time.sleep_ms(300)
            rgb.fill( (0, 0, 0) )
            rgb.write()
            time.sleep_ms(1)
            tqx0 = random.randint(1, 126)
            tqx = tqx0
            tqy = 1
            tqxx = random.randint(-2, 2)
            tqyy = 1
            df = 0
            tqyxks = 1
        if touchpad_h.is_pressed():
            rgb[0] = (int(255), int(0), int(0))
            rgb.write()
            time.sleep_ms(1)
            time.sleep_ms(300)
            rgb.fill( (0, 0, 0) )
            rgb.write()
            time.sleep_ms(1)
            tqyxks = 0
            oled.fill(0)
            oled.show()
        if tqyxks == 0:
            oled.fill(0)
            oled.DispChar(str('掌控板弹球小游戏'), 16, 0, 1)
            oled.DispChar(str('按P向左移，按N向右移'), 0, 32, 1)
            oled.DispChar(str('按H返首页，按T开始！'), 0, 48, 1)
            oled.show()
        if tqyxks == 1:
            oled.fill(0)
            oled.fill_circle(tqx, tqy, 2, 1)
            oled.rect(dbxzb, 62, 19, 2, 1)
            oled.show()
            if tqx < 0:
                tqxx = 0 - tqxx
            elif tqx > 127:
                tqxx = 0 - tqxx
            elif tqy < 0:
                tqyy = 0 - tqyy
            elif tqy > 62 and tqx >= dbxzb and tqx <= dbxzb + 19:
                tqxx = random.randint(-2, 2)
                tqyy = 0 - tqyy
                df = df + 10
                music.pitch(988, 60)
                rgb[0] = (int(51), int(204), int(0))
                rgb.write()
                time.sleep_ms(1)
                time.sleep_ms(30)
                rgb.fill( (0, 0, 0) )
                rgb.write()
                time.sleep_ms(1)
            if touchPad_P.read() < 400 and dbxzb >= -1:
                dbxzb = dbxzb + -3
            elif touchPad_N.read() < 400 and dbxzb <= 108:
                dbxzb = dbxzb + 3
            elif tqy > 64:
                tqyxks = 2
                oled.fill(0)
                oled.show()
                music.pitch(247, 60)
                rgb[0] = (int(255), int(0), int(0))
                rgb.write()
                time.sleep_ms(1)
                time.sleep_ms(30)
                rgb.fill( (0, 0, 0) )
                rgb.write()
                time.sleep_ms(1)
            tqx = tqx + tqxx
            tqy = tqy + tqyy
        if tqyxks == 2:
            oled.fill(0)
            oled.DispChar(str(str('得分：') + str(df)), 0, 0, 1)
            oled.DispChar(str('游戏结束啦！'), 0, 16, 1)
            oled.DispChar(str('请按T键重新挑战！'), 0, 32, 1)
            oled.show()

def _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    YeMianShu = 1
    while not button_a.is_pressed():
        oled.fill(0)
        oled.DispChar(str('应用菜单'), 40, 0, 1)
        oled.DispChar(str((''.join([str(x) for x in [YeMianShu, '/', YeMianShuXianZhi]]))), 110, 50, 1)
        oled.DispChar(str('时钟'), 0, 16, 1)
        oled.DispChar(str('今日天气'), 0, 32, 1)
        oled.DispChar(str('电子钢琴'), 0, 48, 1)
        oled.show()
        if touchpad_p.is_pressed():
            YeMianShu = YeMianShu + -1
            if YeMianShu < 1:
                YeMianShu = YeMianShuXianZhi
            if YeMianShu == 1:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()
            if YeMianShu == 2:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()
        if touchpad_n.is_pressed():
            YeMianShu = YeMianShu + 1
            if YeMianShu > YeMianShuXianZhi:
                YeMianShu = 1
            if YeMianShu == 1:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()
            if YeMianShu == 2:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()
        if touchpad_y.is_pressed():
            _E6_97_B6_E9_92_9F()
        elif touchpad_t.is_pressed():
            _E4_BB_8A_E6_97_A5_E5_A4_A9_E6_B0_94()
        elif touchpad_h.is_pressed():
            _E7_94_B5_E5_AD_90_E9_92_A2_E7_90_B4()
    _E5_9B_BE_E5_BD_A2_E5_8C_96_E6_93_8D_E4_BD_9C_E7_95_8C_E9_9D_A2()

def _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2():
    global tqx0, YeMianShu, i, h, tqx, YeMianShuXianZhi, min, tqy, j, s, tqxx, tqyy, dbxzb, second, df, minute, tqyxks, hour
    YeMianShu = 2
    while not button_a.is_pressed():
        oled.fill(0)
        oled.DispChar(str('应用菜单'), 40, 0, 1)
        oled.DispChar(str((''.join([str(x) for x in [YeMianShu, '/', YeMianShuXianZhi]]))), 110, 50, 1)
        oled.DispChar(str('弹球游戏'), 0, 16, 1)
        oled.DispChar(str('电子烟花'), 0, 32, 1)
        oled.DispChar(str(''), 0, 48, 1)
        oled.show()
        if touchpad_p.is_pressed():
            YeMianShu = YeMianShu + -1
            if YeMianShu < 1:
                YeMianShu = YeMianShuXianZhi
            if YeMianShu == 1:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()
            if YeMianShu == 2:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()
        if touchpad_n.is_pressed():
            YeMianShu = YeMianShu + 1
            if YeMianShu > YeMianShuXianZhi:
                YeMianShu = 1
            if YeMianShu == 1:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_1()
            if YeMianShu == 2:
                _E7_A8_8B_E5_BA_8F_E5_88_97_E8_A1_A8_2()
        if touchpad_y.is_pressed():
            _E5_BC_B9_E7_90_83_E6_B8_B8_E6_88_8F()
        elif touchpad_t.is_pressed():
            _E7_94_B5_E5_AD_90_E7_83_9F_E8_8A_B1()
        elif touchpad_h.is_pressed():
            pass
    _E5_9B_BE_E5_BD_A2_E5_8C_96_E6_93_8D_E4_BD_9C_E7_95_8C_E9_9D_A2()

def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]

my_clock = Clock(oled, 64, 32, 30)

def get_seni_weather(_url, _location):
    _url = _url + "&location=" + _location.replace(" ", "%20")
    response = urequests.get(_url)
    json = response.json()
    response.close()
    return json

random.seed(time.ticks_cpu())
_E5_BC_80_E6_9C_BA()
_E5_9B_BE_E5_BD_A2_E5_8C_96_E6_93_8D_E4_BD_9C_E7_95_8C_E9_9D_A2()
