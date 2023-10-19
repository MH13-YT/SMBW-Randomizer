echo off
cls
echo SMBW Randomizer, dependances installer
echo ---------------------------------------
echo Theses packages will be installed on your computer, and are necessary for run SMBW_Randomizer
echo - Python : Program : Source Winget "https://apps.microsoft.com/search/publisher?name=Python+Software+Foundation&hl=fr-fr&gl=FR"
echo - PyYAML : Python Module : Source PIP "https://pypi.org/project/PyYAML/"
echo - byml : Python Module with executables : Source PIP "https://pypi.org/project/byml/"
pause
winget install python
pip install -r requirements.txt
pause
