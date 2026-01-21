
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



