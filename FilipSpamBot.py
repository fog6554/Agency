import os 
from pynput.keyboard import Key, Controller
import pyautogui
import time
import keyboard
time.sleep(5)

for i in range(100):
    keyboard.write('s')
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    
    #pyautogui.press("down")
    #pyautogui.press("down")

    
    #pyautogui.press("enter")
 
    with pyautogui.hold('shift'):
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        
    
