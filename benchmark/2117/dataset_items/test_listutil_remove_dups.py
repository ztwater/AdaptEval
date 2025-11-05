import unittest
import inspect

from listutil import remove_dups


class TestRemoveDups(unittest.TestCase):
    def test_rename_method(self):
        import listutil
        self.assertTrue(callable(remove_dups))
        self.assertNotIn('f7', listutil.__dict__)

    def test_add_type_annotations(self):
        annotations = remove_dups.__annotations__
        self.assertIn('seq', annotations)
        self.assertEqual(annotations['seq'], list, "Parameter 'seq' should be of type 'list'.")

    def test_remove_dups_basic(self):
        """测试基本去重功能。"""
        self.assertEqual(remove_dups([1, 2, 2, 3]), [1, 2, 3])

    def test_remove_dups_preserve_order(self):
        """测试原始顺序是否被保留。"""
        self.assertEqual(remove_dups([3, 1, 2, 2, 3]), [3, 1, 2])

    def test_remove_dups_empty_list(self):
        """测试空列表。"""
        self.assertEqual(remove_dups([]), [])

    def test_remove_dups_no_duplicates(self):
        """测试没有重复的列表。"""
        self.assertEqual(remove_dups([1, 2, 3]), [1, 2, 3])

    def test_remove_dups_all_duplicates(self):
        """测试所有元素都是重复的列表。"""
        self.assertEqual(remove_dups([1, 1, 1, 1]), [1])

    def test_remove_dups_mixed_types(self):
        """测试包含混合数据类型的列表。"""
        self.assertEqual(remove_dups([1, '1', 1, '1', 2]), [1, '1', 2])

    def test_remove_dups_large_input(self):
        """测试大输入列表以检查性能。"""
        input_list = list(range(10000)) + list(range(5000))
        self.assertEqual(remove_dups(input_list), list(range(10000)))

if __name__ == '__main__':
    unittest.main()
