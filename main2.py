import pyautogui as pg
import time
import keyboard

i = 277
n = 1000
pg.doubleClick(1559, 28)
time.sleep(10)
while i <= n:
    i = i + 20
    pg.leftClick(58, i)

