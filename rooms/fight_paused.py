
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class fight_paused():
    def is_fight_paused(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1625,1033 to 1683,1042
        img = self.get_grab(image_grab)
        step = 4
        coltol = 30
        for y_code in range(1030,1036):
            for x_code in range(1624,1626):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(97,146,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(226,245,187),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(170,194,103),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(164,194,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(230,245,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(240,244,219),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(249,255,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(218,233,156),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(129,162,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(133,164,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(246,252,224),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(167,180,122),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(245,255,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(236,243,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(93,140,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(93,138,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(118,151,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(203,216,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(130,154,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(129,159,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(135,164,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(130,161,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(109,147,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(201,214,168),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(86,135,8),coltol)
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
    a=fight_paused()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_fight_paused()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
