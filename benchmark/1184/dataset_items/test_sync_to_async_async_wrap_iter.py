import asyncio
import unittest
from unittest.mock import MagicMock, patch, call
from concurrent.futures import ThreadPoolExecutor
from typing import AsyncGenerator, Iterable, Optional
import re, ast, inspect

from sync_to_async import async_wrap_iter

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

class TestAsyncWrapIter(unittest.TestCase):
    def setUp(self):
        source = inspect.getsource(async_wrap_iter)
        tree = ast.parse(source)
        comment_remover = CommentRemover()
        comment_remover.visit(tree)
        self.source = ast.unparse(tree)
        self.loop = asyncio.get_event_loop()

    async def consume_async_gen(self, async_gen):
        results = []
        async for item in async_gen:
            results.append(item)
        return results

    def test_async_iteration_over_list(self):
        test_list = [1, 2, 3]
        async_gen = async_wrap_iter(test_list)
        results = self.loop.run_until_complete(self.consume_async_gen(async_gen))
        self.assertEqual(results, test_list)

    def test_async_iteration_propagates_exception(self):
        def raise_exception():
            raise ValueError("An error occurred")

        test_iterable = (raise_exception() for x in [1, 2, 3])
        async_gen = async_wrap_iter(test_iterable)

        with self.assertRaises(ValueError) as context:
            _ = self.loop.run_until_complete(self.consume_async_gen(async_gen))

        self.assertIn("An error occurred", str(context.exception))

    def test_async_iteration_with_thread_pool(self):
        test_list = [1, 2, 3]
        with ThreadPoolExecutor() as pool:
            async_gen = async_wrap_iter(test_list, pool)
            results = self.loop.run_until_complete(self.consume_async_gen(async_gen))
        self.assertEqual(results, test_list)

    # def test_async_wrap_iter_closes_pool_properly(self):
    #     pool = ThreadPoolExecutor()
    #     pool.shutdown = MagicMock()
    #     test_list = [1, 2, 3]
    #     async_gen = async_wrap_iter(test_list, pool)
    #     self.loop.run_until_complete(self.consume_async_gen(async_gen))
    #     pool.shutdown.assert_called_once()

    def test_add_type_annotations(self):
        annotations = async_wrap_iter.__annotations__
        self.assertEqual(annotations['return'], AsyncGenerator)
        self.assertEqual(annotations["it"], Iterable)
        self.assertEqual(annotations["pool"], Optional[ThreadPoolExecutor])

    def test_add_optional_parameter(self):
        parameters = inspect.signature(async_wrap_iter).parameters
        self.assertIn('pool', parameters)
        self.assertEqual(parameters['pool'].default, None)

    def test_loop_execution_logic_update(self):
        test_list = [1, 2, 3]
        with patch.object(self.loop, 'run_in_executor', MagicMock()) as mock_loop:
            async_gen = async_wrap_iter(test_list)
            self.consume_async_gen(async_gen)
            mock_loop.assert_called()

    def test_loop_execution_logic_update_str(self):
        matched_old = re.search(r'threading\.Thread\(\s*target\s*=\s*iter_to_queue\s*\)\.start\(\)', self.source)
        matched_new = re.search(r'loop\.run_in_executor\(\s*pool\s*,\s*iter_to_queue\s*\)', self.source)
        self.assertIsNone(matched_old)
        self.assertIsNotNone(matched_new)



if __name__ == '__main__':
    unittest.main()