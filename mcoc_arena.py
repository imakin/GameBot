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

    def click_last_found(self):
        bot.click(cx(self.room_check.last_found_pos[0]), cy(self.room_check.last_found_pos[1]))

    def mcoc_arena(self):
        while True:
            if (self.reposition_max_wait>0):
                self.reposition_max_wait -= 1
            
            img = room_check.get_grab()
            if False:pass

            elif self.room_check.is_fight(img):
                self.reset_flag()
                setting.printl("room: FIGHTING!")
                counter = 5
                while counter>0:
                    counter -= 1
                    bot.dragTo(cx(1850),cy(870), 0.05, button="left") #medium attack
                    # time.sleep(0.1)
                    bot.click(cx(1100),cy(862)) #block
                    # time.sleep(0.1)
                    bot.click(cx(1700),cy(868)) #light
                    bot.click(cx(1700),cy(868)) #light
                    bot.dragTo(cx(1850),cy(870), 0.05, button="left") #medium attack
                    bot.click(cx(1710),cy(868)) #light
                    bot.click(cx(1710),cy(868)) #light
                    bot.click(cx(1710),cy(868)) #light
                    # time.sleep(0.1)
                    bot.click(cx(1100),cy(862)) #block
                    # time.sleep(0.1)
                    bot.dragTo(cx(1850),cy(870), 0.05, button="left") #medium attack
                    bot.click(cx(1700),cy(868)) #light
                    bot.click(cx(1700),cy(868)) #light
                    bot.click(cx(1710),cy(868)) #light
                    bot.dragTo(cx(1850),cy(870), 0.05, button="left") #medium attack
                    bot.click(cx(1710),cy(868)) #light
                    bot.click(cx(1710),cy(868)) #light
                    # time.sleep(0.1)
                    bot.click(cx(1100),cy(1032)) #special
                img = room_check.get_grab()
                if self.room_check.is_fight_paused(img):
                    setting.printl("fight paused, mode manual!")
                    while True:
                        img = room_check.get_grab()
                        if self.room_check.is_fight_paused(img) or self.room_check.is_fight(img):
                            time.sleep(1)
                        else:
                            setting.printl("fight done. continue bot")
                            break
            
            elif self.room_check.is_fight_paused(img):
                setting.printl("fight paused, mode manual!")
                sampling = 0
                while True:
                    img = room_check.get_grab()
                    if self.room_check.is_fight_paused(img) or self.room_check.is_fight(img):
                        time.sleep(1)
                    else:
                        sampling += 1
                        if sampling>5:
                            setting.printl("fight done. continue bot")
                            break




            elif (
                self.room_check.is_arena_between_match(img)
                or self.room_check.is_arena_between_match_final(img)
                or self.room_check.is_arena_between_match_over(img)
            ):
                self.reset_flag()
                setting.printl("room: arena between match")
                self.click_last_found()
                time.sleep(1)
            
            elif self.room_check.is_arena_next_series(img):
                self.reset_flag()
                setting.printl("room: arena next series")
                self.click_last_found()
                time.sleep(0.5)
            
            elif self.room_check.is_arena_help(img):
                self.reset_flag()
                tries = 3
                while self.room_check.is_arena_help(img) or tries>0:
                    tries -= 1
                    setting.printl("room: arena help")
                    self.click_last_found()
                    time.sleep(1.5)
                    img = room_check.get_grab()

            elif (self.room_check.is_arena_set_lineup(img)):
                self.reset_flag()
                setting.printl("room: home->fight->versus->set lineup (TODO)")
                time.sleep(1)
                for x in range(5):
                    if self.room_check.is_arena_set_lineup_classpenalty(img):
                        img = room_check.get_grab()
                        setting.printl("room: home->fight->versus->set lineup class penalty")
                        x,y = self.room_check.last_found_pos
                        if y>850:
                            target_y = cy(y-7)
                        else:
                            target_y = cy(y+70)
                        bot.moveTo(cx(x-60),cy(y))
                        bot.dragTo(cx(x-60),target_y, 0.5)
                        time.sleep(0.5)
                print('wis')
                if self.room_check.is_arena_set_lineup(img):
                    self.click_last_found()
                    time.sleep(0.5)

            elif (self.room_check.is_arena_select_opponent2(img)):
                self.reset_flag()
                setting.printl("room: home->fight->versus->select opponent")
                time.sleep(1)
                cntn = self.room_check.is_continue2(img)
                if cntn:
                    setting.printl("continue button found at {}".format(cntn))
                    self.click_last_found()
                    time.sleep(0.5)
                else:
                    setting.printl("continue button not found")
            
            elif (
                self.room_check.is_find_match_ready(img) or
                self.room_check.is_find_match_free(img) or
                self.room_check.is_edit_team(img)
            ):
                self.reset_flag()
                setting.printl("room: home->fight->versus->findmatch select champ READY to find")
                time.sleep(1)
                self.click_last_found()

                
            elif (self.room_check.is_find_match(img)):
                self.reset_flag()
                setting.printl("room: home->fight->versus->findmatch select champ")
                
                setting.printl("filtering 4* manual aja, krn setting persist")
                time.sleep(0+random.random())
                
                self.click_last_found()
                time.sleep(0.5)
                img = room_check.get_grab()
                if self.room_check.is_find_match_ready(img):
                    setting.printl("room: home->fight->versus->findmatch select champ READY to find")
                    self.click_last_found()
                    time.sleep(0.5)
                    # return
                else:
                    setting.printl("adding rooster")
                    for repeat in range(3):
                        bot.moveTo(cx(1240),cy(840))
                        time.sleep(0.3)
                        bot.dragTo(cx(1088),cy(853), 0.5)
                        time.sleep(1)
                        img = room_check.get_grab()
                        if self.room_check.is_find_match_ready(img):
                            self.click_last_found()
                            time.sleep(0.5)
                        elif not self.room_check.is_find_match(img):
                            break



            elif self.room_check.is_continue2(img):
                self.reset_flag()
                setting.printl(f"continue button found. clicking")
                self.click_last_found()
                time.sleep(0.5)
            
            elif self.room_check.is_arena_popup_close(img):
                self.reset_flag()
                setting.printl("room: arena popup close")
                self.click_last_found()
                time.sleep(0.5)
            
            else:
                print("warning: window reposition manual aja. width960 posisi kanan bawah nempel, resolusi monitor 1920x1080")
                # placed = self.room_check.window_reposition()
                # setting.printl(f"window position: {placed}")
                time.sleep(0.3)
            # ~ time.sleep(2)
        

            
            
            
            
    def reset_flag(self):
        self.reposition_max_wait =  0
    
app = McocArena()        
app.mcoc_arena()
