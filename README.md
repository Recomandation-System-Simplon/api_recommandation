# api_recommandation


# Librairie_recommandation
Projet de recommandation de livres pour un libraire



# Installation
```console
git clone https://github.com/Recomandation-System-Simplon/api_recommandation.git
cd Librairie_recommandation
```

Si anaconda installer sur votre machine :
```console
conda deactivate
```
En suite création de l'environnement de travail :
```console

python -m venv venv
```
Sur Windows exécutez :
```console
venv/Scripts/activate
```
ou sur Linux :
```console
source venv/bin/activate
```
Ensuite finir par :
```console
pip install -r requirements.txt
```


# Configuration
Ouvrir le fichier `exemple_config.json` et remplacer les valeurs par défaut par celle de votre environnement. Copier ensuite ce fichier dans un dossier instance et le renommer config.json.
```console
mkdir instance
cp exemple_config.json instance/config.json
```
Ensuite exécuter les commandes de configuration pour la BDD:
```console
flask db init
flask db migrate
flask db upgrade
flask insert-db
```






# Docker
Si vous voulez vous éviter toutes les instructions précédentes, il est conseillé d'utiliser Docker.

## Liens vers un tutoriel d'installation de Docker
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-fr
## Lien vers un tutoriel d'installation de Docker-compose
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-fr#:~:text=%C3%89tape%201%20-%20Installation%20de%20Docker%20Compose

## Configuration
Il faut configurer les variables environnements de Postgres dans un fichier .env à placer à la racine de l'application (renommer le fichier `.env.exemple` en `.env` suffit amplement) :
```console
cp .env.exemple .env
```
## Construire et exécuter l'image docker :
```console
docker-compose up -d
```