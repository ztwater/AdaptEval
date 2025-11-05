import inspect
import re
import unittest
import ast

from ctx___init__ import db, get_class_by_tablename

# Mock classes to simulate the database models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

# Add the mock classes to the registry manually for testing
db.Model._decl_class_registry = {
    'User': User,
    'Post': Post
}

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

class TestGetClassByTablename(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(get_class_by_tablename)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_class_found(self):
        """Test that the function returns the correct class when the table name is found."""
        user_class = get_class_by_tablename('user')
        self.assertEqual(user_class, User)

    def test_class_not_found(self):
        """Test that the function returns None when the table name is not found."""
        non_existent_class = get_class_by_tablename('non_existent')
        self.assertIsNone(non_existent_class)

    def test_another_class_found(self):
        """Test that the function returns the correct class for another table name."""
        post_class = get_class_by_tablename('post')
        self.assertEqual(post_class, Post)

    def test_rename_method(self):
        get_class_by_tablename('user')

    def test_change_class_registry(self):
        matched_base = re.search(r'\bBase\.registry\._class_registry', self.source)
        matched_db = re.search(r'\bdb\.Model\._decl_class_registry', self.source)
        self.assertIsNone(matched_base)
        self.assertIsNotNone(matched_db)

    def test_add_return_none(self):
        matched_return = re.search(r'return\s+None', self.source)
        self.assertIsNotNone(matched_return)

if __name__ == '__main__':
    unittest.main()

