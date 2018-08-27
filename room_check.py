import time
import pyautogui
import setting
from setting import cx,cy

class RoomCheck(object):
    def __init__(self):
        self.screen_width = 722
        self.screen_height = 454
        pass
    
    
    def get_grab(self, img=None):
        """
        screen shot function, but return img if img is not None
        """
        if img==None:
            return pyautogui.screenshot()
        else:
            return img
    
    
    def vysor_is_ads(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 78,101 to 92,112
        img = self.get_grab(image_grab)
        step = 2
        coltol = 30
        for y_code in range(98,104):
            for x_code in range(77,79):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(33,34,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(52,55,59),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(23,26,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(24,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(25,27,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(71,72,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(23,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(2))),(49,51,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(2))),(216,216,220),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(2))),(52,52,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(2))),(27,27,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(2))),(124,123,129),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(2))),(171,168,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(2))),(24,26,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(23,26,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(46,47,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(222,221,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(4))),(136,135,140),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(171,169,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(4))),(24,25,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(24,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(23,26,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(6))),(23,26,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(6))),(128,130,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(242,241,243),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(6))),(40,41,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(6))),(23,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(23,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(23,26,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(8))),(133,135,141),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(161,161,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(8))),(49,50,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(222,222,226),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(8))),(42,42,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(24,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(70,73,79),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(10))),(154,157,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(10))),(27,29,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(10))),(23,26,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(10))),(52,53,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(10))),(193,192,195),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(10))),(24,26,30),coltol)
                ):
                    return x_code,y_code
        return False
    
    
    def mcoc_is_room_home(self, screenshot=None):
        """
        check if home
        @return coord (x,y) tuple of fight button if found home
        @return False if not in home
        """
        # captured from 232,147 to 279,177
        img = self.get_grab(screenshot)
        step = 1
        coltol = 50
        for y_code in range(146,148):
            for x_code in range(231,234):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(30,106,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(51,83,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(0))),(132,79,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(18,90,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(17,92,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(79,122,75),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(154,198,152),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(5))),(75,113,70),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(10))),(102,58,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(35),y_code+cy(25))),(7,75,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(25))),(3,72,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(25))),(134,92,49),coltol)
                ):
                    setting.printl("room: home")
                    return x_code,y_code
        return False
    
    def mcoc_is_room_fight(self, image_grab=None):
        """
        check if room fight
        @return False if not in home
        """
        # captured from 376,133 to 411,138
        img = self.get_grab(image_grab)
        step = 3
        coltol = 20
        for y_code in range(133,136):
            for x_code in range(375,377):
                if (self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(99,98,125),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(55,56,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(192,190,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(203,203,224),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(0))),(179,179,201),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(0))),(220,220,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(6,8,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(125,125,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(91,90,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(95,93,121),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(3))),(148,146,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(3))),(134,131,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(3))),(119,118,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(33),y_code+cy(3))),(215,213,230),coltol)
                ):
                    return x_code,y_code
        return False


    def mcoc_is_room_versus(self, image_grab=None):
        """
        check is in room: home->fight->versus
        @return tuple (x,y) of multiverse arena
        @return False if no
        """
        # captured from 270,137 to 385,148
        img = self.get_grab(image_grab)
        step = 3
        coltol = 10
        for y_code in range(134,140):
            for x_code in range(269,271):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(45,120,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(48,119,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(6))),(115,188,240),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(6))),(47,121,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(39),y_code+cy(6))),(96,146,181),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(42),y_code+cy(6))),(92,161,213),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(99),y_code+cy(9))),(72,126,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(102),y_code+cy(9))),(47,123,176),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(105),y_code+cy(9))),(66,132,180),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(108),y_code+cy(9))),(102,167,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(111),y_code+cy(9))),(65,123,162),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(114),y_code+cy(9))),(45,122,175),coltol)
                ):
                    return x_code,y_code
        return False


    def mcoc_find_buttonversus(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 321,379 to 406,397
        img = self.get_grab(image_grab)
        step = 5
        coltol = 30
        for y_code in range(376,382):
            for x_code in range(65,335):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(4,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(75),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(2,91,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(76,134,72),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(65,127,63),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(5))),(3,92,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(25),y_code+cy(5))),(8,89,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(5))),(21,101,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(35),y_code+cy(5))),(11,98,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(5))),(4,90,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(45),y_code+cy(5))),(81,143,80),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(5))),(109,167,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(55),y_code+cy(5))),(73,149,69),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(5))),(93,158,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(65),y_code+cy(5))),(10,88,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(70),y_code+cy(5))),(56,136,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(75),y_code+cy(5))),(146,213,143),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(5))),(4,91,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(10))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(70),y_code+cy(10))),(75,140,73),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(75),y_code+cy(10))),(135,202,132),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(10))),(5,91,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(15))),(3,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(15))),(3,92,0),coltol) and\
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(15))),(3,92,0),coltol)
                ):
                    return x_code,y_code
        return False
    
    
    def mcoc_find_buttonversus_1v1cinematic(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 109,290 to 178,346
        img = self.get_grab(image_grab)
        step = 20
        coltol = 20
        for y_code in range(287,293):
            for x_code in range(100,110):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(168,91,142),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(193,84,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(231,182,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(125,57,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(20))),(182,125,122),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(20))),(176,56,143),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(20))),(249,234,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(20))),(214,166,179),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(40))),(159,109,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(40))),(220,80,145),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(40))),(196,136,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(40))),(102,47,64),coltol)
                ):
                    return x_code,y_code
        return False
    
    
    
    def mcoc_is_room_versus_findmatch(self, image_grab=None):
        """
        check is in room: versus->select champ find match
        @return tuple (x,y) of find match button
        @return False if no
        """
        # captured from 188,425 to 195,437
        img = self.get_grab(image_grab)
        step = 1
        coltol = 25
        for y_code in range(422,428):
            for x_code in range(187,189):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(139,98,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(0))),(157,109,64),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(153,103,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(137,90,50),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(79,46,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(1))),(137,94,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(1))),(55,43,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(1))),(51,46,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(2))),(108,68,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(2))),(91,55,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(2))),(86,53,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(2))),(55,28,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(2))),(53,34,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(2))),(54,43,38),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(2))),(52,46,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(3))),(95,58,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(3))),(85,54,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(3))),(79,54,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(48,31,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(3))),(51,40,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(3))),(52,43,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(53,45,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(101,61,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(4))),(102,66,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(86,59,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(4))),(46,31,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(7))),(47,41,39),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(9))),(42,39,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(9))),(44,47,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(9))),(45,50,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(146,111,76),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(10))),(117,83,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(10))),(83,56,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(10))),(51,37,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(10))),(46,42,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(11))),(151,115,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(11))),(156,121,82),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(11))),(126,96,63),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(11))),(74,56,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(11))),(47,49,46),coltol)
                ):
                    return x_code-50,y_code
        return False



    def mcoc_find_buttonversus_findmatchhelp(self, image_grab=None):
        """
        check is in room: findmatch available to ask help
        @return tuple (x,y) of help button
        @return False if no
        """
        # captured from 241,184 to 262,205
        img = self.get_grab(image_grab)
        step = 5
        coltol = 20
        for y_code in range(181,187):
            for x_code in range(240,242):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(14,104,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(0))),(47,129,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(67,133,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(34,122,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(9,100,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(48,121,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(204,221,179),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(190,215,156),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(162,196,122),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(5))),(22,103,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(55,125,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(10))),(195,210,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(10))),(112,156,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(10))),(243,248,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(10))),(30,105,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(35,115,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(15))),(240,247,230),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(15))),(182,206,159),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(15))),(242,247,239),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(15))),(21,97,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(20))),(5,96,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(20))),(23,111,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(20))),(30,112,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(20))),(16,105,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(20))),(9,106,13),coltol)
                ):
                    return x_code+5,y_code+5
        return False


    def mcoc_is_fighting(self, image_grab=None):
        """
        check is in room: fighting
        @return tuple (x,y) of pause button
        @return False if no
        """
        # captured from 385,97 to 408,117
        img = self.get_grab(image_grab)
        step = 5
        coltol = 40
        for y_code in range(94,100):
            for x_code in range(384,386):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(51,83,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(0))),(64,110,62),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(67,119,70),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(62,115,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(33,62,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(19,68,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(83,140,80),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(27,89,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(31,97,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(5))),(19,67,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(15,64,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(10))),(75,130,76),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(10))),(12,71,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(10))),(37,84,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(10))),(5,54,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(7,56,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(15))),(31,95,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(15))),(1,65,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(15))),(12,68,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(15))),(9,58,8),coltol)
                ):
                    return x_code,y_code
        step = 5
        coltol = 30
        for y_code in range(94,100):
            for x_code in range(385,387):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(54,86,41),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(0))),(68,100,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(56,86,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(0))),(50,90,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(5))),(33,78,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(5))),(158,203,149),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(5))),(79,120,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(5))),(40,96,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(10))),(30,67,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(10))),(151,198,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(10))),(73,123,76),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(10))),(33,88,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(15))),(18,63,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(15))),(78,143,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(15))),(4,66,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(15))),(11,80,11),coltol)
                ):
                    return x_code,y_code
        return False
    
    
    
    def mcoc_is_fighting_paused(self, image_grab=None):
        """
        check is in room: FIGHTING paused
        @return tuple (x,y) of resume button
        @return False if no
        """
        # captured from 205,417 to 271,434
        img = self.get_grab(image_grab)
        step = 20
        coltol = 10
        for y_code in range(414,420):
            for x_code in range(204,206):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(28,100,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(29,102,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(29,100,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(29,99,27),coltol)
                ):
                    return cx(544),cy(426)
        return False
    
    
    
    def mcoc_is_fighting_recovered(self, image_grab=None):
        """
        check is in room: FIGHTING recovered
        @return tuple (x,y) of resume button
        @return False if no
        """
        # captured from 318,158 to 469,179
        img = self.get_grab(image_grab)
        step = 20
        coltol = 20
        for y_code in range(155,161):
            for x_code in range(317,319):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(49,48,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(49,47,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(50,47,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(51,47,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(0))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(120),y_code+cy(0))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(140),y_code+cy(0))),(50,47,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(20))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(120),y_code+cy(20))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(140),y_code+cy(20))),(50,47,47),coltol)
                ):
                    return cx(393),cy(357)
        return False
    
    def mcoc_is_session_offline(self, image_grab=None):
        """
        check is in room: Lost Connection
        @return tuple (x,y) of reconnect Button
        @return False if no
        """
        # captured from 267,209 to 529,331
        img = self.get_grab(image_grab)
        step = 50
        coltol = 10
        for y_code in range(206,212):
            for x_code in range(266,268):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(0))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(0))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(150),y_code+cy(0))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(200),y_code+cy(0))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(250),y_code+cy(0))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(150),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(200),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(250),y_code+cy(50))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(100))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(50),y_code+cy(100))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(100))),(37,80,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(150),y_code+cy(100))),(155,184,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(200),y_code+cy(100))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(250),y_code+cy(100))),(50,47,47),coltol)
                ):
                    return cx(396),cy(305)
        return False
    
    
    def mcoc_is_popup(self, image_grab=None):
        """
        check is in room: any popup shown
        @return tuple (x,y) of close button
        @return False if no
        """
        # captured from 488,134 to 501,148
        img = self.get_grab(image_grab)
        step = 4
        coltol = 30
        for y_code in range(90,300):
            for x_code in range(300,700):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(50,49,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(50,49,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(55,54,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(82,81,79),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(87,84,84),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(109,106,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(116,112,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(61,57,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(115,111,111),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(112,108,108),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(55,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(12))),(50,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(12))),(91,88,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(61,58,58),coltol)
                ):
                    return x_code,y_code
        return False

    def mcoc_is_loading(self, image_grab=None):
        """
        check is in room: loading
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 162,166 to 258,276
        img = self.get_grab(image_grab)
        step = 40
        coltol = 30
        for y_code in range(163,169):
            for x_code in range(161,163):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(235,219,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(86,53,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(108,77,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(40))),(71,38,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(40))),(103,78,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(40))),(120,92,51),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(80))),(165,128,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(80))),(113,77,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(80))),(206,202,180),coltol)
                ):
                    return x_code,y_code
        step = 100
        coltol = 10
        for y_code in range(165,171):
            for x_code in range(235,237):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(91,208,148),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(0))),(140,84,75),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(200),y_code+cy(0))),(113,27,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(300),y_code+cy(0))),(180,223,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(100))),(206,217,243),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(100),y_code+cy(100))),(246,235,214),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(200),y_code+cy(100))),(85,70,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(300),y_code+cy(100))),(176,118,199),coltol)
                ):
                    return x_code,y_code
        return False

    def is_color_similar(self, colorA, colorB, color_tolerance):
        if (
            abs(colorA[0]-colorB[0])<color_tolerance and
            abs(colorA[1]-colorB[1])<color_tolerance and
            abs(colorA[2]-colorB[2])<color_tolerance
        ):
            return True
        return False
    
    
    def vysor_find_buttonhome(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 204,716 to 306,767
        img = self.get_grab(image_grab)
        step = 30
        coltol = 10
        for y_code in range(714,718):
            for x_code in range(203,205):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(30))),(69,134,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(30))),(69,134,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(90),y_code+cy(30))),(69,134,231),coltol)
                ):
                    return x_code+50,y_code+50
        for y_code in range(445,452):
            for x_code in range(338,344):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(30),y_code+cy(30))),(69,134,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(30))),(69,134,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(90),y_code+cy(30))),(69,134,231),coltol)
                ):
                    return x_code+50,y_code+50
        return False
    
    def window_is_ready(self):
        vysorpos = pyautogui.locateOnScreen("sprite/phone-windowname-tablet.png")
        if vysorpos==None:
            vysorpos = pyautogui.locateOnScreen("sprite/phone-windowname.png")
            
        return vysorpos!=None

    def window_reposition(self):
        vysorpos = pyautogui.locateOnScreen("sprite/phone-windowname-tablet.png")
        if vysorpos==None:
            setting.printl("window not found")
            return False
        
        setting.printl("window found in {}".format(vysorpos))
        # ~ if (vysorpos[0]==150 and vysorpos[1]==32):#phone
        if (vysorpos[0]==225 and vysorpos[1]==50):
            setting.printl("already on place")
            return "onplace"
        pyautogui.moveTo(vysorpos[0],vysorpos[1])
        time.sleep(0.5)
        pyautogui.dragTo(225,50, 1, button="left")#tablet
        # ~ pyautogui.dragTo(150,32, 1, button="left")#phone
        return True





    def mcoc_is_quest_dialog(self, image_grab=None):
        """
        check is in room: Quest on dialog
        @return tuple (x,y) of skip button
        @return False if no
        """
        # captured from 379,425 to 409,439
        img = self.get_grab(image_grab)
        step = 3
        coltol = 60
        for y_code in range(422,428):
            for x_code in range(378,380):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(18,26,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(6))),(29,38,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(6))),(47,55,78),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(6))),(104,112,141),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(6))),(118,125,158),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(9))),(21,30,64),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(9))),(70,81,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(9))),(139,150,166),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(9))),(95,105,132),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(9))),(206,218,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(9))),(39,49,76),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(9))),(20,27,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(9))),(42,53,75),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(9))),(90,99,126),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(9))),(109,118,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(25,33,71),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(12))),(106,115,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(12))),(37,48,74),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(12))),(158,168,198),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(159,170,194),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(15),y_code+cy(12))),(75,85,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(18),y_code+cy(12))),(34,45,73),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(21),y_code+cy(12))),(46,58,77),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(44,55,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(12))),(26,35,70),coltol)
                ):
                    return x_code,y_code
        step = 3
        coltol = 60
        for y_code in range(427,433):
            for x_code in range(380,382):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(35,67,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(113,146,105),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(115,147,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(0))),(75,107,65),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(36,65,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(9))),(46,75,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(27),y_code+cy(9))),(44,73,30),coltol)
                ):
                    return x_code,y_code
        return False


    
    def mcoc_is_quest_selectpath(self, image_grab=None):
        """
        check is in room: quest->select next node path
        @return tuple (x,y) of exit quest button
        @return False if no
        """
        # captured from 691,392 to 716,415
        img = self.get_grab(image_grab)
        step = 4
        coltol = 40
        for y_code in range(389,395):
            for x_code in range(690,692):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(141,8,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(186,53,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(189,57,51),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(187,50,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(144,2,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(147,0,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(144,0,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(145,6,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(169,94,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(135,6,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(220,99,103),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(137,5,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(4))),(151,5,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(4))),(147,1,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(148,1,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(171,95,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(233,104,108),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(213,134,130),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(232,158,151),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(8))),(143,31,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(146,0,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(12))),(148,1,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(12))),(168,96,94),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(12))),(163,29,33),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(12))),(150,42,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(12))),(222,132,123),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(12))),(130,19,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(12))),(146,1,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(16))),(146,3,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(16))),(164,88,83),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(16))),(144,4,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(16))),(220,95,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(16))),(130,6,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(16))),(147,0,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(16))),(147,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(20))),(143,3,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(20))),(119,19,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(20))),(116,17,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(20))),(121,19,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(20))),(144,1,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(20))),(150,1,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(20))),(149,0,0),coltol)
                ):
                    return x_code,y_code
        return False


    def mcoc_find_buttonquest_nextnode(self, image_grab=None, scope=None):
        """
        find next node button on quest
        @scope
        @return tuple (x,y) of next node button
        @return False if no
        """
        # captured from 505,188 to 515,196
        # 168,127 - 685,405
        img = self.get_grab(image_grab)
        step = 1
        coltol = 40
        if scope==None:
            scope
        for y_code in range(127,405):
            for x_code in range(168,685):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(35,84,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(0))),(37,120,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(33,147,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(0))),(28,156,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(23,158,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(3))),(12,191,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(3),y_code+cy(3))),(9,197,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(3))),(9,200,16),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(3))),(8,197,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(3))),(3,185,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(7),y_code+cy(3))),(0,166,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(3))),(4,141,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(3))),(13,97,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(32,151,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(1),y_code+cy(4))),(20,162,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(23,176,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(5))),(36,123,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(7),y_code+cy(5))),(24,102,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(5))),(12,72,9),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(7))),(49,50,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(5),y_code+cy(7))),(30,29,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(7))),(12,10,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(7),y_code+cy(7))),(7,2,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(7))),(5,2,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(9),y_code+cy(7))),(9,17,24),coltol)
                ):
                    return x_code,y_code
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(83,101,69),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(37,66,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(27,125,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(12,125,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(9,108,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(2,134,6),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(11,133,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(0))),(11,64,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(21,97,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(2))),(79,97,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(2))),(125,151,110),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(2))),(28,136,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(2))),(8,150,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(2))),(3,153,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(2))),(8,151,14),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(2))),(14,126,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(2))),(40,86,31),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(2))),(6,23,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(156,145,133),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(146,147,126),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(57,104,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(4))),(16,140,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(29,151,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(4))),(4,80,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(28,56,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(4))),(25,34,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(4))),(30,42,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(47,67,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(6))),(33,43,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(6))),(121,134,108),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(86,118,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(6))),(55,79,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(6))),(107,123,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(15,42,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(14),y_code+cy(6))),(24,35,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(6))),(60,96,48),coltol)
                ):
                    return x_code,y_code
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(57,59,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(0))),(29,93,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(0))),(19,143,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(0))),(23,157,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(17,138,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(0))),(17,96,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(0))),(49,75,42),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(2))),(58,100,58),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(2))),(18,144,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(2))),(6,186,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(2))),(6,199,13),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(2))),(4,183,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(2))),(10,148,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(2))),(20,99,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(4))),(81,128,87),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(4))),(20,150,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(4))),(6,178,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(4))),(4,193,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(4))),(2,183,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(4))),(8,152,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(4))),(23,99,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(6))),(91,103,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(6))),(91,145,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(6))),(28,144,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(6))),(11,165,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(6))),(13,153,10),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(6))),(17,110,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(6))),(33,58,20),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(84,88,81),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(2),y_code+cy(8))),(44,57,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(4),y_code+cy(8))),(74,106,67),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(6),y_code+cy(8))),(73,113,62),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(33,66,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(10),y_code+cy(8))),(13,29,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(12),y_code+cy(8))),(68,76,61),coltol)
                ):
                    return x_code,y_code
        return False


    def mcoc_is_quest_selectchampion(self, image_grab=None):
        """
        check is in room: Quest->select champion 
        @return tuple (x,y) of fight  button
        @return False if no
        """
        # captured from 403,307 to 449,322
        img = self.get_grab(image_grab)
        step = 8
        coltol = 30
        for y_code in range(304,310):
            for x_code in range(402,404):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(51,47,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(0))),(129,128,132),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(0))),(52,55,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(0))),(82,85,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(0))),(187,190,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(42,43,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(8))),(51,45,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(8),y_code+cy(8))),(46,44,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(16),y_code+cy(8))),(160,169,184),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(24),y_code+cy(8))),(46,51,65),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(32),y_code+cy(8))),(83,88,104),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(8))),(87,89,105),coltol)
                ):
                    return cx(664),cy(431)
        return False



    def mcoc_is_quest_completenext(self, image_grab=None):
        """
        check is in room: quest->complete
        @return tuple (x,y) of next quest button
        @return False if no
        """
        # captured from 227,376 to 326,389
        img = self.get_grab(image_grab)
        step = 20
        coltol = 10
        for y_code in range(373,379):
            for x_code in range(226,228):
                if (
                    self.is_color_similar(img.getpixel((x_code+cx(0),y_code+cy(0))),(21,95,19),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(20),y_code+cy(0))),(33,105,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(40),y_code+cy(0))),(39,105,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(60),y_code+cy(0))),(26,96,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code+cx(80),y_code+cy(0))),(42,106,40),coltol)
                ):
                    return cx(399),cy(379)
        return False
