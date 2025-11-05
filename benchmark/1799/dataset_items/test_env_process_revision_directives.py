import re
import unittest
import inspect
import ast
from unittest.mock import MagicMock, patch

# Define a dummy MigrationContext and MigrationScript for testing purposes
from alembic.migration import MigrationContext
from alembic.operations.ops import MigrationScript

from env import process_revision_directives
 
class TestProcessRevisionDirectives(unittest.TestCase):
    def setUp(self):
        self.migration_script = MagicMock()
        self.context = MagicMock()
        self.context.config = "config"

        source = inspect.getsource(process_revision_directives)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)

    def test_add_type_annotations(self):
        annotations = process_revision_directives.__annotations__
        self.assertIn("context", annotations)
        self.assertIn("directives", annotations)
        self.assertEqual(annotations["context"], MigrationContext)
        self.assertEqual(annotations["directives"], list[MigrationScript])

    def test_change_string_formatting(self):
        matched_old = re.search(r'[\'\"]\.format\(', self.source)
        matched_new = re.search(r'f[\'\"].+[\'\"]', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)

    def test_remove_identifiers(self):
        signature = inspect.signature(process_revision_directives)
        parameters = signature.parameters
        self.assertNotIn("revision", parameters) 
        self.assertIn("_", parameters) 
    
    @patch('env.ScriptDirectory.from_config')
    def test_first_migration(self, mock_from_config):
        # Simulate no head revision for the first migration
        mock_from_config.return_value.get_current_head.return_value = None

        # Call the function with the mocked context and directives
        process_revision_directives(self.context, None, [self.migration_script])

        # Assert that the revision ID is set to 0001
        self.assertEqual(self.migration_script.rev_id, '0001')

    @patch('env.ScriptDirectory.from_config')
    def test_migration_with_head_revision(self, mock_from_config):
        # Simulate a head revision with ID '0005'
        mock_from_config.return_value.get_current_head.return_value = '0005'

        # Call the function with the mocked context and directives
        process_revision_directives(self.context, None, [self.migration_script])

        # Assert that the revision ID is incremented to 0006
        self.assertEqual(self.migration_script.rev_id, '0006')

    @patch('env.ScriptDirectory.from_config')
    def test_migration_with_non_zero_head_revision(self, mock_from_config):
        # Simulate a head revision with ID '0095'
        mock_from_config.return_value.get_current_head.return_value = '0095'

        # Call the function with the mocked context and directives
        process_revision_directives(self.context, None, [self.migration_script])

        # Assert that the revision ID is incremented to 0096
        self.assertEqual(self.migration_script.rev_id, '0096')


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
