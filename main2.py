import pyautogui as pg
import time
import keyboard

i = 277
n = 1000
pg.doubleClick(1559, 28)
time.sleep(10)
pg.leftClick(58, 277)

while i <= n:
    i = i + 20
    print(i)
    pg.hotkey("ctrl", "c")
    keyboard.press("down")
    time.sleep(5)
    pg.leftClick(763, 890)
    time.sleep(5)
    pg.leftClick(112, 48)
    time.sleep(2)
    pg.hotkey("ctrl", "v")
    time.sleep(2)
    pg.leftClick(180, 107)
    time.sleep(2)
    pg.leftClick(710, 838)
    time.sleep(1)
    pg.leftClick(1503, 5)
    time.sleep(1)
    pg.doubleClick(1558, 340)
    time.sleep(2)
    pg.hotkey("ctrl", "a")
    time.sleep(1)
    pg.hotkey("ctrl", "c")
    time.sleep(1)
    pg.leftClick(1455, 176)
    time.sleep(1)
    pg.leftClick(763, 890)
    time.sleep(1)
    pg.hotkey("ctrl", "v")
    time.sleep(1)
    keyboard.press("enter")
    time.sleep(1)
    pg.leftClick(587, 49)
    time.sleep(2)
    pg.leftClick(851, 889)
    time.sleep(3)




