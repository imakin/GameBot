
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class find_match():
    def is_find_match(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1011,1039 to 1079,1048
        img = self.get_grab(image_grab)
        step = 4
        coltol = 10
        for y_code in range(1036,1042):
            for x_code in range(1010,1012):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(18,103,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(239,250,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(30,109,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(32,103,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(241,255,240),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(239,250,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(224,250,223),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(206,223,204),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(66,122,61),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(203,224,201),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(17,105,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(189,229,186),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(241,253,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(149,181,145),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(25,103,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(106,171,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(19,103,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(55,128,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(13,96,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(218,228,219),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(27,96,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(251,252,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(246,250,246),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(44,104,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(14,97,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(156,174,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(14,96,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(13,96,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(226,235,226),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(202,216,202),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(148,176,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(19,97,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(106,165,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(13,96,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(12,92,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(84,131,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(36,99,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(40,102,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(15,92,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(40,98,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(29,96,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(34,96,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(19,90,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(36,100,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(10,90,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(25,94,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(10,91,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(27,95,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(33,99,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(8))),(12,91,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(8))),(38,100,32),coltol)
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
    a=find_match()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_find_match()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
