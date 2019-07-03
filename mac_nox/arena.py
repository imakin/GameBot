import time
import random
import json
import sys

import pyautogui

import room_check
import setting
import bot
from setting import cx,cy


def save_map(obj ):
    with open('mapquest.txt', 'w') as f:
        f.write(json.dumps(obj))
def load_obj(name ):
    with open('mapquest.map', 'r') as f:
        return json.loads(f.read())
        return pickle.load(f)

log_last_saving = -60
logs = ""

def printlog(x):
    global logs
    global log_last_saving
    
    print("{} {}".format(time.strftime("%H:%M"), x))
    print("{} {}".format(time.strftime("%H:%M"), x), file=sys.stderr)
    logs += "{} {}".format(time.strftime("%H:%M"), x)
    logs = logs[-1000:]
    if (time.time()-log_last_saving)>60:
        try:
            with open("log", "w") as f:
                f.write(logs)
        except Exception as e:
            print(e)
        log_last_saving = time.time()

class McocQuest(object):
    def __init__(self, room_check_object=None):
        self.room_check = room_check_object or room_check.RoomCheck()
        self.solution_unsolved = {}
    
    def mcoc_quest(self):
        room = self.room_check
        while True:
            img = room.get_grab(region=(445*2,87*2,470*2,109*2))
            
            while room.quest_isin_fight_focus(img):
                printlog("fight")
                # ~ self.last_fight_scrot = img
                for x in range(0, 30):
                    bot.click(747, 486, 5)
                    if (x%10==0):
                        bot.moveTo(670,480)
                        time.sleep(0.05)
                        bot.dragTo(840,486,0.05)
                        time.sleep(0.05)
                    if (x%4==0):
                        bot.click(180, 602, 10)
                img = room.get_grab(region=(445*2,87*2,470*2,109*2))
                # ~ printlog(time.time()-room.last_room_time)
                if (time.time()-room.last_room_time>300):
                    printlog("reset Nox")
                    bot.click(15,42)
                    time.sleep(0.5)
                    bot.click(15,42)
                    time.sleep(3)
                    bot.click(360,370)
                    time.sleep(10)
                    bot.click(81,1120)
                    pyautogui.doubleClick(81,1120)
                    # ~ time.sleep(0.1)
                    # ~ time.sleep(0.1)
                    # ~ bot.click(81,1120)
                    time.sleep(5)
                    bot.click(868,293)
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','option','command','1')
                    room.last_room_time = time.time()
                    img = room.get_grab()
                    break
                    
            
            img = room.get_grab()

            if room.quest_isin_postfight(img):
                printlog("post fight")
                bot.click(180, 602, 10)
                bot.click(727, 613, 10)
                time.sleep(1)
            
            elif room.is_champion_info(img):
                printlog("chamption info")
                bot.click(room.last_coord)
                time.sleep(2)
                
            elif room.arena_rearrangeteam(img):
                print("rearrange team")
                
                self.wait_until_true_or_timeout(room.is_continuebutton,10)
                
                img = room.get_grab()
                
                skill = [187,21,21]
                cosmic = [4,135,172]
                science = [72,144,25]
                tech = [11,72,161]
                mystic = [145,34,154]
                mutant = [160,128,27]
                
                class_pool = {
                    "skill":skill,
                    "cosmic":cosmic,
                    "science":science,
                    "tech":tech,
                    "mystic":mystic,
                    "mutant":mutant
                }
                
                champ = [0]*6
                # index 0~2 ours, 3~5 enemy
                img = room.get_grab(rescale=False)
                champ[0] = room.color_average_area( (590,606    ,590+40,606+40    ), [30,35,35], img)
                champ[1] = room.color_average_area( (590,606+160,590+40,606+40+160), [30,35,35], img )
                champ[2] = room.color_average_area( (590,606+320,590+40,606+40+320), [30,35,35], img )
                
                champ[3] = room.color_average_area( (590+654,606+26    ,590+654+40,606+26+40    ), [30,35,35], img )
                champ[4] = room.color_average_area( (590+654,606+26+160,590+654+40,606+26+40+160), [30,35,35], img )
                champ[5] = room.color_average_area( (590+654,606+26+320,590+654+40,606+26+40+320), [30,35,35], img )
                
                champ_class = []
                for c in champ:
                    found_class = False
                    for key in class_pool:
                        if room.is_color_similar(c, class_pool[key], 15):
                            print(key)
                            champ_class.append(key)
                            found_class = True
                            break
                    if not found_class:
                        print("unknown: {}".format(c))
                        champ_class.append("unknown{}".format(c))
                # sort each
                team_class = champ_class[:3]
                enemy_class = champ_class[3:]
                team_class.sort()
                enemy_class.sort()
                # join as code
                rearrange_code = " ".join(team_class + enemy_class)
                
                try:
                    solution = setting.class_selection_pool[rearrange_code]
                    printlog("solution: {}".format(solution))
                    enemy_class_unsorted = champ_class[3:]
                    team_class_unsorted = champ_class[:3]
                    
                    for key in solution:
                        target_enemy = solution[key]
                        team_pos = team_class_unsorted.index(key)
                        if team_pos<0:
                            break
                        for enemy_pos in range(0,3):
                            if enemy_class_unsorted[enemy_pos]==target_enemy:
                                printlog("{} vs {}".format( team_class_unsorted[team_pos], target_enemy))
                                printlog("drag {} to {}".format(team_pos, enemy_pos))
                                
                                if team_pos!=enemy_pos:
                                    time.sleep(1)
                                    bot.moveTo(282,285+80*team_pos)
                                    bot.dragTo(282,285+80*enemy_pos,drag_time=1.5)
                                    time.sleep(1)
                                #team class position has been modified
                                # ~ temp = team_class_unsorted[team_pos]
                                team_class_unsorted[team_pos] = team_class_unsorted[enemy_pos]
                                team_class_unsorted[enemy_pos] = "occupied"
                                
                                enemy_class_unsorted[enemy_pos] = "occupied"
                                break
                    
                    
                except KeyError:
                    printlog("solution for {} is not exists".format(rearrange_code))
                    self.solution_unsolved[rearrange_code] = 0
                    with open("solution_unsolved.txt", "a+") as f:
                        f.write("{}\n".format(self.solution_unsolved))
                    # check 1
                    m = setting.coord_multiplier
                    for i in range(0,3):
                        time.sleep(0.5)
                        ok = True
                        if room.is_color_dominant( img.getpixel( (int(m*756/2),int(m*(764-162)/2)) ), "r" ):
                            print("1 is red")
                            bot.moveTo(282,285+80*0)
                            bot.dragTo(282,285+80*1)
                            time.sleep(0.5)
                            ok = False
                        img = room.get_grab()
                        if room.is_color_dominant( img.getpixel( (int(m*756/2),int(m*(764)/2)) ), "r" ):
                            print("2 is red")
                            bot.moveTo(282,285+80*1)
                            bot.dragTo(282,285+80*2)
                            time.sleep(0.5)
                            ok = False
                        img = room.get_grab()
                        if room.is_color_dominant( img.getpixel( (int(m*756/2),int(m*(764+162)/2)) ), "r" ):
                            print("3 is red")
                            bot.moveTo(282,285+80*2)
                            bot.dragTo(282,285+80*0)
                            ok = False
                        if ok:
                            break
                
                print("OK")
                bot.click(768,613)
                
            
            elif room.arena_2nd(img):
                printlog("arena select, found")
                # bot.click(442,592)
                bot.click(833,592)


                #3rd
                # bot.moveTo(833,300)
                # time.sleep(1)
                # bot.dragTo(100,300)
                # time.sleep(1)
                # bot.click(440,577)

            
            elif room.arena_champselect_helpneeded(img):
                printlog("need help")
                while (room.arena_champselect_helpneeded()):
                    printlog("help needed")
                    bot.click(291,280,1)
                    time.sleep(2)
                
            elif room.arena_champselect(img):
                printlog("arena champ select")
                # ~ if room.arena_champselect_multiplier1():                    
                # ~ printlog("manual belum x3")
                # ~ x = input()
                # ~ if x=="":
                    # ~ printlog("manually")
                    # ~ continue
                if room.arena_champselect_notmultiplier3(img):
                    print("not multiplier 3")
                    bot.click(801,596)#filter menu
                    time.sleep(1)
                    bot.click(801,596)#filter menu
                    time.sleep(1)
                    bot.click(679,165) #reset
                    time.sleep(1)
                    bot.click(679,165)#reset
                    time.sleep(1)
                    bot.click(801,620) #filter tab
                    time.sleep(1)
                    bot.dragTo(800,120) #drag
                    time.sleep(1)
                    # bot.click(727,443)#2*
                    bot.click(727,483)#3*
                    bot.click(727,523)#4*
                    time.sleep(1)
                    for x in range(0,2): #drag time
                        bot.moveTo(430,600)
                        time.sleep(0.2)
                        bot.dragTo(430,80,drag_time=0.2)
                        time.sleep(0.2)
                else:
                    printlog("possibly multiplier 3")
                start = time.time()
                while room.arena_champselect(img) and room.arena_champselect_champempty(img) and (time.time()-start)<30:
                    bot.moveTo(363,357)
                    bot.dragTo(207,344)
                    time.sleep(1)
                    img = room.get_grab()
                start = time.time()
                while room.arena_champselect(img) and not(room.arena_champselect_champempty(img)) and (time.time()-start)<30:
                    bot.click(159,618)
                    time.sleep(0.5)
                    img = room.get_grab()
                    
                    
            elif room.arena_enemyselect(img):
                printlog("enemy select")
                time.sleep(2)
                if room.is_color_dominant(img.getpixel((512*2,488*2)), "g"):
                    bot.click(512,488)
                elif room.is_color_dominant(img.getpixel((519*2,341*2)), "g"):
                    bot.click(519,341)
                time.sleep(2)
                bot.click(758,616)
                
                
            elif room.is_continuebutton(img):
                printlog("continue button shows up")
                if (room.arena_rearrangeteam()):
                    printlog("but in rearrange team")
                    continue
                bot.click(room.last_coord)
                time.sleep(0.5)
                bot.click(792,630)
                time.sleep(2)
            
            elif room.arena_betweenfight(img):
                printlog("continue button between fight")
                # bot.click(room.last_coord)
                # time.sleep(0.5)
                bot.click(576,430) #KO
                time.sleep(0.5)
                bot.click(576,540) #victory
                time.sleep(0.5)
                bot.click(792,630)
                time.sleep(2)
            
            
            elif room.is_popup(img):
                printlog("popup")
                # ~ bot.click(room.last_coord)
                # ~ time.sleep(1)
                bot.click(822,85)
            
            elif room.is_reconnect(img):
                printlog("reconnect")
                time.sleep(3)
                if room.is_reconnect():
                    print("wait 30 min then reconnect")
                    time.sleep(60*30)
                    bot.click(room.last_coord)
            
            elif room.mcoc_fightrecovered(img):
                printlog("fight recovered")
                bot.click(room.last_coord)
            
            
            elif room.mcoc_fightbutton(img):
                printlog("fight button shown")
                bot.click(room.last_coord)
                while room.mcoc_fightbutton():
                    bot.click(room.last_coord)
                    time.sleep(1)
                bot.moveTo(71,352)
                bot.dragTo(1800,360)
                time.sleep(3)
                
            
            elif room.mcoc_fightroom_arenashown(img):
                printlog("versus arena shown")
                bot.click(room.last_coord)
            
            elif room.mcoc_fightroom(img):
                printlog("home -> fight")
                bot.moveTo(71,352)
                bot.dragTo(1800,360)
                time.sleep(3)
            
            elif room.android_home(img):
                printlog("android in home")
                bot.click(room.last_coord)
            
            elif room.last_room!=None:
                room.last_room = None
                room.last_room_time = time.time()
            else:
                printlog("failed for {}".format(time.time() - room.last_room_time))
                if (time.time()-room.last_room_time)>500:
                    printlog("reset Nox")
                    bot.click(15,42)
                    time.sleep(0.5)
                    bot.click(15,42)
                    time.sleep(3)
                    bot.click(360,370)
                    time.sleep(10)
                    bot.click(81,1120)
                    pyautogui.doubleClick(81,1120)
                    # ~ time.sleep(0.1)
                    # ~ time.sleep(0.1)
                    # ~ bot.click(81,1120)
                    time.sleep(5)
                    bot.click(868,293)
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','option','command','1')
                    room.last_room_time = time.time()
    
    def wait_until_true_or_timeout(self, method, timeout=30):
        s = time.time()
        while (time.time()-s)<timeout:
            x = method()
            print(x)
            if x:
                break
            time.sleep(0.5)
        
    def reset_nox(self):
        printlog("reset Nox")
        bot.click(15,42)
        time.sleep(0.5)
        bot.click(15,42)
        time.sleep(3)
        bot.click(360,370)
        time.sleep(10)
        bot.click(81,1120)
        pyautogui.doubleClick(81,1120)
        # ~ time.sleep(0.1)
        # ~ time.sleep(0.1)
        # ~ bot.click(81,1120)
        time.sleep(5)
        bot.click(868,293)
        time.sleep(1)
        pyautogui.hotkey('ctrl','option','command','1')
        room.last_room_time = time.time()  
              
app = McocQuest()
app.mcoc_quest()
