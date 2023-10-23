# Projet Apprentissage Automatique - SNCF - TD1 groupe 1

## Étudiants :

- DUBOIS Jean-Baptiste
- DOUYSSET Martin
- BENCHETRIT Yaniv
- COLINET Robin

## Sujet

- Lien vers le sujet du projet [ici](https://centralesupelec.edunao.com/pluginfile.php/320881/course/section/48479/SNCF.docx).
- Lien de téléchargement de la data [ici](https://www.data.gouv.fr/fr/datasets/r/91fe399d-cafa-4e72-8ba3-56d8717fdad4).

## Setup

1. Cloner le repository en local.
   ```bash
   git clone https://github.com/robincolinet/sncf_td1_gr1.git
   ```
2. Télécharger la data puis la placer sous le nom 'data.csv' à la racine du projet.

## Fichiers

Description succinte de l'organisation du projet:

1. data_exploration.ipynb : visualisations préliminaires de la donnée de travail
2. comparaison_encodings.ipynb : comparaisons des preprocessings/représentation des données
3. comparaison_modèles_regression.ipynb : benchmark de plusieurs modèles de régression multivariée avec optimisation par Randomized Search
4. moyennes_glissantes.ipynb : étude d'impact d'une prise en compte basique de la temporalité des données
5. preprocessing.py, clustering.py : fichiers supports de fonctions
