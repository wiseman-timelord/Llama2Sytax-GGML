@echo off
mode 90,37
con:cols=89 lines=200
title Llama2-Syntax
cls

:: Run the freqbeat.py script
echo Launching Llama2-Syntax...
echo.
@echo on
wsl python3 syntax.py
@echo off
echo.
echo.

:: Exiting
echo Llama2-Syntax Shutting Down...
echo.
echo.
pause
exit /b
