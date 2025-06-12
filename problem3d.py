import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import networkx as nx

def spectral_clustering(G, num_clusters=2):
    """
    Performs community detection using spectral clustering (normalized Laplacian).
    
    Args:
        G (networkx.Graph): Input graph.
        num_clusters (int): Desired number of clusters (default: 2).
    
    Returns:
        list: A list of sets, where each set represents a community of nodes.
    """
    # Step 1: Compute the normalized Laplacian matrix
    L = nx.normalized_laplacian_matrix(G).todense()
    
    # Step 2: Compute eigenvectors of the Laplacian
    eigvals, eigvecs = np.linalg.eigh(L)
    
    # Step 3: Select the first `num_clusters` eigenvectors (smallest eigenvalues)
    k_smallest_eigvecs = eigvecs[:, :num_clusters]
    
    # Step 4: Normalize rows for better clustering
    normed_features = normalize(k_smallest_eigvecs)
    
    # Step 5: Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, n_init=100)
    labels = kmeans.fit_predict(normed_features)
    
    # Step 6: Convert labels to communities
    communities = {}
    for node, label in zip(G.nodes(), labels):
        communities.setdefault(label, set()).add(node)
    
    return list(communities.values())
