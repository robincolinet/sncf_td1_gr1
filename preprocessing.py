import pandas as pd
import numpy as np

def load_data():
    data_path = 'data.csv'
    data = pd.read_csv(data_path, sep=';')
    return data

def creer_features_date(data):
    data['mois'], data['annee'] = data['date'].apply(lambda date: int(date.split('-')[1])),  data['date'].apply(lambda date: int(date.split('-')[0]))

def creer_feature_ligne(df):
    df['ligne'] = df['gare_depart'] + "-" + df['gare_arrivee']

# One-Hot Encoding pour les colonnes catégorielles
def encoding_data(data, features_to_encode):
    data = pd.get_dummies(data, columns=features_to_encode)
    return data

def frequency_encoding(train_data, test_data):
    # Frequency encoding des gares
    frequency_encoding = train_data['gare_depart'].value_counts(normalize=True)
    train_data['gare_depart_encoded'] = train_data['gare_depart'].map(frequency_encoding)
    train_data['gare_arrivee_encoded'] = train_data['gare_arrivee'].map(frequency_encoding)
    test_data['gare_depart_encoded'] = test_data['gare_depart'].map(frequency_encoding)
    test_data['gare_arrivee_encoded'] = test_data['gare_arrivee'].map(frequency_encoding)

    # Colonnes d'entrée
    features = ['annee', 'mois', 'gare_depart_encoded', 'gare_arrivee_encoded', 'nb_train_prevu','duree_moyenne']

    # Colonnes cible
    target = 'retard_moyen_arrivee'

    X_train=train_data[features]
    y_train=train_data[target]

    X_test=test_data[features]
    y_test=test_data[target]

    return X_train, y_train, X_test, y_test

def drop_pourcentages_incorrects(data):
    features_cause = [col for col in data.columns if col.startswith('prct')]
    somme_pourcentage=data[features_cause].sum(axis=1)
    data = data.loc[(somme_pourcentage >= 99.9) & (somme_pourcentage <= 100.1)]