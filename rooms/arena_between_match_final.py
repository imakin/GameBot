
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_between_match_final():
    def is_arena_between_match_final(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1479,913 to 1558,925
        img = self.get_grab(image_grab)
        step = 4
        coltol = 70
        for y_code in range(900,999):
            for x_code in range(1450,1500):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(84,141,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(96,146,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(109,154,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(119,160,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(129,164,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(138,168,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(143,172,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(147,173,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(148,174,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(149,174,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(150,174,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(147,173,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(143,172,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(140,169,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(130,165,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(122,160,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(111,156,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(0))),(99,148,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(0))),(86,142,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(0))),(75,137,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(204,233,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(97,139,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(247,255,230),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(251,250,245),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(151,181,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(138,166,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(253,254,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(246,252,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(147,171,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(148,170,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(254,255,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(148,168,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(253,253,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(202,208,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(134,161,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(235,236,220),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(233,246,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(4))),(100,142,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(4))),(88,134,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(4))),(95,135,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(240,250,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(91,137,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(246,255,227),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(247,247,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(251,254,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(242,252,193),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(216,223,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(239,247,193),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(149,171,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(147,169,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(251,252,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(146,167,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(252,252,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(219,227,181),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(252,255,229),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(8))),(235,237,222),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(8))),(234,245,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(8))),(94,139,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(8))),(78,132,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(8))),(81,125,39),coltol)
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
    a=arena_between_match_final()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_between_match_final()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
