import networkx as nx
from networkx.algorithms.community import girvan_newman
import itertools

def girvan_newman_clustering(G, num_communities=2):
    """
    Performs community detection using the Girvan-Newman algorithm (edge betweenness).
    
    Args:
        G (networkx.Graph): Input graph.
        num_communities (int): Desired number of communities (default: 2).
    
    Returns:
        list: A list of sets, where each set represents a community of nodes.
    """
    # Generate communities using Girvan-Newman (returns an iterator over partitions)
    comp_gen = girvan_newman(G)
    
    # Get the first (num_communities - 1) partitions (since Girvan-Newman splits iteratively)
    limited = itertools.islice(comp_gen, num_communities - 1)
    
    # Extract the final partition
    for communities in limited:
        pass  # This loop runs until the last partition is reached
    
    return communities
