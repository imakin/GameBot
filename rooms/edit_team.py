
try:
    from setting import cx,cy
except:
    import sys, os
    THISFILEPATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{THISFILEPATH}/..')
    from setting import cx,cy 


the_get_grab = None
class edit_team():
    def is_edit_team(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 975,1027 to 990,1058
        img = self.get_grab(image_grab)
        step = 12
        coltol = 40
        for y_code in range(1024,1050):
            for x_code in range(904,976):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(48,46,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(106,158,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(141,103,61),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(18,103,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(24))),(165,204,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(24))),(10,87,4),coltol)
                ):
                    self.last_found_pos = (x_code+cx(20),y_code+cy(20))
                    return x_code+cx(20),y_code+cy(20)
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
    a=edit_team()
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(1)
    c = a.is_edit_team()
    print(c)
    if c:
        pyautogui.moveTo((c[0],c[1]))
