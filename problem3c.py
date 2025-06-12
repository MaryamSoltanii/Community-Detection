import community as community_louvain  # Requires `python-louvain` package

def louvain_modularity_clustering(G):
    """
    Performs community detection using the Louvain method (modularity maximization).
    
    Args:
        G (networkx.Graph): Input graph.
    
    Returns:
        list: A list of sets, where each set represents a community of nodes.
    """
    # Compute the best partition using Louvain
    partition = community_louvain.best_partition(G)
    
    # Convert partition (dict) to a list of sets
    communities = {}
    for node, comm_id in partition.items():
        communities.setdefault(comm_id, set()).add(node)
    
    return list(communities.values())
