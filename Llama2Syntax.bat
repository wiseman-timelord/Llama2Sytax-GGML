@echo off
mode 90,37
con:cols=89 lines=200
title Model-Syntax
cls

:: Run the freqbeat.py script
echo Launching Model-Syntax...
echo.
@echo on
wsl python3 syntax.py
@echo off
echo.
echo.

:: Exiting
echo Model-Syntax Shutting Down...
echo.
echo.
pause
exit /b
