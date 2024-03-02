""" Import required tools"""
import pyautogui
from PIL import ImageGrab
import time
"""In the beginning you have to take a SS and get hold of your screen with game. Then you have to take cor when the action must take place""" 

bbox = (319, 677, 407, 733)
duck_bbox = (273, 611, 323, 676)

# bbox = (1672, 631, 1674, 722)
# duck_bbox = (1664, 575, 1666, 617)

data = ImageGrab.grab(bbox)
data.save('tree.png')
print(data.getcolors())

data2 = ImageGrab.grab(duck_bbox)
data2.save('duck.png')
print(data2.getcolors())
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
        print(f'Data_colors: {data.getcolors()}')
        print(f'Colors: {colors}')
        # time.sleep(4.4) 
        jump()
    if duck_data.getcolors() != duck_colors:
        print(f'Data_colors: {duck_data.getcolors()}')
        print(f'Duck Colors: {duck_colors}')
        # time.sleep(4.4)
        jump() 