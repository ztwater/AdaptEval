def simplifyGraph(var_0):
''' Loop over the graph until all nodes of degree 2 have been removed and their incident edges fused '''

var_1 = var_0.copy()

while any(degree==2 for _, degree in var_1.degree):

    var_2 = var_1.copy() #<- simply changing g itself would cause error `dictionary changed size during iteration` 
    for node, degree in var_1.degree():
        if degree==2:

            if var_1.is_directed(): #<-for directed graphs
                a0,b0 = list(var_2.in_edges(node))[0]
                a1,b1 = list(var_2.out_edges(node))[0]

            else:
                var_3 = var_2.edges(node)
                var_3 = list(var_3.__iter__())
                a0,b0 = var_3[0]
                a1,b1 = var_3[1]

            var_4 = a0 if a0!=node else b0
            var_5 = a1 if a1!=node else b1

            var_2.remove_node(node)
            var_2.add_edge(var_4, var_5)
    var_1 = var_2

return var_1

