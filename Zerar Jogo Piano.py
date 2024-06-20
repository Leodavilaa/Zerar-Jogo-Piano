import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1528,471, duration=1)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep (0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1399,409,(0,0,0)):
        click(1399,409)
    if pyautogui.pixelMatchesColor(1479,403,(0,0,0)):
        click(1479,403)
    if pyautogui.pixelMatchesColor(1551,401,(0,0,0)):
        click(1551,401)
    if pyautogui.pixelMatchesColor(1626,401,(0,0,0)):
        click(1626,401)

