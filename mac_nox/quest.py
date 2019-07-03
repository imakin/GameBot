import time
import random
import json

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

class McocQuest(object):
    def __init__(self, room_check_object=None):
        self.room_check = room_check_object or room_check.RoomCheck()
        self.map = {}
        self.map_current_pos = "start"
        self.map_antiduplicate_lastcoord = None
        self.map_antiduplicate_lastcoord_picked = None
        self.redo_limit = 0
    
    def mcoc_quest(self):
        room = self.room_check
        while True:
            
            img = room.get_grab(region=(0,0,470*2,109*2))
            while room.quest_isin_fight(img):
                print("fight")
                # ~ self.last_fight_scrot = img
                for x in range(0, 30):
                    bot.doubleClick(747, 486, 5)
                    if (x%2==0):
                        bot.moveTo(600,480)
                        bot.dragTo(780,486,0.2)
                    if (x%3==0):
                        bot.click(180, 602, 10)
                img = room.get_grab(region=(0,0,470*2,109*2))

            img = room.get_grab()
            if room.quest_isin_postfight(img):
                print("post fight")
                bot.click(180, 602, 10)
                time.sleep(1)
            
            
            elif room.quest_portal(img):
                print("portal")
                # only 1 option, or already selected: teleport button is clickable
                if room.is_color_similar(
                    img.getpixel((664*2,431*2)),
                    [45,128,0],
                    10
                ):
                    bot.click(710,358)
                    time.sleep(1)
                    bot.click(664,431)
                elif room.quest_portal_is_ready(img):
                    print("teleport ready")
                    bot.click(room.last_coord)

                elif room.quest_portal_get_options_count(img)==2:
                    print("2 options")
                    self.quest_next_node_select(
                        [
                            [700, 380+60*0],
                            [700, 380+60*1],
                        ]
                    )

            
            elif room.quest_isin_quest(img):
                print("is in quest")
                coord_next_node = room.quest_get_nextnode(img)
                tries = 0
                while not(coord_next_node) and tries<3:
                    coord_next_node = room.quest_get_nextnode()
                    tries += 1
                
                if not coord_next_node:
                    continue
                
                #make sure target is clickable node
                i = 0
                while i<len(coord_next_node):
                    print(coord_next_node)
                    c = coord_next_node[i]
                    
                    x0 = 2*(c[0]-5)
                    y0 = 2*(c[1]-5)
                    x1 = 2*(c[0]+5)
                    y1 = 2*(c[1]+5)
                    comparator = [] #if comparator is the same 
                    max_score = 3
                    score = max_score
                    for x in range(0,max_score):
                        node = room.get_grab(region=(x0,y0,x1,y0))
                        p = node.getpixel((3,3))
                        if p==comparator:
                            score -= 1
                        else:
                            break
                        comparator = p
                        # ~ print(c, node.getpixel((5,5)), sep="    :    ")
                    if score<1:
                        print("invalid ",c)
                        coord_next_node.pop(i)
                    else:
                        i += 1
                self.quest_next_node_select(coord_next_node)
                    
            
            
            elif room.quest_isin_prefight(img):
                print("quest prefight")
                bot.click(727,612)
            
            elif room.quest_complete(img):
                print("quest dialog")
                bot.click(room.last_coord)

            elif room.quest_isin_questdialog(img):
                print("quest dialog")
                print("isin quest or popup? ")
                inquest = room.quest_isin_quest()
                print(inquest)
                if inquest:
                    continue
                if room.is_popup():
                    bot.click(room.last_coord)
                    continue
                bot.click(433,624)
                time.sleep(2)
            elif room.is_popup(img):
                print("popup")
                bot.click(room.last_coord)
            
            elif room.quest_playnextbutton(img):
                print("next button click in 5s")
                time.sleep(5)
                bot.click(room.last_coord)
            
    def quest_next_node_select(self, coord_next_node):

        if len(coord_next_node)>1:
            if (
                type(self.map_antiduplicate_lastcoord)==list and
                abs(coord_next_node[0][0]-self.map_antiduplicate_lastcoord[0][0])<20 and
                abs(coord_next_node[0][1]-self.map_antiduplicate_lastcoord[0][1])<20 and
                abs(coord_next_node[1][0]-self.map_antiduplicate_lastcoord[1][0])<20 and
                abs(coord_next_node[1][1]-self.map_antiduplicate_lastcoord[1][1])<20
            ):
                self.redo_limit += 1
                if self.redo_limit>5:
                    print("too many redo, pick other")
                    if self.map_antiduplicate_lastcoord_picked!=0:
                        self.map_antiduplicate_lastcoord_picked = 0
                    else:
                        self.map_antiduplicate_lastcoord_picked = 1
                print("redo pick: auto")
                pick = self.map_antiduplicate_lastcoord_picked
                print(pick)
                bot.click(coord_next_node[pick][0],coord_next_node[pick][1])
                time.sleep(0.5)
                bot.click(coord_next_node[pick][0],coord_next_node[pick][1])
                return False

            self.redo_limit = 0
            self.map[self.map_current_pos] = {}
            i = 0
            for coord in coord_next_node:
                new_pos_key = self.map_current_pos+":"+str(i)
                self.map[new_pos_key] = coord
                self.map[self.map_current_pos][i] = new_pos_key
                
                print(i, ":",coord)
                bot.moveTo(coord[0], coord[1])
                time.sleep(2)
                i += 1
            save_map(self.map)
            print("which one to pick?")
            pick = input()
            try:
                pick = int(pick)
            except:
                print("invalid input, pick 0")
                pick = 0
            
            self.map_current_pos = self.map[self.map_current_pos][pick]
            self.map["map_current_pos"] = self.map_current_pos
            save_map(self.map)
            print(self.map)
            self.map_antiduplicate_lastcoord = coord_next_node
            self.map_antiduplicate_lastcoord_picked = pick
            
            bot.click(coord_next_node[pick][0],coord_next_node[pick][1])
            time.sleep(0.5)
            bot.click(coord_next_node[pick][0],coord_next_node[pick][1])
            
        else:
            try:
                bot.click(coord_next_node[0][0], coord_next_node[0][1])
            except:
                pass

app = McocQuest()
app.mcoc_quest()
