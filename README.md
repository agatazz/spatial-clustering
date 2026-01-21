
# Spatial Clustering: Seismic Zone Delineation

This project explores the application of **Spatially Constrained K-Means** and **Spectral Clustering on Spatial Graphs** to identify distinct seismic zones using earthquake hypocenter data.

The core challenge addressed here is that standard clustering algorithms treat geographic coordinates as independent variables, often resulting in fragmented or geologically nonsensical clusters. By applying spatial constraints and graph-based connectivity, we can delineate zones that respect the physical "skeleton" of tectonic fault lines.

## Basic informaiton

* **Coordinate Projection**: Transformation of Geodetic coordinates (Lat, Lon, Depth) into 3D Cartesian space  to ensure accurate distance calculations.
* **Spatially Constrained K-Means**: Implementation of feature weighting (alpha-scaling) to balance geographic proximity with earthquake magnitude.
* **Spectral Clustering**: Graph-based clustering using a **k-Nearest Neighbors (kNN) Spatial Graph** to identify non-spherical, "stringy" fault structures.
* **Weighted Affinity Matrices**: Integration of seismic magnitude into Spectral Clustering via an RBF-kernel masked by spatial adjacency.
* **Visualization**: Comparison of cluster results against known USGS fault line datasets.

## Tech Stack

* Python 
* **Scikit-Learn**: For `KMeans` and `SpectralClustering` implementations.
* **GeoPandas**: For geospatial data handling and overlaying fault lines.
* **NetworkX**: For visualizing the spatial graph connectivity "skeleton."
* **Matplotlib/Seaborn**: For 2D/3D data visualization and silhouette analysis.

## Dataset

The project uses earthquake records ([USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/)) containing:

* **Location**: Latitude, Longitude, and Depth (Hypocenter).
* **Attributes**: Magnitude, RMS travel time, and horizontal error.

## Methodology

### The Elbow Method
The Elbow Method was employed to identify the mathematical "bend" in cluster inertia, suggesting an optimal range for $K$. However, the final selection of 4 clusters was determined by balancing this mathematical heuristic with the statistical metrics (mean and variance) of the resulting groups to ensure physical and scientific relevance.

### Spatially-Weighted K-Means
This methodology uses a "Soft-Constraint" approach where geography is treated as an additional feature in a standard K-Means framework.
* **Feature Engineering:** The algorithm combines spatial coordinates ($x, y, z$) and aspatial attributes (magnitude) into a single 4D feature vector.
* **Data Normalization:** A `StandardScaler` is applied to all features. This is a critical step because coordinates and magnitudes exist on vastly different scales; scaling ensures Euclidean distances are calculated fairly across all dimensions.
* **Distance Metric:** The model uses Euclidean distance to identify spherical, compact clusters in the multi-dimensional feature space.

### Spatially-Constrained Spectral Clustering
This methodology uses a graph-based approach to prioritize local connectivity and handle complex cluster geometries that K-Means may miss.
* **Graph Construction (The Adjacency Matrix):** * **Spatial Constraint:** A `kneighbors_graph` is built using the $x, y, z$ coordinates to create a "skeleton" of the data where points are only connected if they are physical neighbors. 
    * **Attribute Similarity:** An RBF (Gaussian) Kernel is applied to the scaled magnitudes to measure value-based similarity.
* **Hybrid Affinity Matrix:** The methodology merges these components by multiplying the spatial graph by the magnitude similarity. This "masks" the data, ensuring the algorithm only evaluates magnitude similarity between points that are already geographic neighbors.
* **Mathematical Stability (Soft Connectivity):** To prevent "disconnected graph" errors—where isolated data "islands" break the Spectral embedding—a tiny constant ($\epsilon = 1e-5$) is added to the matrix. This ensures the Graph Laplacian remains stable while keeping the spatial constraint dominant.

### Evaluation Methods
Since these algorithms utilize different mathematical foundations, a variety of metrics were used to evaluate cluster quality:
* **Silhouette Score:** To measure cluster separation and cohesion.
* **Statistical Profiling:** Analysis of the **Mean**, **Standard Deviation**, and **Coefficient of Variation (CV)** for each cluster to verify internal consistency.
* **3D Visualization:** Geographic plotting of clusters and their centroids to confirm spatial logic.
* **Box Plots:** To visualize the spread and outliers of magnitude within each cluster.

## Installation & Usage

1. Clone the repo:
```bash
git clone https://github.com/agatazz/spatial-clustering.git

```

2. Install dependencies:
```bash
pip install scikit-learn geopandas networkx matplotlib pandas numpy

```

3. Run the main analysis:
```python
python main.py

```

---



