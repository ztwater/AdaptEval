import unittest
import inspect
import ast
import re
from common import haversine  # Replace 'your_module' with the name of your module where haversine is defined

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

class TestHaversine(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(haversine)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_known_distance(self):
        # Test with known coordinates and expected distance
        # For example, the distance between (0, 0) and (0, 1) should be approximately 111 km (at the equator)
        self.assertAlmostEqual(haversine((0, 0), (0, 1)),  111.195, places=2)

    def test_anti_podal_points(self):
        # Antipodal points are on exact opposite sides of the Earth
        # The distance should be approximately the diameter of the Earth
        self.assertAlmostEqual(haversine((0, 0), (180, 0)), 20015.086, places=2)

    def test_same_point(self):
        # The distance between a point and itself should be 0
        self.assertEqual(haversine((40.7128, -74.0060), (40.7128, -74.0060)), 0)

    def test_invalid_input(self):
        # Test the function with invalid input, such as non-numeric values
        with self.assertRaises(TypeError):
            haversine(('not', 'lat'), ('not', 'lon'))

    def test_high_latitude(self):
        # Test with points near the poles
        self.assertEqual(haversine((85, 0), (85, 1)),111.19492664455873,0)
        self.assertTrue(0 <= haversine((85, 0), (85, 1)) <= 112.0)

    def test_large_longitude_difference(self):
        # Test with a large difference in longitude
        self.assertEqual(haversine((0, 0), (359, 0)),111.19492664455905,0)
        self.assertTrue(0 <= haversine((0, 0), (359, 0)) <= 112.0)

    def test_math_sin_string_updates(self):
        matched_old = re.search(r'[^.\w]sin\(', self.source)
        matched_new = re.search(r'\bmath\.sin\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_math_cos_string_updates(self):
        matched_old = re.search(r'[^.\w]cos\(', self.source)
        matched_new = re.search(r'\bmath\.cos\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_math_asin_string_updates(self):
        matched_old = re.search(r'[^.\w]asin\(', self.source)
        matched_new = re.search(r'\bmath\.asin\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_math_sqrt_string_updates(self):
        matched_old = re.search(r'[^.\w]sqrt\(', self.source)
        matched_new = re.search(r'\bmath\.sqrt\(', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_math_radians_string_updates(self):
        matched_old = re.search(r'[^.\w]radians', self.source)
        matched_new = re.search(r'\bmath\.radians', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_update_parameters(self):
        parameters = inspect.signature(haversine).parameters
        self.assertEqual(len(parameters), 2)
        self.assertEqual(len(list(parameters)[0]), 2)
        self.assertEqual(len(list(parameters)[1]), 2)

if __name__ == '__main__':
    unittest.main()