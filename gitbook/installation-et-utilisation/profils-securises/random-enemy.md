---
description: Description des parametres des profil sécurisés du module random_enemy
---

# Random Enemy

Il existe deux fichiers gérant la sécurité dans le module random\_enemy

### data\_config.json

les entrées correspondent aux identifiants des niveaux et chaque entrée a une seule option\
Pour savoir quel niveau correspond a quel id vous pouvez utiliser la page suivante du Wonderwiki :\
[https://shibbo.net/WonderWiki/index.php/Filesystem/romfs/BancMapUnit](https://shibbo.net/WonderWiki/index.php/Filesystem/romfs/BancMapUnit)



<table><thead><tr><th width="170">Nom de l'option</th><th>Description</th></tr></thead><tbody><tr><td>enabled</td><td>Active la randomisation des ennemis sur le terrain</td></tr></tbody></table>

### enemy\_config.json

les entrées correspondent aux identifiants des ennemis du jeu et chaque entrée a 3 options\
\
Pour savoir quel identifiant correspond a quel ennemi, il n'existe actuellement aucune Table de correspondance publique, vous pouvez cependant utiliser l'utilitaire [Fushigi](https://github.com/shibbo/Fushigi/releases), ce dernier montre les textures des ennemis de chaque niveau ainsi que leur identifiant\


<table><thead><tr><th width="170">Nom de l'option</th><th>Description</th></tr></thead><tbody><tr><td>enabled</td><td>Cette Option est géré par les profils custom : INUTILE DE LE MODIFIER</td></tr><tr><td>blacklisted</td><td>L'ennemi est blacklisté des randomisations général sécurisés<br>(Ce paramètre est ignoré pour le profil custom_secured)</td></tr><tr><td>enemy_name</td><td>Identifiant de l'ennemi : NE PAS MODIFIER</td></tr></tbody></table>
