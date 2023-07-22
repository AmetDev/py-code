import pyautogui as pg
import time
i = 277
n= 1000
while i <= n:
    i = i + 20
    print(i)
    time.sleep(2)
    pg.leftClick(58, i)
    pg.hotkey("ctrl", "c")
