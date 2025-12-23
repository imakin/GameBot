
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class arena_popup_close():
    def is_arena_popup_close(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1544,673 to 1563,693
        img = self.get_grab(image_grab)
        step = 3
        coltol = 29
        for y_code in range(600,900):
            for x_code in range(1500,1900):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(50,48,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(108,106,104),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(50,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(50,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(52,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(0))),(95,92,93),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(3))),(101,98,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(102,100,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(3))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(3))),(83,80,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(3))),(50,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(57,54,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(6))),(54,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(6))),(108,106,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(113,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(6))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(6))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(9))),(48,46,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(9))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(9))),(55,53,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(9))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(9))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(9))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(9))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(52,49,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(12))),(113,110,111),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(12))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(114,112,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(12))),(109,106,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(108,106,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(15))),(48,46,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(15))),(114,111,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(15))),(50,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(15))),(54,52,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(15))),(113,111,111),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(15))),(49,46,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(18))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(18))),(85,83,84),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(18))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(18))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(18))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(18))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(18))),(104,102,103),coltol)
                ):
                    x_code += cx(3)
                    y_code += cy(3)
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
    a=arena_popup_close()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_arena_popup_close()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
