from tkinter.messagebox import YESNOCANCEL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X: 1128 Y: 1062 RGB: (210, 139,  49)
#X: 958 Y: 476 RGB: (90, 203, 94)

def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def findCSGO():
	win32api.SetCursorPos((960,1080))
	time.sleep(0.5)
	try:
		click(pyautogui.locateOnScreen('csgo.png').left, pyautogui.locateOnScreen('csgo.png').top)
		return True
	except:
		return False

def main():
	found = findCSGO()
	if found:
		while(True):
			if keyboard.is_pressed('q'):
				return
			
			if(pyautogui.locateOnScreen('accept.png') != None):
				click(pyautogui.locateOnScreen('accept.png').left, pyautogui.locateOnScreen('accept.png').top)
				return

			print(pyautogui.locateOnScreen('accept.png'))
	
main()