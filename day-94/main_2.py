""" Import required tools"""
import pyautogui
from PIL import ImageGrab
import time
"""In the beginning you have to take a SS and get hold of your screen with game. Then you have to take cor when the action must take place""" 

bbox = (319, 677, 407, 733)

# 
duck_bbox = (273, 611, 323, 676)
data = ImageGrab.grab(bbox)
data.save('duck.png')
print(data.getcolors())

data2 = ImageGrab.grab(duck_bbox)
data.save('duck.png')
print(data.getcolors())
#

duck_colors = [(3250, (255, 255, 255))]
colors = [(4928, (255, 255, 255))]
"""When you have your colors than you just have to create some functions to make your dino to jump or tu crouch"""

def jump():
    pyautogui.keyDown('space')
    print('Jump')
    time.sleep(0.01)
    pyautogui.keyUp('space')

def duck():
    pyautogui.keyDown('down')
    print('duck')
    time.sleep(0.01)
    pyautogui.keyUp('down')


time.sleep(4)
while True:
    data = ImageGrab.grab(bbox=bbox)
    duck_data = ImageGrab.grab(bbox=duck_bbox)
    if data.getcolors() != colors:
        jump()
    if duck_data.getcolors() != duck_colors:
        duck()