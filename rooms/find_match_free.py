
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class find_match_free():
    def is_find_match_free(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 1000,1045 to 1074,1056
        img = self.get_grab(image_grab)
        step = 4
        coltol = 10
        for y_code in range(1042,1048):
            for x_code in range(999,1001):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(103,167,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(174,218,172),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(91,149,87),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(85,145,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(175,217,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(179,220,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(119,174,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(0))),(17,102,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(84,158,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(0))),(16,102,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(178,220,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(0))),(17,102,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(0))),(48,116,44),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(0))),(174,220,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(0))),(176,218,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(159,213,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(0))),(116,169,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(0))),(29,106,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(0))),(151,197,151),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(248,250,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(228,249,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(129,160,127),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(52,113,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(250,251,251),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(218,229,220),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(82,149,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(4))),(11,96,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(4))),(112,173,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(4))),(108,144,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(4))),(212,240,213),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(4))),(172,221,171),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(4))),(237,250,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(4))),(14,98,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(4))),(11,93,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(4))),(18,93,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(4))),(12,94,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(4))),(232,246,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(4))),(215,225,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(89,128,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(10,92,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(78,123,74),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(15,89,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(145,172,145),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(149,174,149),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(105,139,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(28),y_code+cy(8))),(9,90,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(64,134,62),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(36),y_code+cy(8))),(120,164,119),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(134,174,133),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(44),y_code+cy(8))),(99,138,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(48),y_code+cy(8))),(14,91,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(52),y_code+cy(8))),(10,91,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(56),y_code+cy(8))),(10,90,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(8))),(128,162,128),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(64),y_code+cy(8))),(99,137,96),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(68),y_code+cy(8))),(23,92,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(72),y_code+cy(8))),(126,158,123),coltol)
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
    a=find_match_free()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_find_match_free()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
