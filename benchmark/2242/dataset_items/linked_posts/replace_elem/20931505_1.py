for elem in list(tree.getiterator('pre')):
    parent = parent_map[elem]
    wrap_elem(parent, elem)
