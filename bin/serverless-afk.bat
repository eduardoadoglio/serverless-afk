@echo off
START /wait /b cmd /c "serverless" %* 
START /wait /b cmd /c "python %~dp0serverless-afk.py"