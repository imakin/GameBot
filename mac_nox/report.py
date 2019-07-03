import pyautogui
import requests
import time
from PIL import Image


while True:
    # ~ print("capturing.. ")
    # ~ s = pyautogui.screenshot(region=(120*2,150*2,700*2,500*2))
    # ~ s = s.convert("L")
    # ~ s.thumbnail((200,200))
    # ~ s.save("one.jpg", "JPEG")
    # ~ r = requests.post(
        # ~ "https://www.izzulmakin.com/datastorage/file/",
        # ~ files={"storagefile":open("one.jpg","rb")},
        # ~ headers={"Authorization": "Token e0cf9f5e5a443092a7037bebbb237a22d9be9c03"},
        # ~ timeout=3
    # ~ )
    # ~ print(r.text)
    with open("log", "r") as f:
        log = f.read()[-1000:]
        try:
            r = requests.post(
                "https://www.izzulmakin.com/datastorage/",
                json={"content":log},
                headers={"Authorization": "Token e0cf9f5e5a443092a7037bebbb237a22d9be9c03"},
                timeout=10
            )
            print("sukses")
        except Exception as e:
            print("error")
            print(e)
            #raise e
    print("sent.")
    
    
    time.sleep(60)
