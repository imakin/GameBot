
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class window_ready():
    def is_window_ready(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 571,347 to 639,357
        img = self.get_grab(image_grab)
        step = 3
        coltol = 10
        for y_code in range(50,600):
            for x_code in range(50,1000):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(246,246,246),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(35,35,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(100,100,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(0))),(183,183,183),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(0))),(112,112,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(0))),(88,88,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(33),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(39),y_code+cy(0))),(215,215,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(42),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(0))),(119,119,119),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(237,237,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(51),y_code+cy(0))),(38,38,38),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(54),y_code+cy(0))),(131,131,131),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(57),y_code+cy(0))),(44,44,44),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(205,205,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(63),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(66),y_code+cy(0))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(38,38,38),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(173,173,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(3))),(246,246,246),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(3))),(77,77,77),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(3))),(231,231,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(3))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(3))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(33),y_code+cy(3))),(216,216,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(39),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(42),y_code+cy(3))),(92,92,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(3))),(178,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(51),y_code+cy(3))),(99,99,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(54),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(57),y_code+cy(3))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(3))),(205,205,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(63),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(66),y_code+cy(3))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(172,172,172),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(6))),(238,238,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(6))),(225,225,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(6))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(6))),(118,118,118),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(33),y_code+cy(6))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(6))),(194,194,194),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(39),y_code+cy(6))),(223,223,223),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(42),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(6))),(232,232,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(6))),(157,157,157),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(51),y_code+cy(6))),(34,34,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(54),y_code+cy(6))),(228,228,228),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(57),y_code+cy(6))),(77,77,77),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(6))),(205,205,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(63),y_code+cy(6))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(66),y_code+cy(6))),(247,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(66),y_code+cy(9))),(34,34,34),coltol)
                ):
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
    a=window_ready()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_window_ready()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
