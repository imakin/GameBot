import pyautogui
import requests
import time
from room_check import get_grab

while True:
    s = get_grab(region=(120*2,150*2,700*2,500*2))
    s.save("/tmp/one.jpg")
    requests.post(
        "https://www.izzulmakin.com/datastorage/file/",
        files={"storagefile":open("/tmp/one.jpg","rb")},
        headers={"Authorization": "Token e0cf9f5e5a443092a7037bebbb237a22d9be9c03"}
    )
    time.sleep(60)
