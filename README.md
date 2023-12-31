"""
## Doctolib_Clementine

Doctolib_Clementine est une plateforme web dynamique construite avec le framework Django. Notre objectif est de fournir une solution efficace et intuitive pour voir encore plus de professionnels de santé et surtout de publier régulièrement des enquêtes sur la santé des patients consentants.

## Les fonctionnalités

- Un administrateur (en général le responsable d’un cabinet médical) :
	1-attribue des comptes aux médecins qui le souhaitent. 
	2-Il est en mesure de consulter le compte du médecin et de voir l’ensemble des patients suivis. 
	3-ll peut crud des patients et des médecins. 
	4-C’est lui qui attribue un patient à un médecin. 
	5-Il peut voir l’historique des informations remplies par les patients dans un tableau possédant des filtres dynamiques.
	
- Medecins : 
	1-Peut créer des comptes patients mais doit demander à l’administrateur pour qu’on les lui attribue. 
	2-Le médecin peut crud les patients qui lui sont attribués. 
	3-Il peut voir l’historique des informations remplies par les patients qu’il suit dans un tableau possédant des filtres dynamiques
	
- Patient :
	1- Peut remplir le ou les formulaires sur la plateforme. 
	2- Il peut voir l’historique de ses informations remplies dans un tableau possédant des filtres dynamiques.
	
schéma fonctionnel : 
![Texte alternatif](Projet_DoctoLib_Django_SchemaF.png)

- Authentifications :
	1- Chaque acteur doit s’authentifier sur la plateforme. 
	2- Le patient et le médecin reçoivent un email avec les éléments permettant de s’authentifier. 
	3- Lors de leur 1ère connexion, ils doivent modifier leur mot de passe.
		
- La base de données :
	1- SQLite, en se basant sur les informations du formulaires.
	2- Deux formulaires sont intégré avec une périodicité choisie par le médecin.
	
- Test unitaire : 
	1- Effectuer des tests unitaires sur l'application sur les fonctions les plus inportantes

- un CSS
	
Rendu : 
	1- un fichier README.md contenant les instructions d’installation ;
	2- Une notice sur la gestion et la protection de données à caractère personnels que devront signer le patient et le médecin ;
	3- le fichier SQLite (le système de base de données en Django) avec des données de test ainsi que les informations de connexion au site afin que je puisse l’utiliser et le tester ;
	4- le code de l’application

## Compétences visées:

- Concevoir une base de données analytique avec l’approche orientée requêtes en vue de la mise à disposition des données pour un traitement analytique ou d’intelligence artificielle 

- Programmer l’import de données initiales nécessaires au projet en base de données, afin de les rendre exploitables par un tiers, dans un langage de programmation adapté et à partir de la stratégie de nettoyage des données préalablement définie 

- Préparer les données disponibles depuis la base de données analytique en vue de leur utilisation par les algorithmes d’intelligence artificielle

- Concevoir le programme d’intelligence artificielle adapté aux données disponibles afin de répondre aux objectifs fonctionnels du projet, à l’aide des algorithmes, outils et méthodes standards, notamment de machine learning et de deep learning

- Développer le programme d’intelligence artificielle selon les données du projet et les éléments de conception définis, en exploitant les algorithmes et les outils standards couramment utilisés dans le domaine

- Développer l’interaction entre les fonctionnalités de l’application et l’intelligence artificielle dans le respect des objectifs visés et des bonnes pratiques du domaine.

- Modifier les paramètres et composants de l’intelligence artificielle afin d’ajuster aux objectifs du projet les capacités fonctionnelles de l’algorithme à l’aide de techniques d’optimisation.

- Analyser un besoin en développement d’application mettant en oeuvre des techniques d'intelligence artificielle afin de produire les éléments de réponses techniques

- Concevoir une base de données relationnelle à l’aide de méthodes standards de modélisation de données

- Développer le back-end de l’application d’intelligence artificielle dans le respect des spécifications fonctionnelles et des bonnes pratiques du domaine.

- Développer le front-end de l’ application d’intelligence artificielle à partir de maquettes et du parcours utilisateur⋅rice, dans le respect des objectifs visés et des bonnes pratiques du domaine.

- Communiquer avec les parties prenantes afin de rendre compte de l'avancement du projet en mettant en oeuvre les canaux de communication nécessaires.

- Planifier le travail à effectuer individuellement et en équipe afin d’optimiser le travail nécessaire à l’atteinte de l’objectif visé.

- Définir le périmètre d’un problème rencontré en adoptant une démarche inductive afin de permettre la recherche de solution.

- Rechercher de façon méthodique une ou des solutions au problème rencontré afin de retenir une solution adaptée au contexte.

- Partager la solution adoptée en utilisant les moyens de partage de connaissance ou de documentation disponibles afin de contribuer au développement de la connaissance de l’entreprise.

- Présenter un travail réalisé en synthétisant ses résultats, sa démarche et en répondant aux questions afin de le restituer au commanditaire.


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

## Base de données SQLite 
Schéma de la BDD : 
![Texte alternatif](schema_BDD_doctotolib_clementine.png)

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

## Améliorations et nouvelles fonctionnalités pour les prochaines versions :
- Système d'alertes permettront d’informer le médecin si des valeurs critiques ou incohérentes ont été renseignées.

- Analyse de données : 
	1- Une page permet à l’administrateur et au médecin de rechercher des corrélations faire des régressions, classifications,et du clustering et enfin de faire une analyse de série temporelle et du NLP.
	2- Des graphiques interactifs avec filtres.
	3- Lancer des modèles en sélectionnant des données, de les sauvegarder et de vérifier leurs performances à un instant T. 

- Système d’ETL permettant de mettre les données en formes pour la Chine, les États Unis, le Brésil, l'Afrique du Sud et la France.

"""