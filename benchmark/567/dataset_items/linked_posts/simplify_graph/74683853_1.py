g = nx.DiGraph()
g.add_edges_from([(1,2),(2,3)])
res = simplify_graph_with_predicate(g, lambda node: node == 2)
print(res.edges) # output: [(1,3)]
