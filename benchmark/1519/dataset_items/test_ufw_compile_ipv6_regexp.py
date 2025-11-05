import unittest
from ufw import compile_ipv6_regexp
import os
import re
import ast
import inspect


def extract_method_code(file_content, tree, method_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            start_line = node.lineno - 1  # Lines in ast are 1-indexed
            end_line = node.end_lineno  # End line (only available in Python 3.8+)
            method_lines = file_content.splitlines()[start_line:end_line]
            method_code = '\n'.join(method_lines)
            return method_code


class TestCompileIpv6Regexp(unittest.TestCase):
    def setUp(self):
        src_path = os.path.join(os.path.dirname(__file__), 'ufw.py')
        with open(src_path, 'r', encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = extract_method_code(source, tree, 'compile_ipv6_regexp')

    def test_filter_line_that_contains_ipv6(self):
        reg = compile_ipv6_regexp()
        self.assertTrue(reg.search("### tuple ### allow udp 5353 ::/0 any ff02::fb in") is not None)
        self.assertTrue(reg.search("### tuple ### allow udp 5353 0.0.0.0/0 any 224.0.0.251 in") is None)
        self.assertTrue(reg.search("### tuple ### allow any 23 :: any ::/0 in") is not None)
        self.assertTrue(reg.match("ff02::fb") is not None)
        self.assertTrue(reg.match("224.0.0.251") is None)
        self.assertTrue(reg.match("::") is not None)

    def test_function_wrap(self):
        self.assertTrue(callable(compile_ipv6_regexp))

    def test_return_compiled_pattern(self):
        pattern = compile_ipv6_regexp()
        self.assertIsInstance(pattern, re.Pattern)

    def test_regex_split(self):
        match_concat = re.search(r'\s*\+=\s*r[\'\"].+[\'\"]', self.source, re.DOTALL)
        self.assertIsNotNone(match_concat)

    def test_valid_ipv6(self):
        pattern = compile_ipv6_regexp()
        valid_ipv6_addresses = [
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "::1",
            # "::ffff:255.255.255.255", #BUGFIX
            "::2:3:4:5:6:7:8",
            # "1:2::4:5:6:7:8",  #BUGFIX
            "1:2:3:4:5:6:7:8"
        ]
        for address in valid_ipv6_addresses:
            with self.subTest(address=address):
                self.assertEqual(pattern.match(address).group(), address)

    def test_invalid_ipv6(self):
        pattern = compile_ipv6_regexp()
        invalid_ipv6_addresses = [
            "fe80::1ff:fe23:4567:890a",
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234",
            "2001:db8::2::1",
            "2001:db8:85a3::8a2e:370g:7334",
            "12345::",
            "2001:db8::2:1"
        ]
        for address in invalid_ipv6_addresses:
            with self.subTest(address=address):
                matcher = pattern.match(address)
                if not matcher is None:
                    self.assertNotEqual(pattern.match(address).group(), address)


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


if __name__ == "__main__":
    unittest.main()