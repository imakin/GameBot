import pyautogui
import sys

import mss
from PIL import Image

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

import time

def tab(x):
    return "    "*x

class main(object):
    def __init__(self):
        self.display("position your mouse then press enter button")
        print("enter the name (used as filename, classname, and function - is_[name] ):")
        try:
            thename = sys.argv[1]
            thename = thename.replace("rooms/","")
            thename = thename.replace(".py","")
        except IndexError:
            thename = input()
        print(f"will use the name {thename}")
        
        print("enter to get x0,y0 mouse pos (1s delay before capture)")
        input()
        x0,y0 = pyautogui.position()
        
        print("capture from",x0,y0,
            "\n",
            "now position your mouse then press enter button again"
        )
        print("enter to get x1,y1 mouse pos")
        input()
        x1,y1 = pyautogui.position()
        
        print("will capture from",x0,y0,"to",x1,y1)
        print("press enter to capture screenshot.. make sure window is focus in 2s")
        input()
        time.sleep(2)
        print("capturing...")
        img = get_grab()
        img_cropped = img.crop((x0, y0, x1, y1))
        img_cropped.save(f"sprite/captured_{thename}.png")
        print(f"image saved to sprite/captured_{thename}.png")
        
        step = 2
        print("input resolution detail steps: ")
        step = input()
        step = int(step)*1
        
        #working
        code = """
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 
"""
        code += "\n\n"
        code += "the_get_grab = None"+"\n"
        code += f"class {thename}():"+"\n"
        code += tab(1)+f"def is_{thename}(self, image_grab=None):"    +"\n"
        code += tab(2)+"\"\"\""    +"\n"
        code += tab(2)+"check is in room: "        +"\n"
        code += tab(2)+"@return tuple (x,y) of ..."        +"\n"
        code += tab(2)+"@return False if no"        +"\n"
        code += tab(2)+"\"\"\""    +"\n"
        code += tab(2)+"# captured from %d,%d to %d,%d"%(x0,y0,x1,y1)    +"\n"
        code += tab(2)+"img = self.get_grab(image_grab)"        +"\n"
        
        code += tab(2)+"step = %d"%step+"\n"
        code += tab(2)+"coltol = %d"%10+"\n"
        
        #this is loop for in generated code
        code += tab(2)+"for y_code in range({},{}):".format(y0-3, y0+3)    +"\n"
        code += tab(3)+"for x_code in range({},{}):".format(x0-1, x0+1)    +"\n"
        code += tab(4)+"if ("+"\n"
        #this is loop for in captured image
        for y in range(y0,y1,step):
            for x in range(x0,x1,step):
                r,g,b = img.getpixel((x,y))
                code += (
                        tab(5)+
                        ("self.is_color_similar(img.getpixel((x_code+cx(%d),y_code+cy(%d))),(%d,%d,%d),coltol) and" %
                            (x-x0,y-y0, r,g,b)
                        )+
                        "\n"
                    )
        #remove last " and"
        code = code[:-5]+"\n"
        
        code += tab(4)+"):"+"\n"
        code += tab(5)+"self.last_found_pos = (x_code,y_code)"+"\n"
        code += tab(5)+"return x_code,y_code"+"\n"
        
        code += tab(2)+"return False"+"\n"

        code +=    f"""
    def get_grab(self, image_grab):
        # this used for testing, will be overridden when inherited
        global the_get_grab
        if the_get_grab==None:
            from room_check import get_grab as the_get_grab
        return the_get_grab(image_grab)
"""
        
        code += tab(1)+"def is_color_similar(self, colorA, colorB, color_tolerance):"+"\n"
        code += tab(2)+"if ("+"\n"
        code += tab(3)+"abs(colorA[0]-colorB[0])<color_tolerance and"+"\n"
        code += tab(3)+"abs(colorA[1]-colorB[1])<color_tolerance and"+"\n"
        code += tab(3)+"abs(colorA[2]-colorB[2])<color_tolerance"+"\n"
        code += tab(2)+"):"+"\n"
        code += tab(3)+"return True"+"\n"
        code += tab(2)+"return False"+"\n"
        
        
        code += "if __name__=='__main__':"+"\n"
        code += tab(1)+"import pyautogui\n"
        code += tab(1)+"import time"+"\n"
        code += tab(1)+f"a={thename}()"+"\n"
        code += tab(1)+"print(3)"+"\n"
        code += tab(1)+"time.sleep(0.5)"+"\n"
        code += tab(1)+"print(2)"+"\n"
        code += tab(1)+"time.sleep(0.5)"+"\n"
        code += tab(1)+"print(1)"+"\n"
        code += tab(1)+"time.sleep(1)"+"\n"
        code += tab(1)+f"c = a.is_{thename}()"+"\n"
        code += tab(1)+"print(c)"+"\n"
        code += tab(1)+"if c:"+"\n"
        code += tab(2)    +    "pyautogui.moveTo((c[0],c[1]))"+"\n"
        
        f = open(f"rooms/{thename}.py", "w")
        f.write(code)
        f.close()
        
        
    def display(self, *text):
        print(text)
    
app = main()
