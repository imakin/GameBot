import pyautogui
from setting import cx,cy 
from room_check import RoomCheck

class test(RoomCheck):
    def is_something(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 249,118 to 269,138
        xcode0,ycode0,xcode1,ycode1 = 249,118,249,118
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 9
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(9,223,169),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(254,254,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(241,241,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(255,255,255),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
    def is_color_similar(self, colorA, colorB, color_tolerance):
        if (
            abs(colorA[0]-colorB[0])<color_tolerance and
            abs(colorA[1]-colorB[1])<color_tolerance and
            abs(colorA[2]-colorB[2])<color_tolerance
        ):
            return True
        return False
import time
a=test()
print(3)
time.sleep(0.5)
print(2)
time.sleep(0.5)
print(1)
time.sleep(1)
c = a.is_something()
print(c)
if c:
    pyautogui.moveTo((c[0],c[1]))
