
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_help():
    def is_arena_help(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1278,836 to 1301,857
        img = self.get_grab(image_grab)
        step = 3
        coltol = 80
        for y_code in range(800,999):
            for x_code in range(1200,1380):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(35,130,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(56,145,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(194,240,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(213,242,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(212,241,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(123,180,83),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(0))),(53,141,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(0))),(21,121,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(3))),(51,142,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(71,154,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(244,253,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(89,157,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(3))),(87,154,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(3))),(157,189,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(3))),(66,148,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(3))),(41,133,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(142,197,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(6))),(246,250,243),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(243,252,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(6))),(226,238,218),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(246,252,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(6))),(247,250,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(6))),(246,250,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(6))),(53,133,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(9))),(138,196,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(9))),(246,250,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(9))),(247,251,240),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(9))),(127,164,71),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(9))),(222,246,193),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(9))),(246,250,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(9))),(248,249,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(9))),(54,134,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(138,193,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(12))),(245,251,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(12))),(80,145,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(12))),(88,165,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(88,162,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(12))),(203,232,171),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(12))),(246,250,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(12))),(53,132,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(132,190,108),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(15))),(245,251,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(15))),(246,250,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(15))),(109,154,67),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(15))),(217,243,197),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(15))),(245,250,245),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(15))),(248,249,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(15))),(44,126,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(18))),(74,148,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(18))),(213,228,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(18))),(212,230,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(18))),(214,228,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(18))),(214,229,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(18))),(213,228,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(18))),(211,227,202),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(18))),(29,119,9),coltol)
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
    a=arena_help()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_help()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
