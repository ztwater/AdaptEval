def simplify_graph(G):
    """
    The simplifyGraph function simplifies a given graph by removing nodes of degree 2 and fusing their incident edges.
    Source:  https://stackoverflow.com/questions/53353335/networkx-remove-node-and-reconnect-edges

    :param G: A NetworkX graph object to be simplified
    :return: A tuple consisting of the simplified NetworkX graph object, a list of positions of kept nodes, and a list of indices of kept nodes.
    """

    g = G.copy()

    keept_node_pos = []
    keept_node_idx = []

    while any(degree == 2 for _, degree in g.degree):

        g0 = g.copy()  # <- simply changing g itself would cause error `dictionary changed size during iteration`
        for node, degree in g.degree():
            if degree == 2:

                if g.is_directed():  # <-for directed graphs
                    a0, b0 = list(g0.in_edges(node))[0]
                    a1, b1 = list(g0.out_edges(node))[0]

                else:
                    edges = g0.edges(node)
                    edges = list(edges.__iter__())
                    a0, b0 = edges[0]
                    a1, b1 = edges[1]

                e0 = a0 if a0 != node else b0
                e1 = a1 if a1 != node else b1

                g0.remove_node(node)
                g0.add_edge(e0, e1)
            else:
                keept_node_pos.append(g.nodes[node]['pos'])
                keept_node_idx.append(node)
        g = g0

    return g, keept_node_pos, keept_node_idx

