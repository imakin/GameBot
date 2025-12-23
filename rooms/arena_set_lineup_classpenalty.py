
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_set_lineup_classpenalty():
    def is_arena_set_lineup_classpenalty(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1386,873 to 1399,888
        img = self.get_grab(image_grab)
        step = 3
        coltol = 15
        for y_code in range(800,999):
            for x_code in range(1385,1387):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(72,37,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(88,41,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(91,42,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(73,37,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(61,42,44),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(3))),(97,27,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(254,228,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(255,253,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(97,27,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(3))),(72,37,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(125,17,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(6))),(255,223,230),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(255,253,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(6))),(120,19,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(82,33,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(9))),(125,23,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(9))),(255,255,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(9))),(254,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(9))),(117,57,64),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(9))),(83,33,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(97,27,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(12))),(145,73,80),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(12))),(187,167,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(12))),(98,27,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(74,37,41),coltol)
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
    a=arena_set_lineup_classpenalty()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_set_lineup_classpenalty()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
