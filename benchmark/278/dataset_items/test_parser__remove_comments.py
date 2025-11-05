import unittest
import re
import inspect
import ast
import types

from parser import _remove_comments

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


class TestRemoveComments(unittest.TestCase):

    def setUp(self):
        source = inspect.getsource(_remove_comments)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

        self.remove_comments = lambda string: _remove_comments(string)

    def test_single_line_comment(self):
        self.assertEqual(
            self.remove_comments("int x = 5; // This is a single line comment"),
            "int x = 5; "
        )

    def test_multiline_comment(self):
        self.assertEqual(
            self.remove_comments("/* This is a multiline comment\n"
                                 "spanning several lines */ int x = 5;"),
            "\n int x = 5;"
        )

    def test_comment_with_newline(self):
        self.assertEqual(
            self.remove_comments("void foo() { /* Does nothing */\n"
                                 "    // Does nothing\n}"),
            "void foo() { \n    \n}"
        )

    def test_comment_inside_string(self):
        self.assertEqual(
            self.remove_comments('char* str = "/* This is not a comment */";'),
            'char* str = "/* This is not a comment */";'
        )

    def test_comment_following_code(self):
        self.assertEqual(
            self.remove_comments("int x = 5; // Assigns 5 to x\n"
                                 "int y = 10;"),
            "int x = 5; \n"
            "int y = 10;"
        )

    def test_no_comments(self):
        self.assertEqual(
            self.remove_comments("int x = 5;\nint y = 10;"),
            "int x = 5;\nint y = 10;"
        )

    def test_multiple_comments(self):
        self.assertEqual(
            self.remove_comments("/* First comment */ int x = 5; // Inline comment\n"
                                 "/* Second comment */"),
            " int x = 5; \n"
        )

    def test_comments_with_newline_in_string(self):
        self.assertEqual(
            self.remove_comments('char* str = "This is not a comment\n'
                                 'and neither is this /* nor this */";'),
            'char* str = "This is not a comment\n'
            'and neither is this /* nor this */";'
        )

    def test_comments_preserve_newline_count(self):
        self.assertEqual(
            self.remove_comments("/* First line\n"
                                 "Second line */ int x = 5;"),
            "\n "
            "int x = 5;"
        )

    def test_add_type_annotations(self):
        annotations = _remove_comments.__annotations__
        self.assertIn('string', annotations)
        self.assertEqual(annotations['string'], str)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], str)

    def test_rename_function(self):
        pass

    def test_refactoring(self):
        matched_walrus = re.search(r'comment\s*:=\s*match\.group\(2\)', self.source)
        self.assertIsNotNone(matched_walrus)

    def test_add_type_annotations_child(self):
        # nested_func = None
        # for const in _remove_comments.__code__.co_consts:
        #     if isinstance(const, types.CodeType):
        #         # Check if the function is the nested function
        #         if const.co_name == "_replacer":
        #             nested_func = const
        #             break
        matched_annotations = re.search(r'def\s+_replacer\(match:\s*re\.Match\)\s*->\s*str:', self.source)
        self.assertIsNotNone(matched_annotations)


if __name__ == '__main__':
    unittest.main()