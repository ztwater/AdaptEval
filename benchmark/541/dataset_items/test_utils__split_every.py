import re
import unittest
from itertools import islice
import ast
import inspect

from ctx_utils import _split_every


class TestSplitEvery(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(_split_every)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_empty_iterable(self):
        # Test with an empty iterable
        self.assertEqual(list(_split_every(3, [])), [])

    def test_single_chunk(self):
        # Test with an iterable that fits exactly in one chunk
        self.assertEqual(list(_split_every(3, [1, 2, 3])), [[1, 2, 3]])

    def test_multiple_chunks(self):
        # Test with an iterable that requires multiple chunks
        self.assertEqual(list(_split_every(2, [1, 2, 3, 4])), [[1, 2], [3, 4]])

    def test_chunk_size_one(self):
        # Test with a chunk size of one
        iterable = [1, 2, 3, 4]
        expected = [[1], [2], [3], [4]]
        self.assertEqual(list(_split_every(1, iterable)), expected)

    def test_large_chunk_size(self):
        # Test with a chunk size larger than the iterable
        self.assertEqual(list(_split_every(5, [1, 2, 3, 4])), [[1, 2, 3, 4]])

    def test_string_input(self):
        # Test with a string as input
        self.assertEqual(list(_split_every(2, "abcd")), [["a", "b"], ["c", "d"]])

    def test_generator_input(self):
        # Test with a generator as input
        def gen():
            for i in range(5):
                yield i

        self.assertEqual(list(_split_every(3, gen())), [[0, 1, 2], [3, 4]])

    def test_rename_function(self):
        from ctx_utils import _split_every

    def test_change_api_name(self):
        matched_old = re.search(r'[^.]islice\(', self.source)
        matched_new = re.search(r'\bitertools\.islice\(', self.source)
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
