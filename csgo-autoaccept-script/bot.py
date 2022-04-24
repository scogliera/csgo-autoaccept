import pyautogui, keyboard, win32api, win32con
import subprocess, platform
from math import floor
from time import sleep
from winsound import Beep


def clear():
	if platform.system()=="Windows":
		subprocess.Popen("cls", shell=True).communicate()
	else:
		print("\033c", end="")


def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



class Game:
	def __init__(self):
		self.gameResolution = self.displayResolution = pyautogui.size()
		self.csgoLogo = 'assets/images/csgo.png'
		self.fullscreen = False
		self.findCSGO()

		if self.found:
			self.findResolution()


	def findCSGO(self):
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

		#Looping through each possible taskbar location
		for taskbarPosition, cursorPosition in taskbars:
			try:
				#Placing the cursor on the part of the screen where taskbar should be to show it (if hidden)
				win32api.SetCursorPos(cursorPosition)
				sleep(0.25)

				#Looking for the csgo icon on the taskbar
				click(pyautogui.locateOnScreen(self.csgoLogo, region=taskbarPosition, grayscale=True, confidence=0.8).left, pyautogui.locateOnScreen(self.csgoLogo, region=taskbarPosition, grayscale=True, confidence=0.8).top)
				self.taskbarLocation = (taskbarPosition, cursorPosition)
				self.found = True
				return True

			except AttributeError:
				continue
		 
		self.found = False
		return False
	

	def findResolution(self):
		#After opening up cs, checking resolution every 500ms to find out if cs runs on a custom resolution or native 
		for i in range(10):
			#Checks if the resolution on Desktop matches current resolution (If CS:GO changed monitor resolution)
			if self.displayResolution != pyautogui.size():
				self.gameResolution = pyautogui.size()
				self.fullscreen = True
				Beep(1000, 500)
				Beep(1000, 500)
				print(f"CS:GO Resolution Found! {self.gameResolution.width}x{self.gameResolution.height}")
				break

			#If it didn't detect a resolution change, use the Desktop resolution
			if i == 9:
				self.gameResolution = pyautogui.size()
				Beep(500, 500)
				print(f"The monitor didn't change resolution, either CS:GO is in Windowed or resolution is: {self.gameResolution.width}x{self.gameResolution.height}")
				break
			sleep(0.5)



class Matchmaking(Game):
	def __init__(self):
		Game.__init__(self)
		self.matchmakingAcceptButton = 'assets/images/accept.png'
		self.acceptButtonRegion = (floor((self.gameResolution.width/2)/2), 0, floor(self.gameResolution.width/2), self.gameResolution.height)


	def matchmakingAccept(self):
		print(" > Searching for Accept Button...\n > Hold Left Arrow to stop searching\n\n")

		while(True):
			if keyboard.is_pressed('right') or keyboard.is_pressed('left'):
				print("[Off] AutoAccept")
				Beep(400, 400)
				return False

			if self.fullscreen:
				buttonPosition = pyautogui.locateCenterOnScreen(self.matchmakingAcceptButton, region=self.acceptButtonRegion, grayscale=True, confidence=0.7)
			else:
				buttonPosition = pyautogui.locateCenterOnScreen(self.matchmakingAcceptButton, grayscale=True, confidence=0.7)

			if(buttonPosition != None):
				click(buttonPosition.x, buttonPosition.y)
				print("\nMatch found, [OFF] AutoAccept\nDisabled Keybinds")
				return True
			
			sleep(1)



class Faceit(Game):
	def __init__(self):
		Game.__init__(self)



def main():
	#clear()
	print("What are you playing today?\n\n[M]atchmaking\n[F]aceit")
	event = keyboard.read_event()

	if event.event_type == keyboard.KEY_DOWN and event.name.lower() == 'm':
		game = Matchmaking()
	elif event.event_type == keyboard.KEY_DOWN and event.name.lower() == 'f':
		print("\n\n--- FACEIT IN DEVELOPMENT ---\nMaybe next update? Sorry! :(")
		return
		game = Faceit()
	else:
		return


	if game.found:
		enableKeybinds = True

		clear()
		print("\nBinds\n")
		print(" > Up Arrow | Enables/Disables Keybinds Below")
		print(" > Left Arrow | AutoAccept\n\n")
		print(" > Right Arrow | Quit")
		print("  Logs  \n---------")

		while(True):
			event = keyboard.read_event()
			'''
				Binds:
					Up Arrow - Enables/Disables Keybinds
					Left Arrow - Enables/Disables Autoaccept
					Right Arrow - Stops the script
			'''
			
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
					#If game found, disable keybinds
					if game.matchmakingAccept():
						enableKeybinds = False
	else:
		print("Couldn't find CS:GO! Make sure the game is running!")
		print("Closing script in 5 seconds...")
		sleep(5)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\nStopping Script")
		exit()