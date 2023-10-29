echo off
cls
echo SMBW Randomizer, dependances installer
echo ---------------------------------------
echo Theses packages will be installed on your computer, and are necessary for run SMBW_Randomizer
echo - Python : Program : Source Winget "https://apps.microsoft.com/search/publisher?name=Python+Software+Foundation&hl=fr-fr&gl=FR"
echo - PyYAML : Python Module : Source PIP "https://pypi.org/project/PyYAML/"
echo - byml : Python Module with executables : Source PIP "https://pypi.org/project/byml/"
echo
pause
winget install python
pip install -r requirements.txt
echo Installation Finished, verify if Python Executables is startable
where byml_to_yml > nul
if %errorlevel%==0 (
    echo byml_to_yml : Test Passed
) else (
    echo byml_to_yml : Test Failed
    echo Installation Failed, please retry with automated installation
    pause
    exit
)
where yml_to_byml > nul
if %errorlevel%==0 (
    echo yml_to_byml : Test Passed
) else (
    echo yml_to_byml : Test Failed
    echo Installation Failed, please retry with automated installation
    pause
    exit
)
pause
