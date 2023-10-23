import pandas as pd
import numpy as np

def load_data():
    data_path = 'data.csv'
    data = pd.read_csv(data_path, sep=';')
    return data

def preprocess_data(data):
    data['mois'], data['annee'] = data['date'].apply(lambda date: date.split('-')[1]),  data['date'].apply(lambda date: date.split('-')[0])

def creer_feature_ligne(df):
    df['ligne'] = df['gare_depart'] + "-" + df['gare_arrivee']

# One-Hot Encoding pour les colonnes catégorielles
def encoding_data(data, features_to_encode):
    data = pd.get_dummies(data, columns=features_to_encode);
    return data