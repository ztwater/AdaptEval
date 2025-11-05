def simplifyGraph(G):
    ''' Loop over the graph until all nodes of degree 2 have been removed and their incident edges fused '''

    g = G.copy()

    while any(degree==2 for _, degree in g.degree):

        g0 = g.copy() #<- simply changing g itself would cause error `dictionary changed size during iteration` 
        for node, degree in g.degree():
            if degree==2:

                if g.is_directed(): #<-for directed graphs
                    a0,b0 = list(g.in_edges(node))[0]
                    a1,b1 = list(g.out_edges(node))[0]

                else:
                    edges = g.edges(node)
                    edges = list(edges.__iter__())
                    a0,b0 = edges[0]
                    a1,b1 = edges[1]

                e0 = a0 if a0!=node else b0
                e1 = a1 if a1!=node else b1

                g0.remove_node(node)
                g0.add_edge(e0, e1)
        g = g0

    return g
