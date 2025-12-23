import os, importlib
import time
import mss
import pyautogui
import setting
from setting import cx,cy
from PIL import Image

# from rooms import (
#     window_ready,
#     find_match,
#     find_match_ready,
#     arena_select_opponent,
#     continue_button,
#     arena_set_lineup,
# )
# Path ke folder rooms
ROOMS_PATH = os.path.join(os.path.dirname(__file__), "rooms")
# Ambil semua file .py (kecuali __init__.py)
room_modules = [
    f[:-3] for f in os.listdir(ROOMS_PATH)
    if f.endswith(".py") and f != "__init__.py"
]
# Dynamic import dan ambil class dengan nama sama seperti modul
base_classes = []
for mod_name in room_modules:
    mod = importlib.import_module(f"rooms.{mod_name}")
    cls = getattr(mod, mod_name)  # Asumsi nama class sama dengan nama file
    base_classes.append(cls)



def get_grab(img=None):
    """
    screen shot function, but return img if img is not None
    """
    if img is None:
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Use the first monitor
            sct_img = sct.grab(monitor)
            return Image.frombytes('RGB', sct_img.size, sct_img.rgb)
    else:
        return img

# class RoomCheck(
#     window_ready.window_ready,
#     find_match.find_match,
#     find_match_ready.find_match_ready,
#     arena_select_opponent.arena_select_opponent,
#     continue_button.continue_button,
#     arena_set_lineup.arena_set_lineup
# ):
class RoomCheck(*base_classes):
    def __init__(self):
        self.screen_width = 722
        self.screen_height = 454

        self.last_found_pos = (0,0) #should be filled by is_[name] functions every time they called
    
    
    def get_grab(self, img=None):
        return get_grab(img)
    

    def is_color_similar(self, colorA, colorB, color_tolerance):
        if (
            abs(colorA[0]-colorB[0])<color_tolerance and
            abs(colorA[1]-colorB[1])<color_tolerance and
            abs(colorA[2]-colorB[2])<color_tolerance
        ):
            return True
        return False
    
    
    def window_reposition(self):
        windowpos = self.is_window_ready()
        if windowpos==False:
            setting.printl("window not found")
            return False
        
        setting.printl("window found in {}".format(windowpos))
        if (windowpos[0]==600 and windowpos[1]==100):
            setting.printl("already on place")
            return "onplace"
        pyautogui.moveTo(windowpos[0],windowpos[1])
        time.sleep(0.5)
        pyautogui.dragTo(600,100, 1, button="left")
        return True


