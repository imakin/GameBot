
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class continue_button():
    def is_continue_button(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1786,1052 to 1849,1057
        img = self.get_grab(image_grab)
        step = 4
        coltol = 20
        for y_code in range(1049,1055):
            for x_code in range(1785,1787):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(27,109,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(18,99,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(58,132,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(16,99,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(178,204,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(219,227,217),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(239,251,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(32,105,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(18,98,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(30,101,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(211,229,208),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(154,181,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(63,115,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(241,254,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(228,233,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(19,100,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(17,97,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(45,119,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(33,107,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(23,98,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(142,169,141),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(40,102,38),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(255,254,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(25,101,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(9,93,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(25,95,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(11,96,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(151,178,151),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(125,166,123),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(248,254,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(245,251,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(37,112,33),coltol)
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
    a=continue_button()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_continue_button()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
