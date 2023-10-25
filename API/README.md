# h23_team6
 Repertoire pour le hacktoberfest Lome de l'équipe 6

# Projet 4
## Description/Contexte 
Un espace numérique dédié à la célébration et à la documentation de l'histoire et de la culture togolaises.
## Objectifs principaux 
- Documenter et préserver l'histoire et la culture du Togo.
- Faciliter l'accès à des informations culturelles pour les résidents et les touristes.
- Promouvoir la richesse et la diversité culturelles du Togo.


# Documentation pour installer le projet 
## API 
- git clone récupération du projet
- Mise en place de l'environnement virtuel
  - python -m venv venv
  - venv\Scripts\activate (pour activer l'environnement)
- installer les dépendannces
  - pip install -r requirements.txt
- créer la base de données projethacktober dans postgres (port:5432) pour modifier la configuration base de données aller dans le fichier app.py ligne 30
- lancer le projet avec la commande 
  - flask run --host=0.0.0.0 --port=5000
    - Accéder à la http://127.0.0.1:5000/swagger-ui pour voir les routes de l'api et savoir si ça fonctionne

## Frontend
