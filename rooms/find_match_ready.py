
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class find_match_ready():
    def is_find_match_ready(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 999,1038 to 1075,1045
        img = self.get_grab(image_grab)
        step = 4
        coltol = 10
        for y_code in range(1035,1041):
            for x_code in range(998,1000):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(158,208,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(213,229,212),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(246,255,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(254,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(160,206,158),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(229,250,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(229,244,227),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(48,128,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(48,127,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(132,170,130),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(237,255,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(50,126,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(250,255,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(211,234,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(227,237,227),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(228,250,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(210,225,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(0))),(230,237,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(0))),(209,239,210),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(246,255,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(92,140,89),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(251,254,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(217,228,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(185,214,184),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(230,250,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(28,112,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(34,111,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(27,112,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(213,240,213),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(82,136,83),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(55,132,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(199,235,196),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(27,111,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(91,141,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(217,227,217),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(29,111,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(4))),(235,238,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(4))),(222,238,220),coltol)
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
    a=find_match_ready()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_find_match_ready()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
