import unittest
import numpy as np
import cv2
import torch
import inspect
import ast
import astunparse
from unittest.mock import patch, Mock, DEFAULT, MagicMock
from copy import deepcopy
import re

from ctx_utils import get_warp_pyramid

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

class TestGetWarpPyramid(unittest.TestCase):

    def setUp(self):
        self.im1 = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.circle(self.im1, (40, 50), 20, (255, 255, 255), -1)  # A white circle in the first image
        cv2.rectangle(self.im1, (30, 30), (70, 70), (128, 128, 128), -1)
        # Apply a simple translation to create the second image
        translation_matrix = np.array([[1, 0, 10], [0, 1, 5]], dtype=np.float32)  # Move right by 10, down by 5
        self.im2 = cv2.warpAffine(self.im1, translation_matrix, (100, 100))
        self.nol = 3
        self.criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 100, 0.01)
        self.warp_mode = cv2.MOTION_EUCLIDEAN
        source = inspect.getsource(get_warp_pyramid)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source_no_comment = astunparse.dump(tree)

    def test_initialization_of_warp_matrix(self):
        warp = get_warp_pyramid(self.im1, self.im2, self.nol, self.criteria, self.warp_mode)
        expected_warp = np.array([[1, 0, 10], [0, 1, 5]], dtype=np.float32)
        # the error is as large as 0.1
        self.assertTrue(np.allclose(warp[:2, :], expected_warp, rtol=0.1, atol=0.2))

    def test_refactoring_variable_names(self):
        matched_old = re.search(r'img[12]|criteria[^_]', self.source_no_comment)
        self.assertIsNone(matched_old)

    def side_effect(self, *args, **kwargs):
        print(args, kwargs)
        self.assertIn('inputMask', kwargs)
        self.assertEqual(kwargs['inputMask'], None)
        self.assertIn('gaussFiltSize', kwargs)
        self.assertEqual(kwargs['gaussFiltSize'], 1)

    def test_addition_of_parameters_to_findTransformECC(self):
        return_warp = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float32)
        with patch('cv2.findTransformECC', return_value=(None, return_warp)) as mock_findtransformecc:
            warp = get_warp_pyramid(self.im1, self.im2, self.nol, self.criteria, self.warp_mode)
        _, actual_kwargs = mock_findtransformecc.call_args
        # Check if findTransformECC was called with the expected named parameters
        self.assertIn('inputMask', actual_kwargs)
        self.assertIn('gaussFiltSize', actual_kwargs)
        self.assertEqual(actual_kwargs['inputMask'], None)
        self.assertEqual(actual_kwargs['gaussFiltSize'], 1)

    def test_remove_timing_logic(self):
        # Test no timing logic in the code
        matched_time = re.search(r'timeit\.default_timer', self.source_no_comment)
        self.assertIsNone(matched_time)

    def test_remove_print_statements(self):
        matched_print = re.search(r'print', self.source_no_comment)
        self.assertIsNone(matched_print)

    def test_return_statement(self):
        warp = get_warp_pyramid(self.im1, self.im2, self.nol, self.criteria, self.warp_mode)
        self.assertIsInstance(warp, torch.Tensor)
        self.assertEqual(warp.shape, (2, 3))

if __name__ == '__main__':
    unittest.main()
