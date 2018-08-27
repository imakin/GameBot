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
        # captured from 380,276 to 394,286
        img = self.get_grab(image_grab)
        step = 2
        coltol = 10
        for y_code in range(273,279):
            for x_code in range(379,381):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(57,59,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(29,93,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(19,143,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(23,157,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(17,138,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(17,96,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(49,75,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(2))),(58,100,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(2))),(18,144,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(2))),(6,186,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(2))),(6,199,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(2))),(4,183,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(2))),(10,148,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(2))),(20,99,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(81,128,87),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(20,150,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(6,178,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(4))),(4,193,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(2,183,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(4))),(8,152,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(23,99,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(91,103,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(6))),(91,145,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(6))),(28,144,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(11,165,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(6))),(13,153,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(6))),(17,110,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(33,58,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(84,88,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(8))),(44,57,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(74,106,67),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(8))),(73,113,62),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(33,66,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(8))),(13,29,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(68,76,61),coltol)
                ):
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
