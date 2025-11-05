import unittest
import numpy as np
import ast
import inspect
import re

from _qmc import primes_from_2_to

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

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestPrimesFrom2To(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(primes_from_2_to)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_type_annotations(self):
        annotations = primes_from_2_to.__annotations__
        self.assertIn('n', annotations)
        self.assertEqual(annotations['n'], int)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], np.ndarray)

    def test_function_name(self):
        # Test for id 1: Update Function Name
        # This test is more about the usage rather than the function name itself
        result = primes_from_2_to(10)
        self.assertEqual(len(result), 4)
        self.assertListEqual(list(result), [2, 3, 5, 7])

    def test_use_np_alias(self):
        matched_numpy = re.search(r'numpy', self.source)
        matched_np = re.search(r'np', self.source)
        self.assertIsNone(matched_numpy)
        self.assertIsNotNone(matched_np)

    def test_remove_prime_check(self):
        matched_check = re.search(r'if sieve\[i]:', self.source)
        self.assertIsNone(matched_check)

    def test_primes_large_range(self):
        # Test for a larger range to check the efficiency and correctness of the sieve
        primes = primes_from_2_to(100)
        self.assertEqual(len(primes), 25)  # There are 25 primes below 100
        self.assertTrue(all(is_prime(x) for x in primes))  # Assuming a function is_prime() that checks primality

if __name__ == '__main__':
    unittest.main()
