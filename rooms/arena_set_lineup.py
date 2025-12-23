
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_set_lineup():
    def is_arena_set_lineup(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1772,1051 to 1822,1060
        img = self.get_grab(image_grab)
        step = 4
        coltol = 10
        for y_code in range(1048,1054):
            for x_code in range(1771,1773):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(19,100,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(254,253,251),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(21,106,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(145,172,143),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(29,109,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(140,168,137),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(37,111,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(154,179,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(48,119,39),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(166,193,166),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(130,175,131),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(233,240,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(19,99,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(16,97,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(244,254,246),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(72,133,68),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(13,95,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(87,154,89),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(11,94,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(120,175,117),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(24,96,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(40,114,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(115,154,114),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(11,96,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(211,220,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(12,95,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(13,88,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(14,89,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(14,89,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(13,90,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(9,91,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(13,88,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(12,89,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(14,90,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(11,91,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(12,89,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(11,90,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(14,89,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(12,90,7),coltol)
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
    a=arena_set_lineup()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_set_lineup()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
