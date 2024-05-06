---
description: Un moyen plus technique de contribuer au projet
---

# 💻 Développer de nouvelles fonctionnalités

{% hint style="warning" %}
Cette section est **UNIQUEMENT** dédié aux développeur python, possédant des connaissances en modding Switch et principalement sur celui de Super Mario Bros Wonder
{% endhint %}

## Développer un Module de Randomisation

Vous avez une idée d'élément a ajouter dans le jeu, il vous suffit de créer un module de randomisation et de le partager\
\
Pour cela il suffit de vous basez sur le module d'exemple mais pour cela vous devez réaliser quelques opérations

{% hint style="danger" %}
Avant toute chose vous devez vous devez suivre a la lettre la procédure disponible dans Fonctionnement du Repo Git\
dans le cas contraire votre pull request sera rejeté
{% endhint %}

### Création d'un environnement de travail adapté

Si vous avez suivi la procedure a la lettre vous devriez avoir\
\
\- Forké le projet SMBW\_Randomizer\
\- Avoir crée une branche respectant la convention de nommage suivante\
module-\<nom\_du\_module>-\<version>-\<nom\_d'utilisateur\_git>\
\- Etre da\
\
Si c'est le cas vous pouvez continuer

### Duplication du dossier d'exemple et reprogrammation des ligne relatives a l'identification du module

{% hint style="danger" %}
Le nom que vous allez choisir ne doit pas être identique a un module existant
{% endhint %}

Voici les deux étapes indispensable pour dupliquer le dossier d'exemple et le rendre unique en reprogrammant les élément relatif a son identification

{% tabs %}
{% tab title="Etape 1 : Copier le module d'Exemple" %}
Allez dans le dossier SMBW\_R/modules et dupliquer le dossier exemple\_module
{% endtab %}

{% tab title="Etape 2 : Modifier le nom du module" %}
* Choisissez un nom en respectant la structure suivante\
  (privilegier un nom en rapport avec ce que vous comptez randomizer)\
  le nom choisi ne doit pas avoir d'espace et ne doit pas contenir de caractères spéciaux interprétable comme du code par Python (le seul caractere spécial autorisé est "\__")_\
  \
  exemple : nom du module choisi : "random\_physics"
* Renommer le dossier du module\
  renommez votre copie du dossier "exemple\_module" par le nom de votre module\
  (exemple "random\_physics")\

* Renommez les éléments concernant le module dans le code\
  \- \_\_**init\_\_**.py (ligne 1) : remplacez "exemple" par le nom de votre module\
  (exemple : "random\_physics\_module")\
  \
  \- main.py (ligne 2, 7 et 9) : remplacez "exemple\_module" par le nom de votre module\
  (exemple : random\_physics)\

* OPTIONNEL mais fortement recommandé : Trouvez une description pour votre module et remplacez le contenu de la variable "module\_description"
{% endtab %}
{% endtabs %}

### Développement du Module

{% hint style="danger" %}
En dehors des éléments cité dans l'etape précédente ne modifiez AUCUN autre élément dans main.py\
\
le main.py d'exemple est adapté pour fonctionner parfaitement avec le code principal
{% endhint %}



{% hint style="info" %}
N'hésitez pas a prendre exemple sur les modules existant
{% endhint %}

#### functions.py

le fichier functions.py contient deux ressources importantes\
\
\- la variable "resources" : contenant le / les dossiers a cibler dans le code du jeu\
veillez a conserver la structure du romfs du JEU

\
\- l'extrait de code suivant (ligne 25 a 27)\
ce dernier représente la création de méthodes / profils

{% hint style="danger" %}
Les seuls éléments a modifier sont "Full" et "full" (représentant le nom de la methode, ainsi que l'appel de la fonction (profiles.full)\
\
Veillez a ne pas modifier les variables existantes dans l'appel
{% endhint %}

```python
        if method == "Full" or method == "full":
            data_dump = profiles.full(data_dump, seed)
            shuffle = True
```

#### profiles.py

le fichier profiles.py contient deux éléments important\
\
\- la fonction list() qui retourne la liste des profiles/methodes disponible\
par défaut (aux lignes 7 a 9) :

```python
[
'full',
]
```

\- la fonction full() qui est un exemple d'appel vers les randomisation\_scripts

```python
def full(data_dump, seed):
    ignored_files = [
    ]

    # Randomise Data and add ignored_files if is necessary
    return randomisation_scripts.exemple(data_dump,seed)
```

#### randomizer.py

Le fichier randomizer.py contient tout les scripts de randomisations et voici l'exemple par défaut intégré au fichier\
\
le  "" ligne 10 doit contenir le chemin romfs du dossier cible, cela permet de s'assurer que le script en dessous est utilisé pour le bon dossier

{% hint style="info" %}
L'exemple par défaut crée un input a partir de la variable data\_dump au démarrage du script et a la fin du script (l'idée est de vous aider a voir les modifications sur le code et a développer votre script de randomisation)\
\
Je vous conseille de modifier le script pour écrire un fichier input et output pour que vous puissiez lire plus facilement le data\_dump
{% endhint %}

Vous devez avoir autant de if que le nombre de dossier dans resources

```python
            if "file_data" in data and isinstance(data["file_data"], dict) and "" in data["resource_type"]: 
                pass # Insert Here Code of Randomization for selected resource
```

```python
import random

class randomisation_scripts:
    def exemple(data_dump,seed):
        random.seed(seed) # Configure Seed for Randomization
        print("INPUT")
        input(data_dump) # DEBUG : List Data Dump for helping to create randomizer
        for data in data_dump:
            # You must check resource_type to ensure that the data you are going to manipulate corresponds to the folder to modify 
            if "file_data" in data and isinstance(data["file_data"], dict) and "" in data["resource_type"]: 
                pass # Insert Here Code of Randomization for selected resource
        print("OUTPUT")
        input(data_dump) # DEBUG : List Data Dump for helping to create randomizer
        return data_dump
```



### Fin de Développement et Réalisation de la Pull Request

{% hint style="danger" %}
Pour simplifier le déploiement des correctifs et maintenir un ordre au sein du repo principal\
\
Vous devez suivre a la lettre la procédure disponible dans Fonctionnement du Repo Git\
dans le cas contraire votre pull request sera rejeté
{% endhint %}

Une fois que vous avez développé et testé votre module il vous suffit de lancer une pull request sur le repo principal\
\
Si votre pull request est accepté votre module sera déployé dans la branche développement pour être ensuite release a la prochaine version
