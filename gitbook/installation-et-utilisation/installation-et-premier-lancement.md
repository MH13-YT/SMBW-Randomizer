# 🛠️ Installation et Premier Lancement



{% hint style="warning" %}
Ce projet ne peut pas être utilisé sur une Nintendo Switch non modifié ou équipé d'une cartouche Mig Switch vous devez posséder l'un de ces deux éléments\
\- une console Nintendo Switch utilisant un Custom Firmware : (Atmosphère)\
\- un émulateur Nintendo Switch configuré correctement : (Yuzu / Suyu ou Ryujinx)
{% endhint %}

{% hint style="warning" %}
Le projet nécessite aussi un dump RomFS du jeu obtensible uniquement en réalisant un dump du jeu original : Super Mario Bros Wonder\
\
Ce dump ne sera JAMAIS intégré au sein du code source de SMBW Randomizer et toute demande a ce sujet sera rejeté
{% endhint %}

{% hint style="danger" %}
En tant que créateur du projet je déconseille fortement de partager publiquement les dossiers ROMFS car ces derniers sont la propriété intellectuelles de Nintendo\
\
En partageant ces fichiers vous vous exposez a des risques d'ordre juridique
{% endhint %}

<details>

<summary>Etape 1 : Prérequis Logiciel</summary>

Windows :\
\- Python 3 : Versions Supportés : 3.6 a 3.11\
doit être ajouté au PATH et NE DOIT PAS etre installé depuis le Microsoft Store / WinGet\
(Attention : Assurez vous que les Alias python et python 3 sont désactivé dans les paramètres de Windows)\
\
Linux et Mac OS : \
\- Python 3 : Versions Supportés : 3.6 a 3.11\
\
Linux\
\- tk : Tcl/Tk GUI toolkit (Nécessaire pour faire fonctionner les interfaces graphiques)\
\
Attention : les nom peut changer en fonction de votre environnement Linux

</details>

<details>

<summary>Etape 2 : Copie des Fichiers de Super Mario Bros Wonder (Dump RomFS)</summary>

Il est possible d'extraire la ROMFS d'un jeu de diverses manieres\
\
Vous pouvez le faire par le biais de votre Nintendo Switch Modifié ou par le biais d'un émulateur fonctionnel (si vous possédez déjà les fichiers NSP)\
\
Je vous laisse rechercher la procédure qui vous correspond le mieux sur Google\
(suite a l'affaire Tropic Haze vs Nintendo je préfère éviter de fournir un guide détaillé)\
\
une fois le dossier romfs de Super Mario Bros Wonder en votre possession il vous suffit de le copier au même endroit que le fichier SMBW\_Randomizer.py

</details>

{% hint style="warning" %}
Cette procédure est a réaliser a chaque mise a jour du jeu\
(vous pouvez remplacez les fichiers existant dans cette situation)
{% endhint %}

<details>

<summary>Etape 3 : Installation des paquets Python</summary>

Windows :\
\- Methode Automatique : il vous suffit de lancer install.bat, ce script batch s'assurera que python est installé correctement si tout est ok il listera les différents modules python qui seront installé et vous demandera une confirmation, il vous suffira de l'accepter pour lancer l'installation, a la fin de l'installation il vérifiera que tout est bien installé et accessible\
\
Windows / Linux / Mac OS\
\- Methode Manuelle : ouvrez une invite de commande a l'emplacement de SMBW\_Randomizer.py et executez la commande suivante

```
pip install -r requirements.txt
```

</details>

<details>

<summary>Step 4: Lancer le programme</summary>

