@echo off
cls
where byml_to_yml > nul
if %errorlevel% neq 0 (
    echo byml_to_yml : Test Failed
    echo Cannot start the randomizer without this executable, try running install.bat
    pause
    exit
)
where yml_to_byml > nul
if %errorlevel% neq 0 (
    echo yml_to_byml : Test Failed
    echo Cannot start the randomizer without this executable, try running install.bat
    pause
    exit
)
python SMBW_Randomizer.py
pause