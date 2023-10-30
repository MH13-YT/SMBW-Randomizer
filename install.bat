@echo off
cls
echo SMBW Randomizer, dependencies installer
echo -----------------------------------------
echo The following packages will be installed on your computer and are necessary to run the SMBW Randomizer:
echo - Python: Program: Source Winget "https://apps.microsoft.com/search/publisher?name=Python+Software+Foundation&hl=en-US&gl=US"
echo - PyYAML: Python Module: Source PIP "https://pypi.org/project/PyYAML/"
echo - byml: Python Module with executables: Source PIP "https://pypi.org/project/byml/"
echo.
pause

REM Installing Python with Winget
winget install Python

REM Installing Python dependencies from requirements.txt
pip install -r requirements.txt

echo Installation completed. Please check if Python executables are startable.

REM Checking the byml_to_yml executable
where byml_to_yml > nul
if %errorlevel%==0 (
    echo byml_to_yml: Test Passed
) else (
    echo byml_to_yml: Test Failed
    echo Installation failed, please retry with manual installation.
    pause
    exit /b 1
)

REM Checking the yml_to_byml executable
where yml_to_byml > nul
if %errorlevel%==0 (
    echo yml_to_byml: Test Passed
) else (
    echo yml_to_byml: Test Failed
    echo Installation failed, please retry with manual installation.
    pause
    exit /b 1
)

pause