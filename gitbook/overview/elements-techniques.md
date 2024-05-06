---
description: Explique le fonctionnement Technique de SMBW Randomizer
---

# ⚙️ Eléments Techniques

{% hint style="info" %}
Les romfs de chaque jeux Nintendo Switch contiennent un pack de fichiers RessourceSizeTable (RSTB)\
\
Ce fichier permet a la Nintendo Switch de savoir la taille prévu de chaque fichier du ROMFS et ce dernier doit être corrigé pour faire fonctionner tout mod Switch
{% endhint %}

{% hint style="info" %}
Le projet est développé en Python 3 et n'est pas compilé via les outils de conversion\
\
Cela permet de comparer le code source disponible sur github et le code téléchargé ce qui est un gage de sécurité
{% endhint %}

## Etape Préliminaires : Nettoyage du dossier Output, et vérification de la configuration

Avant de commencer SMBW Randomizer va réaliser quelques etapes préliminaire\
\
La première est de s'assurer que le fichier de configuration ne présente aucune incohérence par exemple si aucun module de randomisation n'est actif il est inutile de continuer\
\
si il y'a pas d'incohérence dans la configuration la suite de cette etape va \
\- générer la liste des fichiers demandé par chaque modules, prérequis indispensable pour l'étape 1\
\- nettoyer le contenu du dossier output

{% hint style="info" %}
Si l'utilisateur a choisi d'utiliser des mods externe d'autres etapes sont activé :\
\
\- La sauvegarde du dossier romfs dans le dossier romfs\_backup\
Si le dossier romfs\_backup n'existe pas il est tout simplement crée a partir du romfs\
Si le dossier romfs\_backup existe : une comparaison des hash des deux dossiers est lancé\
\
Si les hashs ne correspondent pas le dossier est régénéré et dans le cas contraire il passe a l'etape suivante\
\
\- L'inclusion des mods choisi dans le dossier romfs\
Chaque mods selectionné va etre copié dans la romfs et remplacer l'original (c'est le meme comportement que le chargement d'un mod sur console ou emulateur)\
\
Les fichiers des mods ayant été copié sont aussi répertorié dans la variable "modded\_file\_list"\
cette variable est accessible de l'extérieur via la fonction "get\_modded\_file\_list()"\
\
Il existe cependant certains fichiers qui seront ignoré par défaut dans cette procédure\
\- Les fichiers RSTB : Car corrigé automatiquement plus tard\
\- Le dossier Mals : Ce dossier contient tout les textes du jeu, ce dernier est adapté pour chaque mods, ce dernier est ignoré pour simplifier la procédure car les mods actuel peuvent fonctionner sans\*\
\
\* la seule exception connu est le mod qui rend les fleurs cancan vulgaire mais ce dernier a été strike par Nintendo
{% endhint %}

{% hint style="danger" %}
Si vous avez activé le support d'un mod NE COUPEZ SURTOUT PAS le script en cours d'exécution\
\
Si cela se produit (suite a une fausse manipulation ou a un plantage), ne réouvrez SURTOUT PAS SMBW\_Randomizer sans avoir réaliser la procédure çi dessous
{% endhint %}

{% content-ref url="../diagnostiques/dossiers-romfs-corrompus.md" %}
[dossiers-romfs-corrompus.md](../diagnostiques/dossiers-romfs-corrompus.md)
{% endcontent-ref %}

## Etape 1 : Extraction de métadonnées

Les fichiers de Super Mario Bros Wonder sont construit d'une maniere bien précise, les fichiers utilisé actuellement par SMBW Randomizer sont généralement au format .byml / .bgyml et certains de ces fichiers sont compressé en .zs (ZStandard)\
\
Pour simplifier les démarches la première partie de mon programme génère des métadonnées a partir de la liste de fichiers requis par les différents modules de randomisation\
\
dans ces métadonnées nous pouvons trouver par exemple\
\
\- Le nom du fichier (sans ses extensions)\
\- L'emplacement du fichier prévu (romfs, worktable et output)\
\- L'extension de fichier cible\
\- Si le fichier est compressé et si oui avec quel extension ainsi que l'extension du fichier décompressé



## Etape 2 : Extraction des données

