
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_select_opponent():
    def is_arena_select_opponent(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1622,1038 to 1733,1052
        img = self.get_grab(image_grab)
        step = 4
        coltol = 30
        for y_code in range(1035,1041):
            for x_code in range(1621,1623):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(104,152,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(108,159,105),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(112,164,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(113,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(112,167,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(112,167,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(113,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(113,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(112,167,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(112,167,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(112,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(113,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(112,167,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(113,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(113,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(113,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(113,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(0))),(112,167,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(0))),(113,166,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(0))),(113,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(112,167,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(84),y_code+cy(0))),(112,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(88),y_code+cy(0))),(112,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(92),y_code+cy(0))),(112,165,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(96),y_code+cy(0))),(112,166,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(0))),(110,163,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(104),y_code+cy(0))),(105,156,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(108),y_code+cy(0))),(64,98,70),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(62,135,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(64,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(64,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(62,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(62,135,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(63,135,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(62,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(63,135,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(62,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(4))),(62,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(4))),(63,135,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(4))),(62,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(84),y_code+cy(4))),(63,135,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(88),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(92),y_code+cy(4))),(64,135,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(96),y_code+cy(4))),(63,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(4))),(63,135,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(104),y_code+cy(4))),(62,136,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(108),y_code+cy(4))),(59,129,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(243,255,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(54,127,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(246,254,245),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(207,219,207),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(163,210,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(222,247,220),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(41,120,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(44,119,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(39,121,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(237,251,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(195,214,194),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(84,134,83),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(49,124,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(83,137,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(234,245,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(8))),(242,253,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(8))),(40,120,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(8))),(214,224,212),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(8))),(53,130,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(8))),(157,187,156),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(8))),(239,252,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(84),y_code+cy(8))),(64,128,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(88),y_code+cy(8))),(213,239,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(92),y_code+cy(8))),(112,171,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(96),y_code+cy(8))),(40,120,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(8))),(73,144,69),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(104),y_code+cy(8))),(53,128,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(108),y_code+cy(8))),(45,119,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(243,254,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(12))),(19,104,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(12))),(245,255,246),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(188,208,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(12))),(250,255,250),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(12))),(220,245,218),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(177,219,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(12))),(19,104,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(12))),(18,105,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(12))),(19,105,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(12))),(190,209,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(12))),(216,238,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(12))),(97,156,93),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(12))),(245,254,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(12))),(31,111,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(12))),(63,116,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(12))),(19,104,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(12))),(211,223,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(12))),(249,251,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(76),y_code+cy(12))),(149,179,146),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(12))),(57,112,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(84),y_code+cy(12))),(242,252,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(88),y_code+cy(12))),(208,236,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(92),y_code+cy(12))),(30,111,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(96),y_code+cy(12))),(143,191,141),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(12))),(57,130,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(104),y_code+cy(12))),(19,104,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(108),y_code+cy(12))),(24,102,19),coltol)
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
    a=arena_select_opponent()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_select_opponent()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
