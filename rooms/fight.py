
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class fight():
    def is_fight(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1425,659 to 1458,683
        img = self.get_grab(image_grab)
        step = 2
        coltol = 50
        for y_code in range(656,662):
            for x_code in range(1424,1426):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(27,30,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(60,108,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(64,131,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(26),y_code+cy(0))),(46,98,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(8))),(29,33,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(10))),(13,60,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(10))),(11,95,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(10))),(151,195,144),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(10))),(23,86,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(10))),(61,122,61),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(10))),(149,188,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(10))),(60,120,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(22),y_code+cy(10))),(17,90,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(26),y_code+cy(10))),(7,76,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(10))),(10,36,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(16,30,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(12))),(12,63,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(12))),(12,82,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(14))),(18,87,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(14))),(59,119,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(14))),(151,189,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(14))),(60,123,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(22),y_code+cy(14))),(9,90,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(14))),(30,34,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(16))),(12,29,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(16))),(10,66,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(16))),(111,174,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(16))),(16,87,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(16))),(51,109,44),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(18))),(14,86,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(18))),(9,87,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(18))),(10,79,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(26),y_code+cy(18))),(9,69,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(22))),(2,70,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(22))),(0,66,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(22))),(38,34,37),coltol)
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
    a=fight()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_fight()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
