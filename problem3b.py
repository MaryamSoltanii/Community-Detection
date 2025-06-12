import itertools

def girvan_newman_clustering(G, num_communities=2):
    comp_gen = girvan_newman(G)
    limited = itertools.islice(comp_gen, num_communities - 1)
    for communities in limited:
        pass
    return communities
