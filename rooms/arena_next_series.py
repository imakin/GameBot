
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_next_series():
    def is_arena_next_series(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1778,1050 to 1859,1059
        img = self.get_grab(image_grab)
        step = 4
        coltol = 50
        for y_code in range(1047,1053):
            for x_code in range(1777,1779):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(213,240,199),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(68,128,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(70,131,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(222,242,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(195,225,162),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(125,166,64),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(226,243,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(225,243,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(95,143,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(216,240,184),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(225,244,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(107,152,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(226,243,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(204,232,166),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(226,243,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(90,142,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(83,138,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(0))),(222,241,207),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(0))),(116,167,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(0))),(219,243,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(51,119,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(239,249,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(152,180,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(196,224,176),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(217,230,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(83,133,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(214,225,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(90,136,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(97,138,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(94,140,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(219,231,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(238,247,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(242,250,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(221,231,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(224,238,199),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(245,250,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(92,139,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(226,242,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(4))),(217,230,210),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(4))),(122,162,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(4))),(231,244,230),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(4))),(48,113,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(112,149,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(68,120,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(66,120,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(131,159,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(127,161,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(87,132,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(86,133,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(90,134,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(92,136,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(143,165,103),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(136,161,98),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(92,135,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(141,165,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(130,161,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(83,131,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(8))),(83,129,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(8))),(75,126,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(8))),(126,154,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(8))),(104,146,72),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(8))),(118,149,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(8))),(44,109,15),coltol)
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
    a=arena_next_series()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_next_series()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
