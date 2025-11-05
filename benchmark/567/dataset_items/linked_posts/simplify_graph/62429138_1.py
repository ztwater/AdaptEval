>>> G = nx.DiGraph()
>>> G.add_edges_from([(1,2),(2,3)])
>>> list(G.edges)
[(1, 2), (2, 3)]

>>> g = simplifyGraph(G)
>>> list(g.edges)
[(1, 3)]
