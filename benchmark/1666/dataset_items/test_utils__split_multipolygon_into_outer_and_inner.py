import unittest
import shapely
from unittest.mock import MagicMock
import re, ast, inspect
from shapely import MultiPolygon, Polygon

from ctx_utils import _split_multipolygon_into_outer_and_inner


class TestSplitMultipolygonIntoOuterAndInner(unittest.TestCase):
    def setUp(self):
        # Set up a MultiPolygon with one Polygon and one MultiPolygon
        self.multi_polygon = MultiPolygon([
            Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
            Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)], holes=[[(1, 1), (1.2, 1), (1.2, 1.2), (1, 1.2)]])
        ])

        source = inspect.getsource(_split_multipolygon_into_outer_and_inner)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_single_polygon(self):
        # Test with a single Polygon
        poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
        exterior_coords, interior_coords = _split_multipolygon_into_outer_and_inner(poly)
        self.assertSequenceEqual(exterior_coords, [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)])
        self.assertEqual(interior_coords, [])

    def test_multi_polygon(self):
        # Test with a MultiPolygon
        exterior_coords, interior_coords = _split_multipolygon_into_outer_and_inner(self.multi_polygon)
        self.assertEqual(len(exterior_coords), 10)
        self.assertEqual(len(interior_coords), 5)
        self.assertSequenceEqual([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0), (0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5), (0.5, 0.5)], exterior_coords)
        self.assertSequenceEqual([(1.0, 1.0), (1.2, 1), (1.2, 1.2), (1, 1.2), (1.0, 1.0)], interior_coords)

    def test_empty_multi_polygon(self):
        # Test with an empty MultiPolygon
        empty_mp = MultiPolygon()
        exterior_coords, interior_coords = _split_multipolygon_into_outer_and_inner(empty_mp)
        self.assertEqual(exterior_coords, [])
        self.assertEqual(interior_coords, [])

    def test_unhandled_geometry_type(self):
        # Test with an unhandled geometry type
        with self.assertRaises(AttributeError):
            _split_multipolygon_into_outer_and_inner("not a geometry")

    def test_rename_function(self):
        import ctx_utils
        self.assertTrue(callable(_split_multipolygon_into_outer_and_inner))
        self.assertNotIn('extract_poly_coords', ctx_utils.__dict__)

    def test_add_type_annotations(self):
        annotations = _split_multipolygon_into_outer_and_inner.__annotations__
        self.assertEqual(annotations['geom'], MultiPolygon)

    def test_update_geometry_type_checking(self):
        class MockGeom(MagicMock):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._geom_type = 'Polygon'
                self._visit = 0

            @property
            def geom_type(self):
                self._visit += 1
                return self._geom_type

        mock_geom = MockGeom()
        mock_geom.exterior.coords = []
        mock_geom.interiors = []
        _split_multipolygon_into_outer_and_inner(mock_geom)
        self.assertEqual(mock_geom._visit, 2)

    def test_update_return_statement(self):
        results = _split_multipolygon_into_outer_and_inner(self.multi_polygon)
        self.assertEqual(len(results), 2)
        self.assertIsInstance(results[0], list)
        self.assertIsInstance(results[1], list)

    def test_update_exception_message_formatting(self):
        matched_old = re.search(r'ValueError\([\'|\"].+[\'|\"]\s*\+\s*.+\)', self.source, re.DOTALL)
        matched_new = re.search(r'ValueError\(\s*f\'|\"].+[\'|\"]\s*\)', self.source, re.DOTALL)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

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
