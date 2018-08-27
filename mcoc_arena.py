import time
import random

import pyautogui

import room_check
import setting
import bot
from setting import cx,cy

class McocArena(object):
    def __init__(self, room_check_object=None):
        self.room_check = room_check_object or room_check.RoomCheck()
        self.reposition_max_wait = 0
    
    def mcoc_get_buttonarenatarget(self):
        setting.printl("mode 1v1")
        return self.room_check.mcoc_find_buttonversus_1v1cinematic()

    def mcoc_arena(self):
        while True:
            if (self.reposition_max_wait>0):
                self.reposition_max_wait -= 1
            
            img = pyautogui.screenshot()
            if (self.room_check.mcoc_is_room_home(img)):
                setting.printl("room: home")
                # click fight button on home
                bot.click(248,155)
                time.sleep(0.5)
                self.reset_flag()
             
            elif (self.room_check.mcoc_is_room_fight(img)):
                self.reset_flag()
                setting.printl("room: home->fight")
                setting.printl("getting versus button")
                versus_button = self.room_check.mcoc_find_buttonversus()
                
                while (versus_button==False):
                    bot.moveTo(125,256)
                    time.sleep(0.2)
                    bot.dragTo(383,280)
                    time.sleep(2)
                    versus_button = self.room_check.mcoc_find_buttonversus()
                    if not self.room_check.mcoc_is_room_fight():
                        break
                if self.room_check.mcoc_is_room_fight():
                    setting.printl("found versusbutton")
                    time.sleep(0.2)
                    bot.click(versus_button)
                    time.sleep(0.5)
            
            elif (self.room_check.mcoc_is_room_versus(img)):
                self.reset_flag()
                setting.printl("room: home->fight->versus")
                versus_target = self.mcoc_get_buttonarenatarget()
                while (versus_target==False):
                    bot.moveTo(125,284)
                    time.sleep(0.2)
                    bot.dragTo(356,240)
                    time.sleep(2)
                    versus_target = self.mcoc_get_buttonarenatarget()
                    if not self.room_check.mcoc_is_room_versus():
                        break
                if self.room_check.mcoc_is_room_versus():
                    setting.printl("found target")
                    time.sleep(0.2)
                    bot.click(versus_target)
                    time.sleep(0.5)
            
            elif (self.room_check.mcoc_is_room_versus_findmatch(img)):
                self.reset_flag()
                setting.printl("room: home->fight->versus->findmatch select champ")
                
                time.sleep(2+random.random())
                helpbt = self.room_check.mcoc_find_buttonversus_findmatchhelp()
                while helpbt:
                    time.sleep(2+random.random())
                    bot.click(helpbt)
                    time.sleep(2+random.random())
                    helpbt = self.room_check.mcoc_find_buttonversus_findmatchhelp()
                
                bot.moveTo(286,225)
                time.sleep(0.3)
                bot.dragTo(156,154)
                time.sleep(1)
                findmatch_bt = self.room_check.mcoc_is_room_versus_findmatch()
                if (findmatch_bt):
                    bot.click(findmatch_bt)
            
            elif (self.room_check.mcoc_is_fighting(img)):
                self.reset_flag()
                setting.printl("room: FIGHTING")
                while self.room_check.mcoc_is_fighting():
                    for x in range(0,10):
                        bot.click(640,326, 5)
                        time.sleep(0.3+random.random()/4)
                    time.sleep(random.random())
                    bot.click(178,400, 10)
                setting.printl("done fighting")
                
                while (
                    not(self.room_check.mcoc_is_loading())
                    and self.room_check.window_is_ready()
                    and not(self.room_check.mcoc_is_fighting_paused())
                ):
                    bot.click(559,326, 50)
                    time.sleep(random.random()/4)
            
            elif (self.room_check.mcoc_is_loading(img)):
                self.reset_flag()
                setting.printl("room: loading")
                
                while self.room_check.mcoc_is_loading():
                    time.sleep(0.5)
            
            elif (self.room_check.mcoc_is_fighting_paused(img)):
                self.reset_flag()
                setting.printl("room: FIGHTING paused")
                resumebt = self.room_check.mcoc_is_fighting_paused()
                if resumebt:
                    bot.click(resumebt)
                    time.sleep(0.3)
            
            elif (self.room_check.mcoc_is_fighting_recovered(img)):
                self.reset_flag()
                setting.printl("room: FIGHTING recovered")
                resumebt = self.room_check.mcoc_is_fighting_recovered()
                if resumebt:
                    bot.click(resumebt)
                    time.sleep(0.3)
            
            
            elif (self.room_check.mcoc_is_popup(img)):
                self.reset_flag()
                setting.printl("room: there's popup")
                time.sleep(1)
                popupbt = self.room_check.mcoc_is_popup()
                bot.click(popupbt)
            
            elif (self.room_check.mcoc_is_session_offline(img)):
                self.reset_flag()
                setting.printl("room: lost connection")
                bot.click(cx(396),cy(305))
                time.sleep(3)
            
            elif (self.room_check.vysor_is_ads(img)):
                self.reset_flag()
                setting.printl("room: vysor ads")
                bot.click(self.room_check.vysor_is_ads())
            
            else:
                placed = self.room_check.window_reposition()
                if placed=="onplace":
                    self.reposition_max_wait += 2
                    setting.printl("reposition wait: {}".format(self.reposition_max_wait))
                    if self.reposition_max_wait>=10:
                        
                        homebt = self.room_check.vysor_find_buttonhome()
                        if homebt!=None:
                            bot.click(homebt)
                            time.sleep(1)
                            bot.click(homebt)
                            time.sleep(0.5)
                            bot.click(298,149)
                            time.sleep(3)
                            self.reposition_max_wait = 0
                time.sleep(0.3)
            # ~ time.sleep(2)
            
            
            
    def reset_flag(self):
        self.reposition_max_wait =  0
    
app = McocArena()        
app.mcoc_arena()
