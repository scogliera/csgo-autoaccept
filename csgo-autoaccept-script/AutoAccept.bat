@ECHO OFF
if exist %cd%\.venv\ (
	%cd%\.venv\Scripts\python.exe bot.py
) else (
	echo Please run the setup.bat file!
	pause
)