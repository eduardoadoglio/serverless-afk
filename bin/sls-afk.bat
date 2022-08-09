@echo off
START /wait /b cmd /c "python %~dp0serverless-afk.py start" >nul 2>&1
START /wait /b cmd /c "serverless" %* 
START /wait /b cmd /c "python %~dp0serverless-afk.py end" >nul 2>&1