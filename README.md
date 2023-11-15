"""
## Doctolib_Clementine

Doctolib_Clementine est une plateforme web dynamique construite avec le framework Django. Notre objectif est de fournir une solution efficace et intuitive pour voir encore plus de professionnels de santé et surtout de publier régulièrement des enquêtes sur la santé des patients consentants.

## Prérequis

Python 3.10.12
Django==4.2.5 

dependance python :
asgiref==3.7.2
django-crispy-forms==2.1
django-formtools==2.4.1
Faker==20.0.3
joblib==1.3.2
numpy==1.26.0
packaging==23.1
pandas==2.1.0
plotly==5.17.0
python-dateutil==2.8.2
pytz==2023.3.post1
scikit-learn==1.3.0
scipy==1.11.2
six==1.16.0
sqlparse==0.4.4
tenacity==8.2.3
threadpoolctl==3.2.0
typing_extensions==4.8.0
tzdata==2023.3

Base de données SQLite

## Installation
Étape par étape pour obtenir un environnement de développement opérationnel. Voici un exemple :

- Cloner le dépôt Git (si applicable) :
git clone git@github.com:data-IA-2022/Doctolib_Clementine.git
cd votre-projet

- Configurer un environnement virtuel (sur linux):
python -m venv venv
source venv/bin/activate  
--> Sur Windows : venv\Scripts\activate

- Installer les dépendances :
pip install -r requirements.txt

- Configurer les variables d'environnement :
Expliquez comment configurer les variables d'environnement nécessaires (comme les secrets Django, les configurations de base de données, etc.). Vous pouvez fournir un fichier .env.example comme modèle.

- Initialiser la base de données :
python manage.py makemigrations
python manage.py migrate

- Créer un superutilisateur (si nécessaire) :
python manage.py createsuperuser

- Lancer le serveur de développement :
python manage.py runserver

- Accédez ensuite à http://localhost:8000 dans votre navigateur.


## Contribuer

Nous sommes ravis que vous envisagiez de contribuer à notre projet ! Voici quelques directives à suivre pour contribuer efficacement.

- Rapporter des Bugs et Demander des Fonctionnalités
Si vous trouvez un bug ou si vous avez une idée de fonctionnalité, n'hésitez pas à utiliser notre système de suivi des problèmes. Veuillez vérifier d'abord que le problème n'a pas déjà été signalé.

- Envoyer des Pull Requests
Si vous souhaitez apporter des modifications au code, veuillez suivre ces étapes :

-->Forker le Projet : Commencez par forker le projet sur votre compte GitHub personnel.

-->Créer une Branche : Créez une branche pour vos modifications. Utilisez un nom de branche descriptif.
git checkout -b nom_de_votre_branche

-->Apporter vos Modifications : Effectuez vos modifications dans cette branche. Assurez-vous de respecter les conventions de codage du projet.

-->Tester vos Modifications : Assurez-vous que votre code passe tous les tests existants et, si possible, ajoutez des tests pour couvrir vos modifications.

-->Documenter vos Changements : Mettez à jour la documentation si nécessaire.

-->Soumettre une Pull Request : Poussez votre branche sur votre fork et soumettez une pull request au projet principal. Dans la description de votre pull request, expliquez vos changements et pourquoi vous pensez qu'ils devraient être inclus.

- Conventions de Codage et Normes
-->Style de Code : Suivez le style de code PEP 8 pour Python et utilisez des pratiques cohérentes pour le HTML/CSS/JavaScript.
-->Commit Messages : Utilisez des messages de commit clairs et descriptifs.
-->Tests : Ajoutez des tests pour chaque nouvelle fonctionnalité ou correction de bug.

- Processus de Révision
Les pull requests seront révisées par les mainteneurs du projet. Des discussions peuvent avoir lieu dans les commentaires de la pull request si des ajustements sont nécessaires.

Nous remercions chaque contributeur pour leur engagement et leur travail. Votre contribution rend ce projet meilleur et plus riche.

## Licence
Ce projet est sous licence libre - voir le fichier LICENSE.md pour plus de détails.
"""