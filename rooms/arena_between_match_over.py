
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_between_match_over():
    def is_arena_between_match_over(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1353,784 to 1410,798
        img = self.get_grab(image_grab)
        step = 4
        coltol = 90
        for y_code in range(770,900):
            for x_code in range(1300,1404):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(50,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(50,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(51,49,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(255,253,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(53,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(252,252,252),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(54,53,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(254,251,252),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(63,61,62),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(236,235,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(60,59,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(254,252,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(52,49,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(85,85,85),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(206,206,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(255,253,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(251,249,250),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(233,231,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(50,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(251,251,251),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(123,121,122),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(254,252,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(77,75,75),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(101,99,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(12))),(78,76,77),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(92,90,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(12))),(101,98,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(12))),(77,74,75),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(12))),(102,99,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(12))),(102,99,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(12))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(12))),(49,47,48),coltol)
                ):
                    y_code -= 70
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
    a=arena_between_match_over()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_between_match_over()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
