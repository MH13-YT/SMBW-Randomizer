---
description: Le meilleur moyen pour contribuer au projet tout en vous amusant
---

# 🛡️ Améliorer les profils sécurisé

{% hint style="info" %}
Rappel : Les profils sécurisé (caractérisé par dans l'application le suffixe "-secured") permettent de désactiver la randomisation d'une fonction dans un niveau précis pour éviter des soft locks / niveau infaisable par exemple\
\
La modification des profils ne nécessite pas d'outils particulier ou de compétences technique précise (notamment en développement)
{% endhint %}

Lorsque on randomise un jeu il peut arriver que le hasard cause des élément non prévu par le jeu ce qui peut mener a des soft lock ou au blocage de certains niveaux ce qui peut être frustrant.\
\
Cependant le projet a été conçu pour vous permettre de régler ces petit bugs a votre échelle a condition d'être curieux

### Déterminez le module responsable du bug

Pour cela il suffit de trouver la ressource impacté\
\
Par exemple \
\- si vous touchez une fleur wonder et que le jeu se softlock cela provient surement du module random\_wonder\
\
\- si vous touchez une fleur wonder et que les effets en rythme avec la musique ne se déclenche pas, le soucis provient surement du module random\_areaparam\
\
\- si vous touchez une fleur wonder et qu'un ennemi important n'apparait pas cela provient surement du module random\_enemy

### Experimenter pour corriger le bug

Cette procedure dépend beaucoup de la situation, pour l'expliquer de la manière la plus simple possible il suffit de manipuler les fichiers concerné a l'aide des ressources relatif au Profils Sécurisé

{% content-ref url="../../installation-et-utilisation/profils-securises/" %}
[profils-securises](../../installation-et-utilisation/profils-securises/)
{% endcontent-ref %}

Je vous conseille de trouver la solution la moins impactante pour éviter de trop d'empêcher la randomisation le jeu

### Réaliser une pull request sur le projet

{% hint style="danger" %}
Pour simplifier le déploiement des correctifs et maintenir un ordre au sein du repo principal\
\
Vous devez suivre a la lettre la procédure disponible dans Fonctionnement du Repo Git\
dans le cas contraire votre pull request sera rejeté
{% endhint %}

une fois que vous avez trouvé un correctif au bug il vous suffit de suivre la pricedure relative a l'amélioration des profils sécurisé\
\
De commit votre et push votre correctif puis demander une pull request vers la branche development\
\
Si votre pull request est accepté votre patch sera implémenté dans development et implémenter a la prochaine version\
