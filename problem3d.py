from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import numpy as np

def spectral_clustering(G, num_clusters=2):
    """
    Applies spectral clustering using the normalized graph Laplacian.
    
    Parameters:
        G (networkx.Graph): Input graph (assumed undirected).
        num_clusters (int): Desired number of clusters.
    
    Returns:
        communities (List[Set]): List of node sets representing clusters.
    """
    # Step 1: Compute the normalized Laplacian matrix
    L = nx.normalized_laplacian_matrix(G).todense()

    # Step 2: Compute the first 'k' eigenvectors (smallest eigenvalues)
    eigvals, eigvecs = np.linalg.eigh(L)  # چون ماتریس L متقارن است، eigh مناسب‌تر است

    # Step 3: انتخاب eigenvectors متناظر با کوچک‌ترین k مقدار ویژه
    k_smallest_eigvecs = eigvecs[:, :num_clusters]

    # Step 4: نرمال‌سازی سطرها (برای خوشه‌بندی بهتر)
    normed_features = normalize(k_smallest_eigvecs)

    # Step 5: اعمال KMeans روی eigenvectors
    kmeans = KMeans(n_clusters=num_clusters, n_init=100)
    labels = kmeans.fit_predict(normed_features)

    # Step 6: ساخت خروجی به صورت لیست مجموعه‌ها
    communities = {}
    for node, label in zip(G.nodes(), labels):
        communities.setdefault(label, set()).add(node)

    return list(communities.values())
