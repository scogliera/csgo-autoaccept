from tkinter.messagebox import YESNOCANCEL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X: 1128 Y: 1062 RGB: (210, 139,  49)
#X: 958 Y: 476 RGB: (90, 203, 94)

hotbar_x_area = (500, 1500)
area = (400, 800)

def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def findCSGO():
	for x in range(hotbar_x_area[0], hotbar_x_area[1], 15):
		win32api.SetCursorPos((x,1062))
		if pyautogui.pixel(x, 1062)[0] > 160 and pyautogui.pixel(x, 1062)[1] > 100 and pyautogui.pixel(x, 1062)[2] < 100:
			click(x, 1062)
			return True

def main():
	found = findCSGO()
	if found:
		while(True):
			for y in range(area[0], area[1], 25):
				for x in range(hotbar_x_area[0], hotbar_x_area[1], 50):
					win32api.SetCursorPos((x,y))

					if keyboard.is_pressed('q'):
						return
					
					if pyautogui.pixel(x, y)[0] < 40 and pyautogui.pixel(x, y)[1] > 80 and pyautogui.pixel(x, y)[2] < 100:
						click(x, y)
						return
	
main()