import re
import ast
import unittest
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
from unittest.mock import patch, MagicMock
import inspect

from building import get_minimum_bounding_rectangle


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


class TestGetMinimumBoundingRectangle(unittest.TestCase):

    def setUp(self):
        # Sample building footprint data for testing
        coords1 = [(0, 0), (2, 0), (2, 2), (0, 2)]
        coords2 = [(1, 1), (4, 1), (4, 4), (1, 4)]
        polygon1 = Polygon(coords1)
        polygon2 = Polygon(coords2)
        self.nx2_mat = np.array([coords1, coords2])
        self.building_nodes = gpd.GeoDataFrame({'geometry': [polygon1, polygon2]})

        source = inspect.getsource(get_minimum_bounding_rectangle)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_bounding_rectangle_area(self):
        mbr_list = get_minimum_bounding_rectangle(self.building_nodes)
        for mbr, polygon in zip(mbr_list, self.building_nodes.geometry):
            self.assertTrue(mbr.buffer(1e-14).contains(polygon))
            self.assertAlmostEqual(mbr.area, polygon.minimum_rotated_rectangle.area, places=5)

    def test_empty_input(self):
        empty_building_nodes = gpd.GeoDataFrame({'geometry': []})
        mbr_list = get_minimum_bounding_rectangle(empty_building_nodes)
        self.assertEqual(mbr_list, [])

    def test_non_convex_input(self):
        coords = [(0, 0), (2, 0), (2, 2), (1, 1), (0, 2)]
        polygon = Polygon(coords)
        building_nodes = gpd.GeoDataFrame({'geometry': [polygon]})
        mbr_list = get_minimum_bounding_rectangle(building_nodes)
        self.assertEqual(len(mbr_list), 1)
        self.assertIsInstance(mbr_list[0], type(polygon))
        self.assertTrue(mbr_list[0].buffer(1e-14).contains(polygon))
        
    def test_param_type_change(self):
        coords = [(0, 0), (2, 0), (2, 2), (1, 1), (0, 2)]
        with self.assertRaises(AttributeError):
            get_minimum_bounding_rectangle(coords)
            
    def test_func_name_change(self):
        self.assertEqual(get_minimum_bounding_rectangle.__name__,'get_minimum_bounding_rectangle')

    def test_update_parameter(self):
        parameters = inspect.signature(get_minimum_bounding_rectangle).parameters
        self.assertIn('building_nodes', parameters)

    def test_modify_input_handling(self):
        # correctness of input type
        with self.assertRaises(AttributeError):
            get_minimum_bounding_rectangle(self.nx2_mat)

        # check convex_hull.exterior is invoked
        mock_exterior = MagicMock()
        # mock_exterior.__iter__.return_value = self.building_nodes.convex_hull.exterior

        with patch('geopandas.GeoDataFrame.convex_hull') as mock_convex_hull:
            # Configure the mock convex hull to return the mock exterior when accessed
            mock_convex_hull.exterior = mock_exterior
            # Create a mock GeoDataFrame with the mock convex hull
            mock_building_nodes = MagicMock()
            mock_building_nodes.convex_hull = mock_convex_hull

            result = get_minimum_bounding_rectangle(mock_building_nodes)
            # self.assertEqual(len(result), 2)

        # Assert that the convex hull was accessed as expected
        mock_building_nodes.convex_hull.exterior.__iter__.assert_called_once()

    def test_iterative_calculation(self):
        matched_iter_edge = re.search(r'edges\s*=\s*\[.*\]', self.source)
        matched_iter_angle = re.search(r'angles\s*=\s*\[.*\]', self.source)
        self.assertIsNotNone(matched_iter_edge)
        self.assertIsNotNone(matched_iter_angle)

    def test_mbr_list_init(self):
        matched_mbr_list = re.search(r'mbr_list\s*=\s*\[\]', self.source)
        self.assertIsNotNone(matched_mbr_list)

    def test_add_loop(self):
        matched_loop = re.search(r'for\s+[A-Za-z_]+,\s*[A-Za-z_]+\s+in\s+', self.source)
        self.assertIsNotNone(matched_loop)

    def test_list_append(self):
        # test whether append() is invoked (built-in method)
        matched_append = re.search(r'\.append\(.+\)', self.source)
        self.assertIsNotNone(matched_append)

        # check the result length and type
        mbr_list = get_minimum_bounding_rectangle(self.building_nodes)
        self.assertEqual(len(mbr_list), 2)
        self.assertIsInstance(mbr_list[0], Polygon)
        self.assertIsInstance(mbr_list[1], Polygon)

    def test_adapt_output(self):
        mbr_list = get_minimum_bounding_rectangle(self.building_nodes)
        self.assertIsInstance(mbr_list, list)
        self.assertIsInstance(mbr_list[0], Polygon)

if __name__ == '__main__':
    unittest.main()
