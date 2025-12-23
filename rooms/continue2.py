
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class continue2():
    def is_continue2(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1786,1048 to 1849,1063
        img = self.get_grab(image_grab)
        step = 12
        coltol = 20
        for y_code in range(945,1051):
            for x_code in range(1685,1787):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(34,115,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(36,116,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(36,116,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(35,116,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(36,116,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(33,115,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(16,92,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(17,94,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(17,93,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(12))),(16,93,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(12))),(16,93,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(12))),(15,92,11),coltol)
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
    a=continue2()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_continue2()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
