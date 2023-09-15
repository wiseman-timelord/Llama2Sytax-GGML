@echo off
mode 90,37
con:cols=89 lines=200
title Llama2-Variants
cls

:: Run the freqbeat.py script
echo Launching Model-Syntax...
echo.
@echo on
wsl python3 variants.py
@echo off
echo.
echo.

:: Exiting
echo Llama2-Variants Shutting Down...
echo.
echo.
pause
exit /b
