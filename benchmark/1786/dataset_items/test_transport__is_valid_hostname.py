import unittest
import re, inspect, ast

from transport import _is_valid_hostname

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


class TestIsValidHostname(unittest.TestCase):
    def setUp(self):
        self.valid_hostnames = [
            "example.com",
            "sub.example.com",
            "example123.com",
            "sub-domain.example.com"
        ]
        self.invalid_hostnames = [
            "example..com",
            "-example.com",
            "example-.com",
            "example!com",
            "1.2.3.4"
        ]
        source = inspect.getsource(_is_valid_hostname)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_type_annotations(self):
        annotations = _is_valid_hostname.__annotations__
        self.assertIn('hostname', annotations)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['hostname'], str)
        self.assertEqual(annotations['return'], bool)

    def test_rename_function(self):
        import transport
        self.assertTrue(callable(_is_valid_hostname))
        self.assertNotIn('is_valid_hostname', transport.__dict__)

    def test_length_check(self):
        seg1 = ".".join(["a" * 6] * 36) + ".a"  # len=253
        seg2 = seg1 + "aaa"  # len=256
        self.assertTrue(_is_valid_hostname(seg1))
        self.assertFalse(_is_valid_hostname(seg2))

    def test_var_name_changed(self):
        # Testing the refactoring changes is that the variable name has been changed
        matched_old = re.search(r'\blabels\s*=\s*', self.source)
        matched_new = re.search(r'\bparts\s*=\s*', self.source)
        new2 = re.search(r'for\s+x\s+in\s+parts', self.source)
        old2 = re.search(r'for\s+label\s+in\s+labels', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)
        self.assertIsNone(old2)
        self.assertIsNotNone(new2)

    def test_valid_hostnames(self):
        for hostname in self.valid_hostnames:
            self.assertTrue(_is_valid_hostname(hostname), f"Valid hostname failed: {hostname}")

    def test_invalid_hostnames(self):
        for hostname in self.invalid_hostnames:
            self.assertFalse(_is_valid_hostname(hostname), f"Invalid hostname passed: {hostname}")
            
 

if __name__ == '__main__':
    unittest.main()
