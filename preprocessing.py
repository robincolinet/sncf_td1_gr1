import pandas as pd
import numpy as np

def load_data():
    data_path = 'data.csv'
    data = pd.read_csv(data_path, sep=';')
    return data

def preprocess_time(data):
    data['date'] = pd.to_datetime(data['date'])
    data['annee'] = data['date'].apply(lambda time: time.year)
    data['mois'] = data['date'].apply(lambda time: time.month)
    data=data.drop('date', axis=1)
    return data

def preprocess_gares(data):
    data['ligne'] = data['gare_depart'] + "-" + data['gare_arrivee']