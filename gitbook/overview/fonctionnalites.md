---
description: Présentation des fonctionnalités de SMBW_Randomizer
---

# ✨ Fonctionnalités

### Modules

{% tabs %}
{% tab title="Level Order" %}
#### Description

level\_order permet de randomiser l'ordre des niveaux dans la carte du jeu

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2024-04-01 054309.png" alt=""><figcaption><p>Level Order Randomization Result (Left : Original Game : Right Randomizer)<br>(Configuration : Full)</p></figcaption></figure>

#### Profiles

* Full : Randomise les niveau sans faire de distinction au niveau du monde
* Lite : Randomise les niveau en les gardant dans leurs mondes respectif\
  (Limite les Sauts de Difficultés)

#### Effets des profils sécurisé (\_secured)

* Randomise les niveau equipé de sortie secrète entre eux (Evite le bloquage de certaines zone)
{% endtab %}

{% tab title="Random Badges" %}
<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption><p>Changement automatique du Badges sur le Niveau Palais du Volcan Vegetal </p></figcaption></figure>

#### Description

Sélectionne un badge aléatoire pour chaque niveau \
Remplace le badge actuel par le badge sélectionné au lancement du dit niveau\
(Il est possible de remplacer le badge si le joueur le souhaite)

#### Profiles

* All : Prend en Compte tout les badges
* Action Only : Prend uniquement les Badges Action
* Bonus Only : Prend uniquement les Badges Bonus
* Expert Only : Prend uniquement les Badges Expert
* Custom : Prend une liste de badges précises (voir interface custom)

#### Interface Custom

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2024-04-01 060120.png" alt=""><figcaption><p>Interface de sélection des badges pour le Profil Custom<br>(L'ordre des badges est la meme que celle du jeu)</p></figcaption></figure>
{% endtab %}

{% tab title="Random Wonder" %}
<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption><p>Effet du Module Random Wonder sur un Niveau</p></figcaption></figure>

#### Description

Modifie les effets des fleurs wonder de maniere aléatoire\
Les fleurs wonder ont deux type d'effets : Les effet et les transformations\
\- Les effets modifie le terrain (le rend glissant, change la perspective ...)\
\- Les transformation transforme le joueur (en goomba, en ball, en ballon, en version allongé ...)

#### Profiles

* all : Randomise avec tout les effets et transformation
* all\_exclude\_goomba : Randomise avec tout les effet et transformation sauf le goomba
* morph\_only : Randomise uniquement avec les transformation
* morph\_only\_exclude\_goomba : Randomise uniquement avec les transformation sauf le goomba
* effect\_only : Randomise uniquement avec les effets
* custom : Randomise uniquement avec les effets et les transformation souhaité par le joueur

Le goomba peut etre exclu car ce dernier empeche de sauter ce qui peut rendre les niveau injouable

#### Interfaces Custom

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2024-04-01 061701.png" alt=""><figcaption><p>Interface de selection des effets pour le profil custom</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2024-04-01 061622.png" alt=""><figcaption><p>Interface de selection des transformations pour le profil custom</p></figcaption></figure>

#### Effets des profils sécurisé (\_secured)

Permet de forcer la désactivation de la randomisation des effet et/ou transformation dans un niveau précis
{% endtab %}

{% tab title="Random Enemy" %}
<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption><p>Exemple d'impact du module random_enemy sur un niveau</p></figcaption></figure>

#### Description

Modifie les ennemis dispersé sur les niveaux de manière aléatoire (Ne remplace pas les boss)

#### Profiles

* all : Randomise tout les ennemis
* custom : Randomise uniquement certains ennemis

#### Interfaces Custom

<div data-full-width="true">

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption><p>Interface de selection des ennemis (profil custom)<br>Vous pouvez utiliser fushigi ou le wiki de mario wonder pour associer les identifiants au ennemis concernés</p></figcaption></figure>

</div>

#### Effets des profils sécurisé (\_secured)

Permet de bloquer la randomisation de certains ennemis précis et bloque la randomisation dans les niveaux trop problématique
{% endtab %}

{% tab title="Random Areaparam" %}
<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>Effet du module random_areaparam sur le niveau "Badge Challenge Coup du Dauphin 1"</p></figcaption></figure>

#### Description

Modifie les ressources relatives a l'areaparam de maniere aléatoire\
\
L'areaparam gere toutes les ressources relatif au niveau (Arriere plan, Theme, Musique ...) y compris lors des effets wonder

#### Profiles

* all : Randomise l'intégralité de l'areaparam

#### Effets des profils sécurisé (\_secured)

Permet de forcer la désactivation de la randomisation des element précis de l'areaparam dans un niveau précis
{% endtab %}
{% endtabs %}

