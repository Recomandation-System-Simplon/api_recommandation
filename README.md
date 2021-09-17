# api_recommandation


# Librairie_recommandation
Projet de recommandation de livres pour un libraire



# Installation
```console
git clone https://github.com/Recomandation-System-Simplon/Librairie_recommandation.git
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
flask db upgrade
flask insert-db
```