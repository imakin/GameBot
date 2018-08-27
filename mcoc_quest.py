import time
import random

import pyautogui

import room_check
import setting
import bot
from setting import cx,cy

class McocQuest(object):
    def __init__(self, room_check_object=None):
        self.room_check = room_check_object or room_check.RoomCheck()
        self.reposition_max_wait = 0
    
    def mcoc_get_buttonarenatarget(self):
        setting.printl("mode 1v1")
        return self.room_check.mcoc_find_buttonversus_1v1cinematic()

    def mcoc_quest(self):
        while True:
            if (self.reposition_max_wait>0):
                self.reposition_max_wait -= 1
            
            img = pyautogui.screenshot()
            if (self.room_check.mcoc_is_room_home(img)):
                setting.printl("room: home")
                # click fight button on home
                bot.click(cx(248),cy(155))
                time.sleep(0.5)
                self.reset_flag()
                
            
            
            elif (self.room_check.mcoc_is_fighting(img)):
                self.reset_flag()
                setting.printl("room: FIGHTING")
                while self.room_check.mcoc_is_fighting():
                    for x in range(0,10):
                        bot.click(cx(640),cy(326), 5)
                        time.sleep(0.3+random.random()/4)
                    time.sleep(random.random())
                    bot.click(cx(168),cy(410), 5)
                setting.printl("done fighting")
                time.sleep(1)
                bot.click(cx(559),cy(326), 50)
                
                
                while (
                    not(self.room_check.mcoc_is_loading())
                    and not(self.room_check.mcoc_is_fighting())
                    and self.room_check.window_is_ready()
                    and not(self.room_check.mcoc_is_fighting_paused())
                ):
                    bot.click(cx(559),cy(326), 50)
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
            
            
            elif (self.room_check.mcoc_is_popup(img)):
                self.reset_flag()
                setting.printl("room: there's popup")
                time.sleep(1)
                popupbt = self.room_check.mcoc_is_popup()
                if (popupbt):
                    bot.click(popupbt)
            
            elif (self.room_check.mcoc_is_fighting_recovered(img)):
                self.reset_flag()
                setting.printl("room: FIGHTING recovered")
                resumebt = self.room_check.mcoc_is_fighting_recovered()
                if resumebt:
                    bot.click(resumebt)
                    time.sleep(0.3)
            
            elif (self.room_check.mcoc_is_session_offline(img)):
                self.reset_flag()
                setting.printl("room: lost connection")
                bot.click(cx(396),cy(305))
                time.sleep(3)
                
            
            elif (self.room_check.mcoc_is_quest_dialog(img)):
                setting.printl("room: quest->dialog")
                skipbt = self.room_check.mcoc_is_quest_dialog()
                if (skipbt):
                    bot.click(skipbt)
                    time.sleep(0.5)
                self.reset_flag()
            
            elif (self.room_check.mcoc_is_quest_selectpath(img)):
                setting.printl("room: quest->select path")
                setting.printl("finding next node")
                nextnode = self.room_check.mcoc_find_buttonquest_nextnode()
                while (not(nextnode) and self.room_check.mcoc_is_quest_selectpath() ):
                    nextnode = self.room_check.mcoc_find_buttonquest_nextnode()
                    setting.printl(".")
                    time.sleep(0.1)
                if not(nextnode):
                    setting.printl("doesn't feel like we're in select path")
                else:
                    setting.printl("")
                    setting.printl("nextnode: {}. in 2 second".format(nextnode))
                    pyautogui.moveTo(nextnode)
                    time.sleep(2)
                    bot.click(nextnode)
                self.reset_flag()
            
            elif (self.room_check.mcoc_is_quest_selectchampion(img)):
                setting.printl("room: quest->select champion")
                fightbt = self.room_check.mcoc_is_quest_selectchampion()
                if fightbt:
                    bot.click(fightbt)
                    time.sleep(0.5)
            
            elif (self.room_check.mcoc_is_quest_completenext(img)):
                setting.printl("room: quest->complete")
                nextbt = self.room_check.mcoc_is_quest_completenext()
                if nextbt:
                    bot.click(nextbt)
                    time.sleep(0.5)
            
            elif (self.room_check.vysor_is_ads(img)):
                self.reset_flag()
                setting.printl("room: vysor ads")
                bot.click(self.room_check.vysor_is_ads())
                
            
            else:
                placed = self.room_check.window_reposition()
                if placed=="onplace":
                    self.reposition_max_wait += 2
                    setting.printl("reposition wait: {}".format(self.reposition_max_wait))
                    if self.reposition_max_wait>=20:
                        
                        homebt = self.room_check.vysor_find_buttonhome()
                        if homebt!=None:
                            bot.click(homebt)
                            time.sleep(1)
                            bot.click(homebt)
                            time.sleep(0.5)
                            bot.click(cx(298),cy(149))
                            time.sleep(3)
                            self.reposition_max_wait = 0
                time.sleep(0.3)
            # ~ time.sleep(2)
            
            
            
    def reset_flag(self):
        self.reposition_max_wait =  0
    
app = McocQuest()        
app.mcoc_quest()
