import time
import pyautogui
import setting
from colorsys import rgb_to_hsv

from inspect import stack
from setting import cx,cy,region_x,region_y

class RoomCheck(object):
    def __init__(self):
        self.screen_width = 722
        self.screen_height = 454
        self.last_coord = [0,0]
        self.last_room = None
        self.last_room_time = time.time()
        self.color_similar_depth = 0
        self.color_similar_depth_last_callee = None
        
        pass
    
    
    def get_grab(self, img=None, region=None, rescale=False):
        """
        screen shot function, but return img if img is not None
        """
        if img==None:
            if region==None:
                img = pyautogui.screenshot(region=(0,0,region_x,region_y))
                if rescale:
                    img.thumbnail((int(region_x/2),int(region_y/2)))
                return img
            else:
                return pyautogui.screenshot(region=region)
        else:
            return img
    
    def is_color_similar_rgb(self, colorA, colorB, color_tolerance, colorB_alt=None):
        self.color_similar_depth += 1
        self.color_similar_last_compared = colorA, colorB
        if (
            abs(colorA[0]-colorB[0])<color_tolerance and
            abs(colorA[1]-colorB[1])<color_tolerance and
            abs(colorA[2]-colorB[2])<color_tolerance
        ):
            return True
        if colorB_alt != None:
            if (
                abs(colorA[0]-colorB_alt[0])<color_tolerance and
                abs(colorA[1]-colorB_alt[1])<color_tolerance and
                abs(colorA[2]-colorB_alt[2])<color_tolerance
            ):
                return True
            
        return False
    
    
    def is_color_similar(self, colorA, colorB, color_tolerance, colorB_alt=None):
        self.color_similar_depth += 1
        self.color_similar_last_compared = colorA, colorB
        
        # ~ color_tolerance = color_tolerance*1.4
        
        colora = [int(c*360) for c in rgb_to_hsv(
                    colorA[0]/255,
                    colorA[1]/255,
                    colorA[2]/255
                )
            ]
        colorb = [int(c*360) for c in rgb_to_hsv(
                    colorB[0]/255,
                    colorB[1]/255,
                    colorB[2]/255
                )
            ]
        self.color_similar_last_compared_hsv = colora, colorb
        if (abs(colora[0]-colorb[0])<color_tolerance*1.4):
            if abs(colora[2]-colorb[2])<color_tolerance*3:
                return True
        #gray could have any HUE and value
        if colora[1]<36 and colorb[1]<36 and abs(colora[2]-colorb[2])<color_tolerance*1.4:
            return True
        if colorB_alt!=None:        
            colorb = [int(c*360) for c in rgb_to_hsv(
                        colorB_alt[0]/255,
                        colorB_alt[1]/255,
                        colorB_alt[2]/255
                    )
                ]
            if (abs(colora[0]-colorb[0])<color_tolerance*1.4):
                return True
        return False
        
    
    
    def is_color_dominant(self, color, dominantName, minimumdiff=10):
        """
        @param dominantName: "r", "g", or "b"
        """
        if dominantName=="r":
            return (color[0]>color[1]+minimumdiff and color[0]>color[2]+minimumdiff)
        elif dominantName=="g":
            return (color[1]>color[0]+minimumdiff and color[1]>color[2]+minimumdiff)
        elif dominantName=="b":
            return (color[2]>color[0]+minimumdiff and color[2]>color[1]+minimumdiff)
        return False
    
    
    def color_average_area(self, region, background,  image_grab=None):
        """
        get average color
        @param region: tuple/array [x0, y0, x1, y1]
        @param background: ignored color
        
        REGION must be final multiplied value if display pixel ratio!=1
        """
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        coltol = 10
        rgbsum = [0,0,0]
        rgbcount = 0
        for y in range(region[1], region[3]):
            for x in range(region[0], region[2]):
                color = img.getpixel(
                    (cx(x), cy(y))
                )
                if (self.is_color_similar(color, background, coltol)):
                    pass
                else:
                    rgbcount += 1
                    for i in range(0,3):
                        rgbsum[i] = rgbsum[i]+color[i]
        if rgbcount==0:
            return background
        return int(rgbsum[0]/rgbcount), int(rgbsum[1]/rgbcount), int(rgbsum[2]/rgbcount)
        


    def quest_isin_quest(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        
        xcode0,ycode0,xcode1,ycode1 = 794,556,824,588
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 9
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(159,30,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(27*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(27*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(27*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(27*coord_multiplier))),(146,0,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        # captured from 786,455 to 830,494
        xcode0,ycode0,xcode1,ycode1 = 786,455,830,494
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,1,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(146,1,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(146,1,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(222,178,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(146,1,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(146,1,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(182,85,85),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(146,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(146,1,1),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False
    
    def quest_get_nextnode(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        #portal check
        
        # captured from 406,503 to 496,529
        xcode0,ycode0,xcode1,ycode1 = 406,503,496,529
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(38,123,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(66,146,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(84,160,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(74,152,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(47,130,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(43,127,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(80,157,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(120,190,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(93,168,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(54,135,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return [[x_code,y_code],]
        
        # node normal 
        # captured from 160,128, 777,566
        xcode0,ycode0,xcode1,ycode1 = 160,128, 820,566
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 3
        found = []
        coltol = 30
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if ((
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,202,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,202,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,185,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,139,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(0,202,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(0,202,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(0,181,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(68,68,68),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(119,119,102),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(85,85,68),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(72,70,70),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(34,34,25),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(17,17,17),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(17,17,1),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(0,0,0),coltol)
                ) or (
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,160,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,149,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,163,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,136,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(0,164,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(91,83,76),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(90,90,86),coltol)
                ) or (
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,173,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,170,0),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(74,76,73),coltol) and
                    self.is_color_similar_rgb(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(22,22,16),coltol)
                )):
                    skip = False
                    for x,y in found:
                        if abs(x_code-x)<50 and abs(y_code-y)<50:
                            skip = True
                            break
                    if skip:
                        continue
                    self.last_coord = x_code,y_code
                    found.append( (x_code,y_code,) )
        return found if found else []
        
        
    def quest_portal(self, image_grab=None):
        """
        check is in room: portal select exit
        @return tuple (x,y) of teleport text
        @return False if no
        """
        # captured from 582,70 to 661,107
        xcode0,ycode0,xcode1,ycode1 = 582,70,582,70
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(50,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(50,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(50,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(50,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(235,235,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(228,227,227),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(151,150,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(228,227,227),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(201,201,201),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(235,235,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(107,106,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(234,234,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(50,49,49),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,48,48),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        
    def quest_portal_is_ready(self, image_grab=None):
        """
        check is in room: PORTAL: Teleport button enabled (can teleport)
        @return tuple (x,y) of teleport button
        @return False if no
        """
        # captured from 658,507 to 675,520
        xcode0,ycode0,xcode1,ycode1 = 658,430,658,587
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 100
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(29,115,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
    def quest_portal_get_options_count(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 603,552 to 614,567
        xcode0,ycode0,xcode1,ycode1 = 603,552,603,552 #2 options
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(234,97,91),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(88,38,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(197,49,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(197,49,40),coltol)
                ):
                    return 2
        return False
        
    def quest_complete(self, image_grab=None):
        """
        check is in room: complete dialog
        @return tuple (x,y) of playnext
        @return False if no
        """
        # captured from 406,522 to 520,550
        xcode0,ycode0,xcode1,ycode1 = 406,522,520,550
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,108,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,108,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,108,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(90*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,108,35),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False


    def quest_playnextbutton(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 368,520 to 490,549
        xcode0,ycode0,xcode1,ycode1 = 368,520,490,549
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(100*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(120*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(100*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(120*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(5,78,4),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        
        
    
    def quest_isin_questdialog(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        xcode0,ycode0,xcode1,ycode1 = 323,370,620,608
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 6
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203)) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(206,178,160),coltol,colorB_alt=(165,188,203))
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    print("dialog: 1")
                    return x_code,y_code
        #check for monolog
        c = self.color_average_area((390*2,447*2,530*2,487*2), [0,0,0])
        if self.is_color_similar(c,[184,154,66],20):
            print("monolog")
            return True
        return False
        
        # captured from 429,615 to 474,629
        xcode0,ycode0,xcode1,ycode1 = 429,615,474,629
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 3
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(218,205,202),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(84,33,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(80,31,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(185,166,162),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(204,190,187),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(77,30,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(184,165,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(21*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(84,36,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(77,30,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(250,249,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(75,29,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(33*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(238,234,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(36*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(73,28,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(39*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(69,27,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(42*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(253,253,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(249,247,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(148,114,107),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(119,79,71),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(81,31,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(204,190,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(179,158,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(94,49,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(21*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(80,31,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(79,31,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(250,249,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(79,30,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(33*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(239,234,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(36*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(73,28,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(39*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(73,28,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(42*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(253,253,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(89,35,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(86,33,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(86,33,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(224,214,212),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(205,190,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(94,43,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(203,187,185),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(21*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(82,32,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(80,31,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(250,249,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(79,30,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(33*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(244,241,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(36*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(137,105,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(39*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(130,97,93),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(42*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(75,29,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(227,217,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(94,36,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(92,35,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(210,195,192),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(207,191,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(87,33,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(95,43,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(21*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(204,188,186),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(84,32,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(251,249,249),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(82,31,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(33*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(239,234,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(36*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(82,30,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(39*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(81,30,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(42*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(78,29,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(98,38,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(103,46,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(95,37,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(92,36,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(91,35,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(92,35,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(90,34,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(21*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(87,33,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(86,33,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(27*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(85,32,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(85,32,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(33*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(84,30,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(36*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(82,30,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(39*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(82,30,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(42*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(82,31,26),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False




    def quest_isin_prefight(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of HIGHLIGHTED Fight button
        @return False if no
        """
        # captured from 681,604 to 726,634
        xcode0,ycode0,xcode1,ycode1 = 681,604,681,604
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 20
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(50,115,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(83,131,22),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(120,149,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,74,30),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(83,98,25),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(122,124,19),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # fight button not highlighted
        # captured from 727,612 to 752,634
        xcode0,ycode0,xcode1,ycode1 = 727,612,752,634
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(10,86,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(102,150,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(10,86,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(4,77,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(4,77,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(4,77,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(2,72,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(2,72,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(2,72,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        # heal disabled button
        # captured from 236,615 to 255,631
        xcode0,ycode0,xcode1,ycode1 = 236,615,255,631
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 9
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(151,151,151),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(55,55,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(63,63,63),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(42,43,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(42,43,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(42,43,43),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        
        #heal enabled button
        
        xcode0,ycode0,xcode1,ycode1 = 238,615,253,630
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 6
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(74,128,72),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(175,199,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(47,109,45),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(4,74,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(4,74,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(4,74,2),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False





    def quest_isin_fight(self, image_grab=None):
        """
        check is in room: 
        @return True of pause button
        @return False if no
        """
        # captured from 446,88 to 462,101
        xcode0,ycode0,xcode1,ycode1 = cx(446),cy(88),cx(462),cy(101)
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 8
        coltol = 10
        for y_code in range(ycode0-3,ycode0+3):
            for x_code in range(xcode0-1,xcode0+1):
                # ~ self.color_similar_depth = 0
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(156,186,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(156,186,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(155,183,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(155,183,154),coltol)
                ):
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return True
                # ~ if self.color_similar_depth>0:
                    # ~ print(self.color_similar_depth, self.color_similar_last_compared, self.color_similar_last_compared_hsv)
        return False

    def quest_isin_fight_focus(self, image_grab=None):
        """
        check is in room: fight, image screenshot focus on pause button: 446,88 to 462,101
        @return True of pause button
        @return False if no
        """
        # captured from 446,88 to 462,101
        xcode0,ycode0,xcode1,ycode1 = cx(446),cy(88),cx(462),cy(101)
        img = self.get_grab(image_grab,region=(445*2,87*2,470*2,109*2))
        coord_multiplier = setting.coord_multiplier
        # step = 8
        coltol = 10
        for y_code in range(0,6):
            for x_code in range(0,2):
                # ~ self.color_similar_depth = 0
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(156,186,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(156,186,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(155,183,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(155,183,154),coltol)
                ):
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return True
                # ~ if self.color_similar_depth>0:
                    # ~ print(self.color_similar_depth, self.color_similar_last_compared, self.color_similar_last_compared_hsv)
        return False
        



    def quest_isin_postfight(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 419,409 to 474,440
        xcode0,ycode0,xcode1,ycode1 = 419,409,474,440
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 10
        for y_code in range(ycode0-3,ycode0+3):
            for x_code in range(xcode0-1,xcode0+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(201,200,200),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False


    def is_reconnect(self, image_grab=None):
        """
        check is in room: game disconnected
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 396,401 to 507,429
        xcode0,ycode0,xcode1,ycode1 = 396,401,507,429
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 15
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(45*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(75*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(90*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(105*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(42,113,40),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(7,81,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(45,108,43),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(34,100,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(45*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(254,254,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(25,93,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(75*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(90*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(20,90,18),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(105*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(7,81,5),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False

    def is_popup(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        xcode0,ycode0,xcode1,ycode1 = 491,50, 850,340
        img = self.get_grab(image_grab)
        
        coord_multiplier = setting.coord_multiplier
        # step = 3
        coltol = 15
        try:
            for y_code in range(ycode0-3,ycode1+3):
                for x_code in range(xcode0-1,xcode1+1):
                    if (
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(114,112,112),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(114,112,112),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(57,56,56),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(113,112,112),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(88,87,87),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(107,106,106),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(74,73,73),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(50,48,48),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(114,112,112),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(49,47,47),coltol) and
                        self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(49,47,47),coltol)
                    ):
                        self.last_coord = 822,85
                        if self.last_room!=stack()[0][3]:
                            self.last_room_time = time.time()
                            self.last_room = stack()[0][3]
                        return self.last_coord
            return False
        except IndexError:
            print("popup test error")
            return False
        
        # ~ coord_multiplier = setting.coord_multiplier
        # ~ # step = 8
        # ~ coltol = 15
        # ~ for y_code in range(ycode0-3,ycode1+3):
            # ~ for x_code in range(xcode0-1,xcode1+1):
                # ~ if (
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(114,112,112),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(49,47,47),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(62,60,60),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(113,111,111),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(49,47,47),coltol)
                # ~ ):
                    # ~ self.last_coord = x_code,y_code
                    # ~ return x_code,y_code
        # ~ return False

    def mcoc_fightroom(self, image_grab=None):
        

        # captured from 296,482 to 341,544
        xcode0,ycode0,xcode1,ycode1 = 236,482,801,544
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(95,152,94),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False

    def arena_rogue(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 348,430 to 421,533
        xcode0,ycode0,xcode1,ycode1 = 348,430,421,533
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 50
        coltol = 20
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(76,28,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(251,140,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(50*coord_multiplier))),(251,155,168),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(50*coord_multiplier))),(253,124,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(253,252,130),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(233,108,154),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False
        
    def arena_2nd(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 131,417 to 204,474
        xcode0,ycode0,xcode1,ycode1 = 131,417,204,474
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 10
        for y_code in range(ycode0-1,ycode0+1):
            for x_code in range(xcode0-1,xcode0+2):
                self.color_similar_depth = 0
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(216,154,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,248,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,249,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(250,246,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(254,246,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(255,251,252),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(255,251,252),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(255,245,253),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(255,253,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(254,248,250),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(254,250,251),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(254,234,226),coltol)
                ):
                    self.last_coord = 427,587
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
                if self.color_similar_depth>1:
                    print(self.color_similar_depth, self.color_similar_last_compared)
        return False
        
    def arena_omega(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # pos kedua
        # captured from 800,477 to 843,543
        xcode0,ycode0,xcode1,ycode1 = 800,477,843,543
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 20
        for y_code in range(ycode0-2,ycode0+2):
            for x_code in range(xcode0-1,xcode0+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(230,192,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(233,195,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(177,80,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(170,108,139),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(252,205,185),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(64,8,11),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(120,52,87),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(101,34,35),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(137,25,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(213,152,133),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(92,51,88),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(172,88,108),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        # captured from 361,469 to 437,582
        xcode0,ycode0,xcode1,ycode1 = 361,469,437,582
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 20
        for y_code in range(ycode0-3,ycode0+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(243,145,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(189,55,71),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(254,242,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(255,226,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(163,42,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(113,49,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(188,54,79),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(218,121,117),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(183,76,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(90*coord_multiplier))),(177,157,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(90*coord_multiplier))),(97,132,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(90*coord_multiplier))),(114,141,58),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False


    def arena_hela(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 397,450 to 478,552
        xcode0,ycode0,xcode1,ycode1 = 397,450,478,552
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 35
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(253,217,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(35*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(185,114,65),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(72,96,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(35*coord_multiplier))),(242,178,132),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(35*coord_multiplier),y_code*coord_multiplier+cy(35*coord_multiplier))),(189,100,51),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(35*coord_multiplier))),(35,33,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(70*coord_multiplier))),(229,226,213),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(35*coord_multiplier),y_code*coord_multiplier+cy(70*coord_multiplier))),(30,36,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(70*coord_multiplier),y_code*coord_multiplier+cy(70*coord_multiplier))),(30,33,28),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False

    def arena_korg(self, image_grab=None):
        """
        check is in room: arena selection, searching for korg
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 372,381 to 470,482
        xcode0,ycode0,xcode1,ycode1 = 65,381,760,482
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 20
        coltol = 20
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(229,228,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(147,71,34),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(135,66,27),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(48,28,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(35,16,32),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(223,214,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(163,70,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(214,149,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(138,81,67),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(208,217,200),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(219,201,180),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(133,39,82),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(228,140,119),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(186,105,114),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(174,102,90),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(250,248,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(255,252,248),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(66,17,17),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(230,147,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(191,99,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(140,18,23),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(187,77,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(171,52,68),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(254,243,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(201,134,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(95,13,15),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(198,80,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(254,125,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(255,242,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(80*coord_multiplier),y_code*coord_multiplier+cy(100*coord_multiplier))),(216,160,193),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False

    def mcoc_fightroom_arenashown(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 563,547 to 590,572
        xcode0,ycode0,xcode1,ycode1 = 563,547,590,572
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-1,ycode1+1):
            for x_code in range(xcode0-1,xcode0+200):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(168,199,168),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(144,184,144),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(1,92,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(0,0,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False
        
        
    def arena_champselect(self, image_grab=None):
        """
        check is in room: arena -> edit team
        @return tuple (x,y) of find match button
        @return False if no
        """
        # captured from 100,602 to 122,615
        xcode0,ycode0,xcode1,ycode1 = 100,602,100,602
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 8
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(47,117,46),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(242,246,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(118,164,117),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(13,91,12),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(116,161,116),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(61,124,61),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        """
        check is in room: 
        @return tuple (x,y) of DISABLED find match bt
        @return False if no
        """
        # captured from 109,607 to 122,620
        xcode0,ycode0,xcode1,ycode1 = 109,607,109,607
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 5
        coltol = 10
        for y_code in range(ycode0-2,ycode1+2):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(70,70,70),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(66,66,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(76,76,76),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(52,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(52,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(52,52,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(47,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(47,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(47,47,47),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        """
        check is in room: FInd match enable no cost gold
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 83,604 to 118,640
        xcode0,ycode0,xcode1,ycode1 = 83,604,83,604
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 15
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(38,110,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(38,110,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(38,110,36),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(6,80,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(6,80,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(6,80,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False



    def arena_champselect_champempty(self, image_grab=None):
        """
        check is in room: arena champ select champ still empty
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 184,326 to 230,369
        xcode0,ycode0,xcode1,ycode1 = 184,326,230,369
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(23,25,26),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False



    def arena_enemyselect(self, image_grab=None):
        """
        check is in room: arena select opponent
        @return tuple (x,y) of find new match button
        @return False if no
        """
        # captured from 542,611 to 590,646
        xcode0,ycode0,xcode1,ycode1 = 542,611,542,611
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(190,212,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(118,164,118),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(135,175,135),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(40,111,39),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(4,77,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(4,77,3),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(149,168,192),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(3,62,2),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(106,150,106),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(122,138,159),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(2,71,0),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False

    def arena_rearrangeteam(self, image_grab=None):
        img = self.get_grab(image_grab)
        #all big grey are
        coord_multiplier = setting.coord_multiplier
        coltol = 5
        if (
            self.is_color_similar(img.getpixel((
                        cx(151*coord_multiplier),
                        cy(212*coord_multiplier)
                    )),[49,47,47],coltol) and
            self.is_color_similar(img.getpixel((
                        cx(208*coord_multiplier),
                        cy(519*coord_multiplier)
                    )),[49,47,47],coltol) and
            self.is_color_similar(img.getpixel((
                        cx(752*coord_multiplier),
                        cy(342*coord_multiplier)
                    )),[49,47,47],coltol) and
            self.is_color_similar(img.getpixel((
                        cx(771*coord_multiplier),
                        cy(422*coord_multiplier)
                    )),[49,47,47],coltol) and
            self.is_color_similar(img.getpixel((
                        cx(815*coord_multiplier),
                        cy(255*coord_multiplier)
                    )),[49,47,47],coltol)
            
        ):
            self.last_coord = 713,616
            return self.last_coord 


        """
        check is in room: set lineup arrange team
        @return tuple (x,y) of ...
        @return False if no
        """
        passed = False
        
        # captured from 329,285 to 353,474
        xcode0,ycode0,xcode1,ycode1 = 329,285,353,474
        coord_multiplier = setting.coord_multiplier
        # step = 40
        coltol = 10
        for y_code in range(ycode0,ycode0+1):
            for x_code in range(xcode0,xcode0+1):
                self.color_similar_depth = 0
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(40*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(80*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(120*coord_multiplier))),(23,25,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(160*coord_multiplier))),(23,25,26),coltol)
                ):
                    passed = True
                if not passed and self.color_similar_depth>1:
                    print(self.color_similar_depth, self.color_similar_last_compared, self.color_similar_last_compared_hsv)
        if not(passed):
            return False
        # 1st VS Text
        # captured from 442,295 to 453,302
        xcode0,ycode0,xcode1,ycode1 = 442,295,442,295
        coord_multiplier = setting.coord_multiplier
        # step = 4
        coltol = 10
        for y_code in range(ycode0,ycode0+1):
            for x_code in range(xcode0,xcode0+1):
                self.color_similar_depth = 1000
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(205,212,223),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(238,240,244),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(203,210,221),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(194,204,215),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(45,53,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(191,201,214),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
                print(self.color_similar_depth, self.color_similar_last_compared, self.color_similar_last_compared_hsv)
        """
        check is in room: 
        @return tuple (x,y) of Info button on enemy player
        @return False if no
        """
        # captured from 810,222 to 822,235
        xcode0,ycode0,xcode1,ycode1 = 810,222,810,222
        coord_multiplier = setting.coord_multiplier
        # step = 2
        coltol = 5
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(93,93,93),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(80,80,80),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(62,60,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(98,97,97),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(56,54,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(56,54,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(99,99,99),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(56,54,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(94,94,94),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(56,54,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(100,100,100),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(58,56,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(62,60,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(86,86,86),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(101,101,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(75,74,74),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(49,47,47),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False

    def mcoc_fightrecovered(self, image_grab=None):
        """
        check is in room: fight recovered: the fight recovered text
        @return tuple (x,y) of fight button
        @return False if no
        """
        # captured from 419,203 to 471,237
        xcode0,ycode0,xcode1,ycode1 = 419,203,419,203
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 10
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(105,104,103),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,48,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(163,162,162),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(208,208,208),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(20*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(40*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(50*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol)
                ):
                    self.last_coord = 454,508
                    return 454,508
        return False

    def arena_betweenfight(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 561,272 to 734,303 
        xcode0,ycode0,xcode1,ycode1 = 561,272,734,303
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 15
        for y_code in range(ycode0,ycode0+1):
            for x_code in range(xcode0,xcode0+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(90*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(120*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(150*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(51,48,48),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(90*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(120*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(150*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(49,47,47),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        # captured from 585,360 to 643,430
        xcode0,ycode0,xcode1,ycode1 = 585,360,643,430
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 15
        for y_code in range(ycode0-3,ycode0+3):
            for x_code in range(xcode0-1,xcode0+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,47,47),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(27,32,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(27,32,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(27,32,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(60*coord_multiplier))),(27,32,37),coltol)
                ):
                    self.last_coord = 487,514
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return self.last_coord
        # captured from 308,434 to 394,486
        xcode0,ycode0,xcode1,ycode1 = 308,434,394,486
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 30
        coltol = 10
        for y_code in range(ycode0-3,ycode0+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(134,171,133),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(162,191,161),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(39,37,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(39,37,37),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(60*coord_multiplier),y_code*coord_multiplier+cy(30*coord_multiplier))),(39,37,37),coltol)
                ):
                    self.last_coord = 497,414
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return self.last_coord
        return False
        
        
        
    def arena_champselect_helpneeded(self, image_grab=None):
        
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 298,294 to 314,311
        xcode0,ycode0,xcode1,ycode1 = 298,294,298,294
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 7
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(60,134,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(166,193,137),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(199,216,180),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(246,249,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(251,253,247),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(247,250,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(245,249,242),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(78,141,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(76,139,4),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False
        
        
    def arena_champselect_notmultiplier3(self, image_grab=None):
        """
        check is in room: streak 0
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 329,190 to 347,212
        xcode0,ycode0,xcode1,ycode1 = 329,190,329,190
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 2
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(35,83,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,128,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,133,212),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,123,199),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(35,84,152),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(35,66,131),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(35,80,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(36,104,177),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(35,66,128),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(35,97,169),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(36,95,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(36,98,168),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(36,106,177),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,102,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,90,158),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,81,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,44,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,115,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(36,102,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(36,94,163),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(35,80,146),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(35,43,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(36,114,188),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(36,96,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(35,96,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(35,83,149),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(38,48,104),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(36,107,179),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(35,65,127),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(36,134,213),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(36,99,167),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(35,64,123),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(34,69,131),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(35,118,193),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(35,123,198),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(35,120,194),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(34,78,140),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        """
        check is in room: streak 1
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 330,191 to 346,208
        xcode0,ycode0,xcode1,ycode1 = 330,191,346,208
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 1
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(33,71,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(35,128,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(35,128,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(33,68,130),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,139,219),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(34,116,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,152,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(34,52,111),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(36,136,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(35,117,192),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(34,48,108),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(36,131,209),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(35,122,198),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(33,45,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(36,96,166),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(36,129,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(34,55,116),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(35,43,101),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(35,50,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(11*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(36,151,234),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(34,113,186),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        
        """
        check is in room: winstreak 3
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 332,189 to 349,211
        xcode0,ycode0,xcode1,ycode1 = 332,189,332,189
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 2
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(18,17,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(18,17,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(24,62,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(30,110,179),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(24,62,113),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(24,63,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(33,132,208),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(23,54,103),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(19,17,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(18,17,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(31,114,184),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(19,18,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(19,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(19,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(22,40,85),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(28,92,154),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(20,19,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(19,18,52),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(18,17,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(27,77,136),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(21,19,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(30,104,171),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(33,125,199),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(33,128,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(21,30,73),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(20,18,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(20,18,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(19,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(20,26,66),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(19,17,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(20,21,61),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(31,109,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(20,19,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(21,19,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(19,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(33,131,207),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(19,17,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(19,17,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(19,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(22,21,60),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,109,177),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(21,19,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(27,83,142),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(35,144,224),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(30,109,178),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(36,152,235),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(25,62,112),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(20,19,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(19,18,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(20,19,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(20,19,57),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(19,17,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(20,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(20,19,56),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(19,18,54),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(19,18,53),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(20,18,55),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(20*coord_multiplier))),(20,18,57),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        """
        check is in room: streak 3
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 329,192 to 347,213
        xcode0,ycode0,xcode1,ycode1 = 329,192,329,192
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 1
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(24,70,123),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(29,106,172),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(32,124,196),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(33,132,207),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(33,135,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(32,129,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(31,115,185),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(27,87,149),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(26,80,138),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(35,150,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(30,111,179),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(25,76,130),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(24,65,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(24,64,114),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(24,70,124),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(28,93,155),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(35,145,226),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(32,122,195),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(31,114,183),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(33,135,211),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(26,77,134),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(35,147,229),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(25,70,125),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(32,124,198),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(29,103,168),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(36,152,236),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(27,86,147),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(27,85,142),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(36,154,238),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(28,91,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(36,153,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(28,89,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(26,74,129),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(35,148,230),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(25,73,129),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(23,55,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(24,64,115),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(28,90,150),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(35,144,225),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(32,128,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(27,81,139),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(30,112,181),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(32,127,202),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(34,137,216),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(35,144,224),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(35,145,226),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(33,131,208),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(29,103,169),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(28,91,153),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(35,150,232),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(33,134,210),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(27,83,142),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(23,53,102),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(32,121,193),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(35,143,223),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(11*coord_multiplier))),(33,128,203),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(11*coord_multiplier))),(30,108,176),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(33,130,206),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(29,100,165),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(33,130,205),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(34,141,221),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,119,190),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(31,118,189),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(13*coord_multiplier))),(25,69,123),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(29,96,160),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(11*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(13*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(31,113,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(14*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(30,112,182),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(14*coord_multiplier))),(24,66,120),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        
    def arena_champselect_multiplier1(self, image_grab=None):
        """
        check is in room: champ select multiplier 1x
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 460,194 to 471,208
        xcode0,ycode0,xcode1,ycode1 = 440,194,461,194
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 1
        coltol = 50
        for y_code in range(ycode0,ycode1+1):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(29,101,170),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(4*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(35,150,233),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(29,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(34,143,223),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(30,104,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(1*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(2*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(32,121,195),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(30,104,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(2*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(30,104,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(30,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(4*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(31,106,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(32,106,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(31,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(7*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(30,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(30,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(30,105,174),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(11*coord_multiplier))),(30,105,175),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(11*coord_multiplier))),(36,154,237),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(7*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(32,118,191),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
    def arena_champselect_multiplier125(self, image_grab=None):
        """
        check is in room: multiplier 1.25
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 477,193 to 496,210
        xcode0,ycode0,xcode1,ycode1 = 477,193,496,210
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 3
        coltol = 10
        for y_code in range(ycode0-1,ycode0+3):
            for x_code in range(xcode0-1,xcode0+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(36,150,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(35,93,159),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(38,97,162),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(36,150,233),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(37,82,146),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(3*coord_multiplier))),(39,85,148),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(38,103,173),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(6*coord_multiplier))),(39,139,219),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(40,97,163),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(38,143,224),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(37,136,214),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(3*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(39,123,197),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(6*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(38,139,218),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(38,149,231),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(38,152,234),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        
        
    def is_continuebutton(self, image_grab=None):
        """
        check is in room: there is continue button
        @return tuple (x,y) of the button
        @return False if no
        """
        # captured from 768,613 to 785,636
        xcode0,ycode0,xcode1,ycode1 = 768,613,768,613
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 8
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(31,104,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(31,104,29),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(8*coord_multiplier))),(9,85,7),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(8*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(5,78,4),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(16*coord_multiplier),y_code*coord_multiplier+cy(16*coord_multiplier))),(5,78,4),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        
        """
        check is in room: 
        @return tuple (x,y) of continue/next button july arena
        @return False if no
        """
        # captured from 690,614 to 724,646
        xcode0,ycode0,xcode1,ycode1 = 690,614,690,614
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 12
        coltol = 15
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(46,113,28),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(58,119,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(74,127,24),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(25,92,5),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(116,154,92),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(12*coord_multiplier))),(63,112,8),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(16,81,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(12*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(27,87,1),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(24*coord_multiplier),y_code*coord_multiplier+cy(24*coord_multiplier))),(42,96,1),coltol)
                ):
                    self.last_coord = x_code,y_code
                    return x_code,y_code
        return False
        
        
    def is_champion_info(self, image_grab=None):
        """
        check is in room: 
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 259,127 to 294,156
        xcode0,ycode0,xcode1,ycode1 = 259,127,294,156
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 15
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(218,186,109),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,32,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(49,32,21),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(207,164,74),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(15*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(57,38,26),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(30*coord_multiplier),y_code*coord_multiplier+cy(15*coord_multiplier))),(63,42,29),coltol)
                ):
                    self.last_coord = 84,87
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return self.last_coord
        return False
        
    def mcoc_fightbutton(self, image_grab=None):
        """
        check is in room: menu fight button showns
        @return tuple (x,y) of ... fight button
        @return False if no
        """
        # captured from 205,160 to 217,175
        xcode0,ycode0,xcode1,ycode1 = cx(205),cy(160),cx(217),cy(175)
        img = self.get_grab(image_grab)
        coord_multiplier = setting.coord_multiplier
        # step = 5
        coltol = 20
        for y_code in range(ycode0-2,ycode0+2):
            for x_code in range(xcode0-2,xcode0+2):
                self.color_similar_depth = 0
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(167,195,166),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(195,214,195),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(192,212,191),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(11,87,9),coltol+10) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(54,117,52),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(5*coord_multiplier))),(193,212,192),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol)# and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(5*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(10,86,8),coltol) and
                    # ~ self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(10*coord_multiplier),y_code*coord_multiplier+cy(10*coord_multiplier))),(9,85,7),coltol)
                ):
                    self.last_coord = x_code,y_code
                    if self.last_room!=stack()[0][3]:
                        self.last_room_time = time.time()
                        self.last_room = stack()[0][3]
                    return x_code,y_code
        return False

    def android_home(self, image_grab=None):
        
        """
        check is in room: home, playstore search bar, return point is champions app position
        @return tuple (x,y) of ...
        @return False if no
        """
        # captured from 249,118 to 269,138
        xcode0,ycode0,xcode1,ycode1 = 249,118,249,118
        img = self.get_grab(image_grab)
        coord_multiplier = 2.0
        # step = 9
        coltol = 10
        for y_code in range(ycode0-3,ycode1+3):
            for x_code in range(xcode0-1,xcode1+1):
                if (
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(0*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(9,223,169),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(9*coord_multiplier))),(254,254,254),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(0*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(255,255,255),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(9*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(241,241,241),coltol) and
                    self.is_color_similar(img.getpixel((x_code*coord_multiplier+cx(18*coord_multiplier),y_code*coord_multiplier+cy(18*coord_multiplier))),(255,255,255),coltol)
                ):
                    self.last_coord = 308,356
                    return self.last_coord
        return False