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
    pg.leftClick(806, 882)
    time.sleep(5)
    pg.leftClick(23, 48)
    time.sleep(2)
    pg.leftClick(113, 400)
    time.sleep(2)
    pg.leftClick(704, 709)
    time.sleep(2)
    pg.leftClick(707, 367)
    pg.hotkey("ctrl", "v")
    pg.leftClick(723, 513)
    pg.hotkey("ctrl", "v")
    pg.leftClick(910, 578)
    time.sleep(2)
    pg.leftClick(1065, 505)
    pg.leftClick(806, 882)


