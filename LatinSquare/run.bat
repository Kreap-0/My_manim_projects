@echo off

:Loop

data_generator.exe
solver.exe
checker.exe

fc checker.out answer.txt
if errorlevel=1 pause

goto :Loop