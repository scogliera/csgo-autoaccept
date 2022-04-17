import pyautogui, keyboard, win32api, win32con
from math import floor
from time import sleep
from winsound import Beep
import concurrent.futures


def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def findCSGO():
	#Defining taskbar locations
	bottomTaskbar = (0, floor((pyautogui.size().height)-(pyautogui.size().height/5)), pyautogui.size().width, floor(pyautogui.size().height/5))
	leftTaskbar = (0, 0, floor(pyautogui.size().width/5), pyautogui.size().height)
	topTaskbar = (0, 0, pyautogui.size().width, floor(pyautogui.size().height/5))
	rightTaskbar = (floor((pyautogui.size().width)-(pyautogui.size().width/5)), 0, floor(pyautogui.size().width/5), pyautogui.size().height)
	#Adding all taskbar locations to a tuple, and adding a xy coordinate to them
	taskbars = ((bottomTaskbar, (floor(pyautogui.size().width/2), pyautogui.size().height-1)), 
				(leftTaskbar, (1, floor(pyautogui.size().height/2))), 
				(topTaskbar, (floor(pyautogui.size().width/2), 1)), 
				(rightTaskbar, (pyautogui.size().width-1, floor(pyautogui.size().height/2))))

	for taskbar, xy in taskbars:
		try:
			#Placing the cursor on the part of the screen where taskbar should be to show it (if hidden)
			win32api.SetCursorPos(xy)
			sleep(0.25)
			#Looking for the csgo icon on the taskbar
			click(pyautogui.locateOnScreen('images/csgo.png', region=taskbar, grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('images/csgo.png', region=taskbar, grayscale=True, confidence=0.8).top)
			return True
		except:
			continue
	
	print("Couldn't find CS:GO! Make sure the game is running!")
	return False


def acceptGame(fullscreen, centerRegion):
	print(" > Searching for Accept Button...\n > Hold Left Arrow to stop searching\n\n")
	while(True):
		if keyboard.is_pressed('right') or keyboard.is_pressed('left'):
			print("[Off] AutoAccept")
			Beep(400, 400)
			return False

		if fullscreen:
			if(pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8) != None):
				click(pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('images/accept.png', region=centerRegion, grayscale=True, confidence=0.8).top)
				print("\nMatch found, [OFF] AutoAccept\nDisabled Keybinds")
				return True
				
		else:
			if(pyautogui.locateOnScreen('images/accept.png', grayscale=True, confidence=0.8) != None):
				click(pyautogui.locateOnScreen('images/accept.png', grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen('images/accept.png', grayscale=True, confidence=0.8).top)
				print("\nMatch found, [OFF] AutoAccept\nDisabled Keybinds")
				return True
		sleep(1)
		

def main():
	if findCSGO():
		#Setting up variables to find out if user uses Exclusive Fullscreen or Windowed
		resolution = pyautogui.size()
		fullscreen = False
	
		#Setting up settings bools and areas for searching up images
		enableKeybinds = True
		centerRegion = (floor((resolution.width/2)/2), 0, floor(resolution.width/2), resolution.height)

		#After opening up cs, checking resolution every 500ms to find out if cs runs on a custom resolution or native 
		for i in range(10):
			if resolution != pyautogui.size():
				resolution = pyautogui.size()
				fullscreen = True
				Beep(1000, 500)
				Beep(1000, 500)
				print(f"Fullscreen Resolution Found! {resolution.width}x{resolution.height}")
				break

			if i == 9 and resolution == pyautogui.size():
				print(f"Didn't find Fullscreen Resolution, using default {pyautogui.size().width}x{pyautogui.size().height}")
				Beep(500, 500)
			sleep(0.5)

		print("\nBinds\n")
		print(" > Up Arrow | Enables/Disables Keybinds Below")
		print(" > Right Arrow | Quit")
		print(" > Left Arrow | AutoAccept\n\n")
		print("  Logs  \n---------")

		while(True):
			event = keyboard.read_event()
			if event.event_type == keyboard.KEY_DOWN and event.name == 'up':
				if enableKeybinds:
					enableKeybinds = False
					print("Disabled Keybinds")
				else:
					enableKeybinds = True
					print("Enabled Keybinds")
					
			if enableKeybinds:
				if event.event_type == keyboard.KEY_DOWN and event.name == 'right':
					return

				elif event.event_type == keyboard.KEY_DOWN and event.name == 'left':
					print("[On] AutoAccept")
					Beep(800, 400)
					if acceptGame(fullscreen, centerRegion):
						enableKeybinds = False

							

if __name__ == '__main__':
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.submit(main)

#pyautogui.screenshot('scrn.png', region=centerRegion)