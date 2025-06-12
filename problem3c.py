import community as community_louvain  # این همون python-louvain هست

def louvain_modularity_clustering(G):
    """
    Applies Louvain algorithm for community detection (modularity maximization).
    Returns a list of sets, each representing a community.
    """
    # اجرای الگوریتم Louvain
    partition = community_louvain.best_partition(G)

    # تبدیل دیکشنری به لیست از مجموعه‌ها
    communities = {}
    for node, comm_id in partition.items():
        communities.setdefault(comm_id, set()).add(node)

    return list(communities.values())
