# ISC-TNI-REST Travaux Pratiques sur les API REST

## Objectif du TP
Lors de cette séance de travaux pratiques nous allons déployer une API REST, l'utiliser et la modifier.

## Pré-requis
Ce TP requiert un certain nombre de prérequis techniques sur votre machine:
  - Python 3.x
  - Bruno ([téléchargement](https://www.usebruno.com/)), un outil qui vous permettra de tester vos requêtes REST plus facilement

## Step 1. Installez FastAPI
1. Assurez-vous d'avoir le fichier [main.py](main.py) dans votre dossier de travail
2. Depuis la ligne de commande dans votre dossier de travail, exécutez: `pip install "fastapi[all]"`

## Step 1. Implémentation du serveur REST (Python, Flask)
FastAPI étant installé, vous pouvez maintenant lancer votre serveur REST:
 - Exécutez `uvicorn main:app --reload` depuis le dossier contenant **main.py**
 - Lancez un navigateur et naviguez vers [http://localhost:8000](http://localhost:8000), vous recevez une réponse très simple au format json
 - Modifiez la fonction adéquate dans **main.py** pour renvoyer une autre valeur et testez à nouveau

FastAPI dispose d'une fonctionnalité de documentation automatique. Pour la voir en action, naviguez vers une de ces deux adresses:
 - [http://localhost:8000/docs](http://localhost:8000/docs)
 - [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Step 2. Consommation de l'API
Utilisez Bruno pour tester et comprendre le fonctionnement de l'API.
 - Utilisez la fonctionnalité de documentation automatique de l'étape précédente pour vous guider
 - N'oubliez pas de spécifier l'entête (header) `content-type` avec la valeur `application/json`

## Step 3. Modification de l'API
Une fois l'API maitrisée, modifiez le fichier **main.py** pour y ajouter l'opération DELETE qui supprimera un objet existant de la liste, et renverra une erreur 404 si l'objet spécifié n'est pas trouvé.
