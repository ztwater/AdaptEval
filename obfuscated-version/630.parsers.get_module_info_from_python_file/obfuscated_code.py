import ast
from collections import namedtuple

var_0 = namedtuple("Import", ["module", "name", "alias"])

def get_imports(var_1):
    with open(var_1) as fh:        
       var_2 = ast.parse(fh.read(), var_1)

    for node in ast.iter_child_nodes(var_2):
        if isinstance(node, ast.Import):
            var_3 = []
        elif isinstance(node, ast.ImportFrom):  
            var_3 = node.module.split('.')
        else:
            continue

        for n in node.names:
            yield var_0(var_3, n.name.split('.'), n.asname)
