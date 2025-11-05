import unittest
from unittest import TestCase, mock
from setup import _apply_patch
import inspect
import re
import ast


class TestApplyPatch(TestCase):
    def setUp(self):
        # Set up any prerequisites for the tests
        self.patch = """--- original
+++ modified
@@ -1,3 +1,3 @@
 Hello
-world
+earth
"""
        self.original_text = "Hello\nworld\n"
        self.modified_text = "Hello\nearth\n"


        source = inspect.getsource(_apply_patch)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_keepends(self):
        matched_keepends = re.search(r'keepends=True', self.source)
        self.assertIsNotNone(matched_keepends)

    def test_change_variable_type(self):
        # Test for adaptation 0: Change Variable Type
        result = _apply_patch(self.original_text, self.patch)
        self.assertEqual(result, self.modified_text, "The patched text should match the modified text.")

    def test_exception_handling_refinement(self):
        # Test for adaptation 2: Exception Handling Refinement
        # Test the exception is raised with the correct message when encountering an invalid line
        invalid_patch = "Invalid patch line\n"
        with self.assertRaises(ValueError) as context:
            _apply_patch(self.original_text, invalid_patch)
        self.assertTrue("Invalid line in patch" in str(context.exception))

    def test_extend_method_used(self):
        patch = """--- original
+++ modified
@@ -1,3 +1,3 @@
 Hello
-world
+earth
"""
        original_text = "original"

        with mock.patch('builtins.list') as MockList:
            mock_list_instance = MockList.return_value
            # Set up the mock to record calls to extend
            mock_list_instance.extend = mock.MagicMock()
            
            # Call the original function
            result = _apply_patch(original_text, patch)
            
            # Now we can assert that extend was called on our mock list
            mock_list_instance.extend.assert_called()

    def test_rename_function(self):
        import setup
        self.assertTrue(callable(_apply_patch))
        self.assertNotIn('apply_patch', setup.__dict__)

    def test_update_variable_name(self):
        match_var_name = re.search(r'_hdr_pat', self.source)
        self.assertIsNone(match_var_name)


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
        if isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body[0].value.value = ""
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Skip over async function decorators
        node.decorator_list = []
        self.generic_visit(node)

if __name__ == '__main__':
    unittest.main()
