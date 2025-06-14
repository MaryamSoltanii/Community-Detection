def build_representative_network(G, communities, dataset_name, method_name="Louvain"):
    import matplotlib.pyplot as plt

    # مرحله 1: اختصاص هر نود به یک جامعه
    node_to_comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node_to_comm[node] = i

    # مرحله 2: ایجاد گراف نماینده (گراف خوشه‌ها)
    R = nx.Graph()

    # افزودن نودهای نماینده خوشه‌ها
    for i, comm in enumerate(communities):
        R.add_node(i, size=len(comm))  # سایز نود = تعداد اعضا

    # مرحله 3: شمردن یال‌های بین خوشه‌ها
    for u, v in G.edges():
        cu = node_to_comm[u]
        cv = node_to_comm[v]
        if cu != cv:
            if R.has_edge(cu, cv):
                R[cu][cv]['weight'] += 1
            else:
                R.add_edge(cu, cv, weight=1)

    # مرحله 4: رسم گراف نماینده
    pos = nx.spring_layout(R, seed=42)
    sizes = [R.nodes[n]['size'] * 50 for n in R.nodes()]  # ضرب برای وضوح بیشتر
    weights = [R[u][v]['weight'] for u, v in R.edges()]

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(R, pos, node_size=sizes, node_color="skyblue", edgecolors='black')
    nx.draw_networkx_edges(R, pos, width=weights, alpha=0.7)
    nx.draw_networkx_labels(R, pos, labels={i: f"C{i+1}" for i in R.nodes()}, font_size=10)
    edge_labels = {(u, v): f"{R[u][v]['weight']}" for u, v in R.edges()}
    nx.draw_networkx_edge_labels(R, pos, edge_labels=edge_labels, font_size=8)

    plt.title(f"Representative Network ({method_name}) - {dataset_name}")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(f"{dataset_name}_{method_name}_representative_network.png")
    plt.show()
