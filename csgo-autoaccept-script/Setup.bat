@ECHO OFF
if exist %HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\ (
	goto setup
) else (
	goto doesntexist
)

:setup
title AutoAccept Setup
for /f "delims=" %%a in ('dir /ad /b %HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python') do set "pyfolder=%%a"
@ECHO ON
%HOMEDRIVE%%HOMEPATH%\AppData\Local\Programs\Python\%pyfolder%\python.exe -m venv .venv
%cd%\.venv\Scripts\pip.exe install -r assets\requirements\requirements.txt
GOTO:eof

:doesntexist
@ECHO ON
echo & echo. & echo. & echo. Python is not installed in the default location! Please install the script manually. & echo. & echo.
pause