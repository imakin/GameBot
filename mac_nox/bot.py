"""
functions add random pos or time
"""
import pyautogui
import random

def click(x,y=None, max_d=2):
    if (type(x)==tuple and y==None):
        y = x[1]
        x = x[0]
    try:
        a,b= random.randint(x-max_d,x+max_d),random.randint(y-max_d,y+max_d)
        pyautogui.click(a,b)
    except pyautogui.FailSafeException:
        print("error FailSafeException: ",a,b)
        
def doubleClick(x,y=None, max_d=2):
    if (type(x)==tuple and y==None):
        y = x[1]
        x = x[0]
    try:
        a,b= random.randint(x-max_d,x+max_d),random.randint(y-max_d,y+max_d)
        pyautogui.doubleClick(a,b)
    except pyautogui.FailSafeException:
        print("error FailSafeException: ",a,b)
        
def moveTo(x,y, max_d=2):
    pyautogui.moveTo(
        random.randint(x-max_d,x+max_d),
        random.randint(y-max_d,y+max_d)
    )

def dragTo(x,y, drag_time=None, button="left", max_d=2):
    pyautogui.dragTo(
        random.randint(x-max_d, x+max_d),
        random.randint(y-max_d, y+max_d),
        drag_time or (10/random.randint(10,20)),
        button=button
    )
