import unittest
import ast
import inspect
import re
import networkx as nx
from unittest.mock import patch

from utility import simplify_graph

class TestSimplifyGraph(unittest.TestCase):
    def setUp(self):
        self.graph1 = nx.DiGraph()
        self.graph1.add_edges_from([(1, 2), (2, 3)])
        self.graph2 = nx.Graph()
        self.graph2.add_edges_from([(1, 2), (2, 3), (3, 4)])
        self.graph3 = nx.DiGraph()
        self.graph3.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
        self.graph4 = nx.DiGraph()
        self.graph4.add_edges_from([(1, 2), (3, 4)])
        self.add_positions(self.graph1)
        self.add_positions(self.graph2)
        self.add_positions(self.graph3)
        self.add_positions(self.graph4)
        source = inspect.getsource(simplify_graph)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    @staticmethod
    def add_positions(G):
        # Assign a position to each node for testing purposes
        for node in G.nodes:
            G.nodes[node]['pos'] = (node % 2, node // 2)

    def test_simplify_directed_graph(self):
        g, pos, idx = simplify_graph(self.graph1)
        expected_graph = nx.DiGraph([(1, 3)])
        self.assertTrue(nx.is_isomorphic(g, expected_graph))
        self.assertEqual([pos[0], pos[1]], [g.nodes[i]['pos'] for i in idx])

    def test_simplify_undirected_graph(self):
        g, pos, idx = simplify_graph(self.graph2)
        expected_graph = nx.Graph([(1, 4)])
        self.assertTrue(nx.is_isomorphic(g, expected_graph))
        self.assertEqual([pos[0], pos[1]], [g.nodes[i]['pos'] for i in idx])

    def test_simplify_graph_with_multiple_degree2_nodes(self):
        g, pos, idx = simplify_graph(self.graph3)
        expected_graph = nx.DiGraph([(1, 5)])
        self.assertTrue(nx.is_isomorphic(g, expected_graph))
        self.assertEqual([pos[0], pos[1]], [g.nodes[i]['pos'] for i in idx])

    def test_simplify_graph_without_degree2_nodes(self):
        g, pos, idx = simplify_graph(self.graph4)
        expected_graph = self.graph4  # No nodes of degree 2 to simplify
        self.assertTrue(nx.is_isomorphic(g, expected_graph))

    def test_rename_func(self):
        from utility import simplify_graph

    def test_init_kept_lists(self):
        matched_list_init = re.search(r'\w+\s*=\s*(\[]|list\(\))', self.source)
        self.assertIsNotNone(matched_list_init)

    def test_update_else(self):
        matched_else = re.search(r'else:\s*\n\s+\w+\.append\(', self.source)
        self.assertIsNotNone(matched_else)

    def test_expand_return(self):
        result = simplify_graph(self.graph1)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)


class CommentRemover(ast.NodeVisitor):
    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str):
            # Preserve docstrings and regular strings
            self.generic_visit(node)
        elif isinstance(node.value, ast.Constant):
            # Skip over comments (which are stored as Constant nodes)
            pass
        else:
            self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Skip over function decorators
        node.decorator_list = []
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        self.generic_visit(node)

if __name__ == '__main__':
    unittest.main()