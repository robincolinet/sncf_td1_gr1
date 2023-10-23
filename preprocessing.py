import pandas as pd
import numpy as np

def load_data():
    data_path = 'data.csv'
    data = pd.read_csv(data_path, sep=';')
    return data

def preprocess_data(data):
    df = pd.DataFrame(data)
    # Interaction entre gares de départ et d'arrivée
    df['ligne'] = df['gare_depart'] + "-" + df['gare_arrivee']

    df['mois'] = df['date'].str.split('-').str[1]
    df = df.drop(['date'])

# One-Hot Encoding pour les colonnes catégorielles
def encoding_data(data, features_to_encode):
    data = pd.get_dummies(data, columns=features_to_encode);
    return data