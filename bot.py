from tkinter.messagebox import YESNOCANCEL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math

#X: 1128 Y: 1062 RGB: (210, 139,  49)
#X: 958 Y: 476 RGB: (90, 203, 94)

def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def openCSGO():
	pass


def findCSGO():
	win32api.SetCursorPos((math.floor(pyautogui.size().width/2),pyautogui.size().height)) #Place cursor on the bottom part of screen to show taskbar if it auto hides
	time.sleep(0.5) #Waits for the taskbar animation
	try:
		#Tries finding the csgo logo and clicks on it
		regionLeft = 0
		regionTop = math.floor((pyautogui.size().height)-(pyautogui.size().height/5))
		regionWidth = pyautogui.size().width
		regionHeight = math.floor(pyautogui.size().height/5)

		click(pyautogui.locateOnScreen('pictures/csgo.png', region=(regionLeft, regionTop, regionWidth, regionHeight), grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('pictures/csgo.png', region=(regionLeft, regionTop, regionWidth, regionHeight), grayscale=True, confidence=0.8).top)
		return True
	except:
		return False

def clickAccept(centerRegion):
	click(pyautogui.locateOnScreen('pictures/accept.png', region=centerRegion, grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('pictures/accept.png', region=centerRegion, grayscale=True, confidence=0.8).top)
	return

def main():
	found = findCSGO() #continues if csgo logo was clicked
	if found:
		xPosCenter = math.floor(pyautogui.size().width/3)
		yPosCenter = math.floor(pyautogui.size().height/3)
		centerRegion = (xPosCenter, yPosCenter, xPosCenter, yPosCenter)

		while(True):
			if keyboard.is_pressed('q'):
				return
			
			if(pyautogui.locateOnScreen('pictures/accept.png', region=centerRegion, grayscale=True, confidence=0.8) != None):
				clickAccept(centerRegion)
			
			
main()