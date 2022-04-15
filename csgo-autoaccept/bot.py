from tkinter.messagebox import YESNOCANCEL
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math
import winsound


def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def findCSGO():
	win32api.SetCursorPos((math.floor(pyautogui.size().width/2),pyautogui.size().height)) #Place cursor on the bottom part of screen to show taskbar if it auto hides
	time.sleep(0.5) #Waits for the taskbar animation
	try:
		#Tries finding the csgo logo and clicks on it
		regionLeft = 0
		regionTop = math.floor((pyautogui.size().height)-(pyautogui.size().height/5))
		regionWidth = pyautogui.size().width
		regionHeight = math.floor(pyautogui.size().height/5)

		click(pyautogui.locateOnScreen('images/csgo.png', region=(regionLeft, regionTop, regionWidth, regionHeight), grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('images/csgo.png', region=(regionLeft, regionTop, regionWidth, regionHeight), grayscale=True, confidence=0.8).top)
		return True
	except:
		return False	


def main():
	found = findCSGO() #continues if csgo logo was clicked
	if found:
		time.sleep(5)
		winsound.Beep(1000, 200)
		winsound.Beep(1000, 200)
		accept = False

		regionLeft = math.floor((pyautogui.size().width/2)/2)
		regionTop = 0
		regionWidth = math.floor(pyautogui.size().width/2)
		regionHeight = pyautogui.size().height
		centerRegion = (regionLeft, regionTop, regionWidth, regionHeight)
		print("\nBinds\n > Q | Quit")
		print(" > U | AutoAccept\n\n")
		print("  Logs  \n---------")

		while(True):
			if keyboard.is_pressed('q'):
				return
			
			if keyboard.is_pressed('o'):
				print("Screenshotted")
				pyautogui.screenshot('scrn.png', region=centerRegion)

			if keyboard.is_pressed('u'):
				if accept:
					winsound.Beep(400, 400)
					accept = False
					print("[OFF] AutoAccept")
					time.sleep(1)

				else:
					winsound.Beep(800, 400)
					accept = True
					print("[ON] AutoAccept")
					time.sleep(1)
			
			if accept:
				if(pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8) != None):
					click(pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8).top)
					accept = False
					print("\nMatch found, [OFF] AutoAccept")


if __name__ == '__main__':
	main()