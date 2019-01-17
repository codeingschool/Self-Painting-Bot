import pyautogui, time
time.sleep(5) # 1
pyautogui.click() #2   # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) #3   # move right
    distance = distance - 5 #4
    pyautogui.dragRel(0, distance, duration=0.2) #5   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2) #6     # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)   # move up
