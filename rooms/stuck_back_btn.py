
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class stuck_back_btn():
    def is_stuck_back_btn(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1004,652 to 1041,683
        img = self.get_grab(image_grab)
        step = 12
        coltol = 20
        for y_code in range(649,655):
            for x_code in range(1003,1005):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(51,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(53,50,51),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(51,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(51,48,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(115,112,113),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(12))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(24))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(24))),(49,47,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(24))),(105,103,104),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(24))),(48,46,45),coltol)
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
    a=stuck_back_btn()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_stuck_back_btn()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
