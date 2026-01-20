from sklearn.impute import KNNImputer
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import silhouette_score
import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


def visualize_3d(data, cluster_column='cluster'):
    fig = px.scatter_3d(data, x='longitude', y='latitude', z=-data['depth'],
                        color=cluster_column, 
                        size='mag',  # Earthquake magnitude dictates point size
                        hover_data=['id', 'place'],
                        title="Interactive Earthquake Clusters")

    # Adjust the 'aspectmode' so the depth doesn't look stretched
    fig.update_layout(scene=dict(aspectmode='data'))
    fig.show()


def visualize_3d_static(data,cluster_name):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    scatter = ax.scatter(data['longitude'], data['latitude'], -data['depth'], 
                        c=data[cluster_name], cmap='viridis', s=20, alpha=0.6)

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Depth (km)')
    plt.title('3D Cluster Visualization')
    plt.colorbar(scatter, label= 'Cluster ID')
    plt.show()




def visualize_graph_connectivity(data, adj_matrix, cluster_col):
    """
    data: Your clustered DataFrame
    adj_matrix: The weighted adjacency matrix used for Spectral Clustering
    cluster_col: The string name of your cluster column (e.g., 'spectral_cluster')
    """
    # Handle both Sparse and Dense matrices for the graph
    if hasattr(adj_matrix, "toarray"):
        G = nx.from_scipy_sparse_array(adj_matrix)
    else:
        G = nx.from_numpy_array(adj_matrix)

   
    pos = {i: (data.longitude.iloc[i], data.latitude.iloc[i]) for i in range(len(data))}

    plt.figure(figsize=(12, 8))

    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray')

    scatter = plt.scatter(data.longitude, data.latitude, 
                         c=data[cluster_col], 
                         cmap='viridis', 
                         s=50, 
                         edgecolors='black', 
                         zorder=5) # zorder=5 keeps points on top of the gray lines

    plt.colorbar(scatter, label='Cluster ID')
    plt.title(f"Spectral Connectivity Graph: {cluster_col}")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.savefig('spectral_graph_connectivity.png')


def calculate_sillouette_score(clustered_features, cluster_name, data):
    score = silhouette_score(clustered_features, data[cluster_name])
    print(f"Silhouette Score: {score}")


def visualize_clusters_on_known_fault_lines(data, crs, cluster_column):
   
    gdf_quakes = gpd.GeoDataFrame(
        data, geometry = gpd.points_from_xy(data.longitude, data.latitude), crs = crs
    )

    faults_url = "https://raw.githubusercontent.com/GEMScienceTools/gem-global-active-faults/master/geojson/gem_active_faults.geojson"
    gdf_faults = gpd.read_file(faults_url)

    fig, ax = plt.subplots(figsize=(12, 8))

    gdf_faults.plot(ax = ax, color = 'black', linewidth = 0.8, alpha = 0.5, label = 'Fault Lines')

    gdf_quakes.plot(ax = ax, column = cluster_column, cmap = 'viridis', markersize = 15, 
                    legend = True, label = 'Earthquake Clusters')

    plt.title("Earthquake Clusters vs. Known Fault Lines")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()