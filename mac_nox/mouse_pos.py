#!/usr/bin/env python3

import pyautogui
import time

while True:
  pos = pyautogui.position()
  print( pos , end="\t\t")
  sc = pyautogui.screenshot(region=(pos[0]*2-1, pos[1]*2-1, pos[0]*2+1, pos[1]*2+1) )
  print(sc.getpixel((1,1)) )
  #time.sleep(1)