A partir des métadonnées obtenu dans l'étape précédent SMBW\_Randomizer utilise diverses procédures pour l'extraction des données \
(les fichiers sont décompressé / copié depuis romfs vers worktable)\
\
La décompression (si le fichier est compressé) est effectué en utilisant : \
\- La librarie ZStandard pour les fichiers .zs\
\
La copie (si le fichier n'est pas compressé) est effectué en utilisant la librarie Shutil\
\
La conversion des fichiers en variable python est effectué en utilisant :\
\- La librarie byml pour les fichiers .byml et .bgyml\


## Etape 3 : Randomisation

La randomisation est effectué via les différents modules de randomisation, ces derniers sont exécuté de manière procédurale (il randomise la variable les uns après les autres)

{% hint style="info" %}
Les données d'origine sont modifié pour etre randomisé avec le premier module ce qui retournera une version randomisé avec le premier module\
\
Cette version randomisé par le premier module est ensuite envoyé au deuxième module qui retournera une version randomisé par le premier et deuxième module\
\
et ainsi de suite jusqu'à ce que tout les modules ait procédé a une randomisation ce qui retournera la version complète (comportant les randomisation de tout les modules actif)
{% endhint %}

{% hint style="info" %}
Cela signifie que si un module peut écraser les randomisation d'un autre bien que c'est pas censé arriver vu que chaque module vise des données différentes (même si ils visent un fichier identique)
{% endhint %}

## Etape 4 : Insertion des données randomisé

{% hint style="info" %}
Si l'utilisateur a choisi d'utiliser des mods externe d'autres etapes sont activé avant l'insertion des données randomisé\
\
La copie du contenu des fichiers moddé depuis romfs vers output \
(grace a la fonction "get\_modded\_file\_list()")
{% endhint %}

A partir des métadonnées obtenu dans l'étape précédente et de la version randomisé des donnés extraite en etape  SMBW\_Randomizer utilise diverses procédures pour l'insertion des données\
(les fichiers sont décompressé / copié depuis worktable vers output)\
\
La conversion des variables python en fichiers est effectué en utilisant :\
\- La librarie byml pour les fichiers .byml et .bgyml\
\
La compression (si le fichier était compressé) est effectué en utilisant : \
\- La librarie ZStandard pour les fichiers .zs\


{% hint style="info" %}
Si des fichiers moddés ont été randomisé ces derniers remplaceront leurs version non randomisé déja copié dans output\
\
Par conséquent meme le contenu des mods est randomisé
{% endhint %}

## Etape 5 : Adaptation des Fichiers RSTB (RessourceSizeTable)

{% hint style="info" %}
Les fichiers RSTB sont les fichiers qui contiennent la taille limite de chaque fichiers présent dans la ROMFS du jeu (il y'a un fichier par version) (si un fichier listé dans la RSTB dépasse sa limite de taille cela peut causer des erreurs qui peuvent entrainer un plantage du jeu)\
\
(Théoriquement ce n'est pas censé arriver puisque du point de vue de Nintendo les fichiers ne sont pas censé être altéré) sauf quand on utilise des mods ou un randomizeur\
\
Par conséquent SMBW Randomizer (comme tout programme générant des mods) doit prendre en compte ces éléments et corriger chaque fichiers RSTB\
\
Pour cela la solution la plus simple est de supprimer l'entrée des fichiers altéré et c'est cette solution qui est utilisé par SMBW\_Randomizer
{% endhint %}

A partir des metadonnées il est possible de savoir quel fichier sera altéré par le randomiseur et par conséquent quel fichiers doivent etre retiré des fichiers RSTB pour permettre leurs chargement

{% hint style="info" %}
Si l'utilisateur a choisi d'utiliser des mods externe la meme procedure s'execute en utilisant la fonction "get\_modded\_file\_list()"\
\
Si l'entrée a déjà été supprimé elle est tout simplement ignoré du processus\
\
Cela permet aussi d'étendre le support des mods a des version considéré non supporté (car tout les fichiers RSTB sont adapté)
{% endhint %}

Une fois ces procédures terminé les fichiers RSTB sont copié dans output

## Etape 6 : Retour des fichiers randomisé a l'utilisateur

Les fichiers de sortie sont adapté sous plusieurs format (adapté aux usages généraux d'un mod switch)\
\
romfs : est le dossier romfs standard utilisable n'importe ou tant que on respecte la methode imposé par l'outil utilisé (Atmosphere, Yuzu / Suyu ...)\
\
YUZU : ce dossier contient une variante du dossier romfs packagé pour etre utilisable sur yuzu par simple copie de son contenu a la racine du dossier de yuzu ou un de ses forks comme suyu)\
\
RYUJINX : ce dossier contient une variante du dossier romfs packagé pour etre utilisable sur ryujinx par simple copie de son contenu a la racine du dossier de ryujinx\
\
SMM : ce dossier contient une variante du dossier packagé pour être géré par l'homebrew Simple Mod Manager, il suffit de copier le dossier mods a la racine de votre carte SD puis d'ouvrir Simple Mod Manager pour activer le mod Randomized pour Super Mario Bros Wonder\
\


## Etape 7 : Nettoyage

Avant la fermeture du programme SMBW Randomizer fait un nettoyage des fichiers présent dans Worktable

{% hint style="info" %}
Si l'utilisateur a choisi d'utiliser des mods externe le dossier romfs sera aussi supprimé puis recrée a partir du dossier romfs\_backup
{% endhint %}

{% hint style="danger" %}
Pour rappel NE COUPEZ SURTOUT PAS le script en cours d'exécution lors de cette procedure\
\
Si cela se produit (suite a une fausse manipulation ou a un plantage), ne réouvrez SURTOUT PAS SMBW\_Randomizer sans avoir réaliser la procédure çi dessou
{% endhint %}

{% content-ref url="../diagnostiques/dossiers-romfs-corrompus.md" %}
[dossiers-romfs-corrompus.md](../diagnostiques/dossiers-romfs-corrompus.md)
{% endcontent-ref %}
