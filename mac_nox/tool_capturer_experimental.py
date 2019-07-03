import pyautogui

import time

def tab(x):
  return "  "*x

class main(object):
  def __init__(self):
    self.display("position your mouse then press C button")
    
    print("enter to get x0,y0 mouse pos")
    input()
    x0,y0 = pyautogui.position()
    
    print("capture from",x0,y0,
      "\n",
      "now position your mouse then press C button again"
    )
    print("enter to get x1,y1 mouse pos")
    input()
    x1,y1 = pyautogui.position()
    
    print("will capture from",x0,y0,"to",x1,y1)
    print("press enter to capture screenshot..")
    input()
    img = pyautogui.screenshot(region=(x0,y0,x1-x0,y1-y0))
    img.save("captured_target.png")
    
    step = 2
    print("input resolution detail steps: ")
    step = input()
    step = int(step)*1
    
    #working
    
    code = ""
    code += "import pyautogui\n"
    code += "from setting import cx,cy \n"
    code += "from room_check import RoomCheck\n\n"
    code += "class test(RoomCheck):"+"\n"
    code += tab(1)+"def is_something(self, image_grab=None):" +"\n"
    code += tab(2)+"\"\"\"" +"\n"
    code += tab(2)+"check is in room: "   +"\n"
    code += tab(2)+"@return tuple (x,y) of ..."   +"\n"
    code += tab(2)+"@return False if no"    +"\n"
    code += tab(2)+"\"\"\"" +"\n"
    code += tab(2)+"# captured from %d,%d to %d,%d"%(x0,y0,x1,y1) +"\n"
    code += tab(2)+"img = self.get_grab(image_grab, region=({},{},{},{}))".format(x0,y0,x1,y1)    +"\n"
    
    code += tab(2)+"step = %d"%step+"\n"
    code += tab(2)+"coltol = %d"%10+"\n"
    
    #this is loop for in generated code
    code += tab(2)+"for y_code in range({},{}):".format(y0-3, y0+3) +"\n"
    code += tab(3)+"for x_code in range({},{}):".format(x0-1, x0+1) +"\n"
    code += tab(4)+"if ("+"\n"
    #this is loop for in captured image
    for y in range(0,y1-y0,step):
      for x in range(0,x1-x0,step):
        r,g,b,a = img.getpixel((x,y))
        code += (
            tab(5)+
            ("self.is_color_similar(img.getpixel((x_code+cx({}),y_code+cy({}))),({},{},{}),coltol) and".format(
                (x-x0,y-y0, r,g,b)
              )
            )+
            "\n"
          )
    #remove last " and"
    code = code[:-5]+"\n"
    
    code += tab(4)+"):"+"\n"
    code += tab(5)+"return x_code,y_code"+"\n"
    
    code += tab(2)+"return False"+"\n"
    
    code += tab(1)+"def is_color_similar(self, colorA, colorB, color_tolerance):"+"\n"
    code += tab(2)+  "if ("+"\n"
    code += tab(3)+   "abs(colorA[0]-colorB[0])<color_tolerance and"+"\n"
    code += tab(3)+   "abs(colorA[1]-colorB[1])<color_tolerance and"+"\n"
    code += tab(3)+   "abs(colorA[2]-colorB[2])<color_tolerance"+"\n"
    code += tab(2)+  "):"+"\n"
    code += tab(3)+    "return True"+"\n"
    code += tab(2)+"return False"+"\n"
    
    
    code += "import time"+"\n"
    code += "a=test()"+"\n"
    code += "print(3)"+"\n"
    code += "time.sleep(0.5)"+"\n"
    code += "print(2)"+"\n"
    code += "time.sleep(0.5)"+"\n"
    code += "print(1)"+"\n"
    code += "time.sleep(1)"+"\n"
    code += "c = a.is_something()"+"\n"
    code += "print(c)"+"\n"
    code += "if c:"+"\n"
    code += tab(1)+"pyautogui.moveTo((c[0],c[1]))"+"\n"
    
    f = open("captured_code.py", "w")
    f.write(code)
    f.close()
    
    
  def display(self, *text):
    print(text)
  
app = main()
