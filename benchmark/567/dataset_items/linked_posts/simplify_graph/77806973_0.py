import networkx as nx

g = nx.DiGraph()
g.add_edges_from([(1,2),(2,3),(1,3),(3,4),(2,4)])

node = 2

for in_src, _ in g.in_edges(node):
    for _, out_dst in g.out_edges(node):
        g.add_edge(in_src, out_dst)

g.remove_node(node)

print(g.edges)

