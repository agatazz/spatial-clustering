
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

### 1. Spatially Constrained K-Means

Standard K-Means is modified by scaling the spatial features  by a factor .

* High: Forces geographically compact "blobs."
* Low: Prioritizes attribute similarity (e.g., grouping all high-magnitude quakes together).

### 2. Spectral Clustering on Spatial Graphs

Unlike K-Means, Spectral Clustering views the data as a graph:

1. A **kNN Graph** is built where edges only exist between geographic neighbors.
2. The edges are weighted by magnitude similarity.
3. The **Graph Laplacian** is used to find "Min-Cuts," effectively identifying where seismic activity is physically decoupled.

## Results & Evaluation

* **Silhouette Analysis**: KMeans model achieved a Silhouette Score of **~0.72** with , indicating strong cluster separation.
* **Geological Validation**: Clusters were overlaid on known fault lines to verify that the mathematical groupings align with real-world tectonic structures.

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

### Future Exploration

* [ ] Implement **HDBSCAN** to separate seismic noise from active fault clusters.
* [ ] Test **SKATER** (Spatial 'K'luster Analysis by Tree Edge Removal) for strict contiguity.

