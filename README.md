<div align="center">
	<h1>
		<br>
		<a href="https://github.com/scogliera/csgo-autoaccept/">
			<img src="images/github/banner.png" alt="csgo-autoaccept">
		</a>
		</br>
  <div>
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/scogliera/csgo-autoaccept">
  </div>
	</h1>
	<h4>A simple script that looks for the Accept button and clicks on it when found</h4>
<br><br><br>
</div>

## Notes
* **You must have CS:GO running before starting the script**
* If you're using the **Python Script instead of the Application**, you must have **Python 3 installed**
<br><br><br>

## Usage
- After opening up the script, **wait for it to open up CS:GO in the taskbar**
- When it opens up CS:GO, it will get your resolution and beep twice once successful (Takes about 5 seconds). **DO NOT minimize CS before you hear the beeps**
- At this point, everything is set up and ready for use
- See the console window for binds
<p align="center">
  <img src="images/usage.png" alt="Console Menu"/>
  <br><br><br>
</p>


## Installation
### Application (.exe)
> This is the best choice for **ease of instalation**.

* Download the "**csgo-autoaccept-setup.exe**" file
* Once you start the setup, **Windows Smartscreen will probably show a warning**, since Windows doesn't know who created the program
* To continue, press **More info** and **Run Anyway**
* In the setup, enter the folder you want the script to install into, and wait for the installation to finish
* After that, you're finished! Go into the folder where you installed the script and run **bot.exe**!


### Python Script
> This is the best choice for **speed** and **reliability**.

* To use the Python Script, download the "**csgo-autoaccept-script.zip**" file
* Extract the contents of the .zip file
* Open up cmd in the **csgo-autoaccept-script** folder (An easy way to do so is by entering **cmd** in the address bar)

<p align="center">
  <img src="images/cmd.png" alt="Opening the cmd"/>
</p>

* Create a venv
1. Locate your python installation folder. By default in: **C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe**
2. In the cmd window opened up earlier, type:
```C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv```
* Download the required dependencies by entering: 
```pip install -r requirements.txt```
* After that, you're set up! Start the bot by using the ```python bot.py``` command!
