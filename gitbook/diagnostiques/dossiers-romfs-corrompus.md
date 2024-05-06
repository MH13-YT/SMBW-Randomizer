---
description: >-
  Cette page permet de résoudre les problemes relatif a des dossiers ROMFS
  Corrompus suite a l'utilisation de mods et vous permettra de restaurer votre
  ROMFS
---

# ⁉️ Dossiers RomFS Corrompus

### Causes Possibles

{% hint style="warning" %}
Si SMBW Randomizer a rencontré une erreur alors vous avez activé le support des mods
{% endhint %}

{% hint style="danger" %}
Si vous avez fermé SMBW Randomizer en ayant activé le support des mods
{% endhint %}

### Solution

{% hint style="danger" %}
Ne réouvrez SURTOUT pas SMBW Randomizer avant d'avoir réalisé les opérations suivantes (Cela ne résoudra rien bien au contraire)\
\
Si vous réouvrez SMBW\_Randomizer sans avoir réaliser la manipulation votre dossier romfs\_backup sera automatiquement corrompu car remplacé par une copie de votre romfs corrompu suite a son arret en cours d'execution
{% endhint %}

Supprimez le dossier romfs et utiliser le dump du romfs que vous possédez pour restaurer le dossier\
\
Lors du prochain lancement d'SMBW Randomizer (en activant le support des mods) le dossier romfs\_backup si il a été corrompu sera automatiqument restauré (car les hashs ne correspondra pas)\
\
si les hashs correspondent alors le dossier est intact et ne sera pas recrée

{% hint style="danger" %}
Par sécurité n'utilisez pas le dossier romfs\_backup comme base pour votre copie il est possible qu'il soit corrompu (selon l'étape ou l'application a planté)
{% endhint %}

