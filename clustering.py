import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.cluster import KMeans
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def preprocess_clustering_par_lignes(data):
    data_clustering = data[data['annee'] < 2023]
    data_clustering = data_clustering.groupby('ligne').agg({'prct_cause_externe': 'mean',
                                            'prct_cause_infra': 'mean',
                                            'prct_cause_gestion_trafic': 'mean',
                                            'prct_cause_materiel_roulant': 'mean',
                                            'prct_cause_gestion_gare': 'mean',
                                            'prct_cause_prise_en_charge_voyageurs': 'mean'}).reset_index()
    return data_clustering

def recherche_meilleur_clustering_par_lignes(clustering_data):
    inertia = []

    # Define a range of cluster numbers to test
    cluster_range = range(1, 40)

    # Calculate inertia for each cluster number
    for n_clusters in tqdm(cluster_range, desc='Calcul des inerties'):
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(clustering_data[['prct_cause_externe', 'prct_cause_infra', 'prct_cause_gestion_trafic', 'prct_cause_materiel_roulant', 'prct_cause_gestion_gare', 'prct_cause_prise_en_charge_voyageurs']])
        inertia.append(kmeans.inertia_)

    # Plot the Elbow Method graph
    plt.plot(cluster_range, inertia, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal Number of Clusters')
    plt.show()

    # Create an empty list to store silhouette scores
    silhouette_scores = []

    # Define a range of cluster numbers to test
    cluster_range = range(2, 40)  # Start with a minimum of 2 clusters

    # Calculate silhouette scores for each cluster number
    for n_clusters in tqdm(cluster_range, desc='Calcul des Silhouette scores'):
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        cluster_labels = kmeans.fit_predict(clustering_data[['prct_cause_externe', 'prct_cause_infra', 'prct_cause_gestion_trafic', 'prct_cause_materiel_roulant', 'prct_cause_gestion_gare', 'prct_cause_prise_en_charge_voyageurs']])
        silhouette_avg = silhouette_score(clustering_data[['prct_cause_externe', 'prct_cause_infra', 'prct_cause_gestion_trafic', 'prct_cause_materiel_roulant', 'prct_cause_gestion_gare', 'prct_cause_prise_en_charge_voyageurs']], cluster_labels)
        silhouette_scores.append(silhouette_avg)

    # Plot the Silhouette Score graph
    plt.plot(cluster_range, silhouette_scores, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score for Optimal Number of Clusters')
    plt.show()