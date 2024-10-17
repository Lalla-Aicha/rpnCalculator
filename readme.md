Description du projet :
Ce projet consiste à développer une calculatrice en notation polonaise inverse (NPI) pour permettre à l'utilisateur d'effectuer des calculs en mode postfixé via une interface web. L'application est composée de :

Un backend FastAPI qui effectue les calculs NPI et sauvegarde les opérations dans une base de données. Les fichiers concernant le backend sont dans le dossier source

Un frontend React qui permet à l'utilisateur d'interagir avec la calculatrice et de télécharger un fichier CSV contenant l'historique des opérations. Les fichiers concernant le frontend sont dans le dossier rpn-calculator-frontend qui est dans le dossier source


## Installation

Clonez le dépôt et installez les dépendances :
git clone <url-du-repo>
cd KONE-AYOMI
pip install -r requirements.txt

## Lancer l'application localement
uvicorn main:app --reload


## Lancer l'application avec Docker
docker-compose up


##Connecter le frontend et le backend : Assurez-vous que le backend FastAPI est en cours d'exécution
##et que les requêtes sont envoyées à la bonne URL (http://localhost:8000/calculate/).


##Afin de lancer l'application React :
cd rpn-calculator-frontend
npm start


Lorsque le frontend React envoie des requêtes à l'API FastAPI, assurez-vous que le backend est en cours d'exécution sur http://localhost:8000.

## Utilisation
Pour calculer une expression en notation polonaise inverse (NPI) :
Entrez une expression NPI dans le champ texte (par exemple 3 4 + 2 *).
Cliquez sur le bouton "Calculer". Le résultat sera affiché en dessous du champ.

Téléchargement du fichier CSV : Cliquez sur le bouton "Télécharger le fichier CSV" pour récupérer un fichier CSV contenant l'historique des opérations effectuées avec leurs résultats.