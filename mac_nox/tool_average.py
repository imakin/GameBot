import room_check
import pyautogui
rc = room_check.RoomCheck()

def avg():
  print("x0 y0")
  input()
  pos = pyautogui.position()
  x0,y0 = pos.x, pos.y
  print("x1 y1")
  input()
  pos = pyautogui.position()
  x1,y1 = pos.x, pos.y
  print(x0,y0,x1,y1)
  print(rc.color_average_area( (x0,y0,x1,y1), [30,35,35] ) )

avg()
