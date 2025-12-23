
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_between_match():
    def is_arena_between_match(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1482,914 to 1555,924
        img = self.get_grab(image_grab)
        step = 5
        coltol = 70
        for y_code in range(800,999):
            for x_code in range(1451,1500):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(88,142,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(0))),(102,150,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(115,156,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(127,162,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(136,166,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(25),y_code+cy(0))),(138,169,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(0))),(138,168,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(35),y_code+cy(0))),(140,168,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(140,168,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(0))),(136,165,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(0))),(131,163,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(55),y_code+cy(0))),(121,159,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(109,152,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(65),y_code+cy(0))),(96,145,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(70),y_code+cy(0))),(78,136,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(245,250,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(252,255,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(249,252,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(128,157,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(5))),(166,181,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(25),y_code+cy(5))),(221,234,156),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(5))),(136,164,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(35),y_code+cy(5))),(253,255,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(5))),(249,252,229),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(5))),(198,212,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(5))),(249,252,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(55),y_code+cy(5))),(253,255,250),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(5))),(249,251,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(65),y_code+cy(5))),(250,254,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(70),y_code+cy(5))),(247,254,240),coltol)
                ):
                    self.last_found_pos = (x_code,y_code)
                    return x_code,y_code
        return False

    def get_grab(self, image_grab):
        # this used for testing, will be overridden when inherited
        global the_get_grab
        if the_get_grab==None:
            from room_check import get_grab as the_get_grab
        return the_get_grab(image_grab)
    def is_color_similar(self, colorA, colorB, color_tolerance):
        if (
            abs(colorA[0]-colorB[0])<color_tolerance and
            abs(colorA[1]-colorB[1])<color_tolerance and
            abs(colorA[2]-colorB[2])<color_tolerance
        ):
            return True
        return False
if __name__=='__main__':
    import pyautogui
    import time
    a=arena_between_match()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_between_match()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
