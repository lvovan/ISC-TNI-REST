# ISC-TNI-REST Travaux Pratiques sur les API REST

## Objectif du TP
Lors de cette séance de travaux pratiques nous allons développer un service REST en Python, que nous allons ensuite sécuriser par le biais d'un jeton et consommer de deux manières différentes.

## Pré-requis
Ce TP requiert un certain nombre de prérequis techniques sur votre machine:
  - Python 3.x
  - Postman ([téléchargement](https://github.com/portapps/postman-portable/releases/download/8.5.1-50/postman-portable-win64-8.5.1-50.7z))

## Step 1. Installez FastAPI
Depuis la ligne de commande dans votre dossier de travail, exécutez: `pip install "fastapi[all]"`

## Step 1. Implémentation du serveur REST (Python, Flask)
FastAPI étant installé, vous pouvez maintenant lancer votre serveur REST:
 - Exécutez `uvicorn main:app --reload`
 - Lancez un navigateur et naviguez vers [http://localhost:8000](http://localhost:8000), vous recevez une réponse au format json!
 - Modifiez le code source pour renvoyer une autre valeur et testez à nouveau

FastAPI dispose d'une fonctionnalité de documentation automatique. Pour la voir en action, naviguez vers une de ces deux adresses:
 - [http://localhost:8000/docs](http://localhost:8000/docs)
 - [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Step 2. Consommation de l'API
Utilisez Postman pour déterminer le fonctionnement de l'API.
 - Utilisez la fonctionnalité de documentation automatique pour vous guider
 - N'oubliez pas de spécifier l'entête (header) `content-type` avec la valeur `application/json`

## Step 3. Modification de l'API
Une fois l'API maitrisée, modifiez le fichier **main.py** pour y ajouter l'opération DELETE qui supprimera un objet existant de la liste, et renverra une erreur 404 si l'objet spécifié n'est pas trouvé.
