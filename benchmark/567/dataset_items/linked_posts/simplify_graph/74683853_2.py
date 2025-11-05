g = nx.DiGraph()
g.add_edge("node_one", "node_two")
g.add_edge("node_two", "node_three")
res = simplify_graph_with_predicate(g, lambda node: "two" in node)
print(res.edges) # output: [('node_one', 'node_three')]