Windows :\
\- Methode Automatique : il existe plusieurs scripts de lancement pour SMBW\_Randomizer\
(Chaque Script demande de maniere facultative si l'utilisateur veut écrire/utiliser une seed précise).\
Si aucune seed n'est écrite/utilisé SMBW\_Randomizer en génèrera une aléatoirement\
Le script utilise l'argument CLI --seed (suivi de la seed en question) si une seed a été rentrée par l'utilisateur\
\
"run.bat" : Lance SMBW\_Randomizer avec les parametres par défaut \
\
"run\_with\_mods.bat" : Lance SMBW\_Randomizer avec les parametres par défaut et l'argument --mods qui permettra a l'utilisateur de selectionner les mods a utiliser (a partir d'une interface graphique)\
\
"configure.bat" : Lance SMBW\_Randomizer avec l'argument --configure permettant de lancer l'interface graphique de configuration\
\
Windows / Linux / Mac OS\
\- Methode Manuelle : ouvrez une invite de commande a l'emplacement de SMBW\_Randomizer.py et exécutez la commande suivante

```
python.exe SMBW_Randomizer.py <arguments>
```

Vous pouvez utiliser l'argument -h pour obtenir la liste des arguments disponible.\
\
Exemple :

```
python.exe SMBW_Randomizer.py -h
```

Cette liste comporte en plus des arguments cité ci dessus les argument CLI (Command Line Interface) de SMBW\_Randomizer\
(cette dernière est dédié aux utilisateurs dépourvu d'interface graphique et aux utilisateurs expérimentés)\
\
Si SMBW\_Randomizer.py ne trouve pas de fichier config.json ou que le config.json stipule qu'aucun fichier de configuration n'a été choisi l'interface de configuration s'ouvrira automatiquement \
\
(ce fichier est généré / régénéré si l'utilisateur a utilisé l'argument --configure-cli par conséquent l'interface graphique ne sera pas ouvert automatiquement si sa configuration est valide

</details>

{% hint style="info" %}
Le contenu des script batch (.bat) peuvent être vérifiés en cliquant droit et en choisissant modifier (en utilisant le bloc notes) ou en utilisant un IDE (comme Visual Studio Code)\
\
vous pouvez aussi vérifier leurs contenus sur le projet github
{% endhint %}

<details>

<summary>Etape 5 : Utilisation des données obtenus</summary>

Si l'étape 4 s'est déroulé correctement vous dévriez avoir dans le dossier output 4 dossiers\
\
(Pour les Utilisateurs de console Physiques Modifié)\
\- romfs : contenu du mod dans son format le plus basique\
(Doit etre copié dans l'un des dossiers suivant en fonction de votre CFW)\
(Si le dossier n'existe pas vous devez le créer\
Atmosphere : atmosphere/contents/010015100B514000/\
\
\- SMM : contenu du mod packagé pour fonctionner avec SIMPLE MOD MANAGER\
le dossier SMM contient un dossier mods, il vous suffira de le copier a la racine de votre carte SD\
\
(Pour les utilisateurs d'Emulateurs)\
\- YUZU : contenu du mod packagé pour fonctionner avec YUZU ou un de ses forks (comme SUYU par exemple)\
le dossier YUZU doit contenir un dossier nommé load, ce dernier doit etre copié a l'emplacement ou est stocké le dossier de l'emulateur\
pour obtenir son emplacement il vous suffit d'ouvrir l'émulateur et de cliquer sur ouvrir le dossier de "Nom de L'Emulateur"), cela vous ouvrira l'explorateur de fichier au bon emplacement et il suffira de coller le dossier load dedans\
\
\- RYUJINX : contenu du mod packagé pour fonctionner avec RYUJINX\
le dossier RYUJINX doit contenir un dossier nommé mods, ce dernier doit etre copié a l'emplacement ou est stocké le dossier de l'emulateur\
pour obtenir son emplacement il vous suffit d'ouvrir l'émulateur et de cliquer sur ouvrir le dossier de "Nom de L'Emulateur"), cela vous ouvrira l'explorateur de fichier au bon emplacement et il suffira de coller le dossier mods dedans

</details>



{% hint style="danger" %}
Si vous avez déjà utilisé SMBW Randomizer avant\
il est INDISPENSABLE de supprimer les dossiers suivants en fonction de votre situation et si ils existent\
\
\- Console Physique (Atmosphere)\
mods/Super Mario Bros Wonder/Randomized\
atmosphere/contents/010015100B514000/romfs\
\
\- Emulateur basé sur Yuzu (YUZU / SUYU ...)\
\<dossier de l'emulateur>/load/010015100B514000\
\
\- Emulateur basé sur Ryujinx (RYUJINX / RYUJINX LDN BUILD)\
\<dossier de l'emulateur>/mods/contents/010015100B514000/Randomized
{% endhint %}

Une fois toute ces procédures accompli il suffit&#x20;

* De désactiver (si necessaire) et réactiver le mod si vous êtes un Utilisateur de Simple Mod Manager ou d'un Emulateur&#x20;
* Lancer votre jeu et commencer a jouer\


Amusez vous bien avec SMBW\_Randomizer et que la chance soit de votre coté pour vos prochaines sessions
