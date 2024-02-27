import pyautogui
import keyboard
import random
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def autoClick(x,y,delay):
    while keyboard.is_pressed('q') == False:
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def textOut(text):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
