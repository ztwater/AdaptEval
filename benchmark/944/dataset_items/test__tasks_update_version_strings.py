import os
import re
import unittest
from _tasks import update_version_strings  # 确保只导入 update_version_strings

class TestUpdateVersionStrings(unittest.TestCase):

    def setUp(self):
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, "w") as f:
            f.write("version = \"1.2.3-alpha\"\n")
            f.write("another_version = \"4.5.6\"\n")
            f.write("ignore_me = \"1.2.3\"\n")
        self.test_file = open(self.test_file_path, "r+")  # 创建 test_file 属性

    def tearDown(self):
        self.test_file.close()  # 先关闭 test_file 属性
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_update_version_strings(self):
        # 是否能够正确地更新版本字符串
        update_version_strings(self.test_file_path, "1.2.3-beta")
        with open(self.test_file_path, "r") as f:
            content = f.readlines()
            self.assertEqual(content[0], 'version = "1.2.3-beta"\n')
            self.assertEqual(content[1], 'another_version = "4.5.6"\n')
            self.assertEqual(content[2], 'ignore_me = "1.2.3"\n')

    def test_basic_version_match(self):
        # 测试基本版本字符串是否被正确匹配
        version_str = '"1.2.3"'
        match = re.search(r'(")(\d+\.\d+\.\d+(-\S+)?)(")', version_str)  # 临时导入正则表达式
        self.assertIsNotNone(match)
        self.assertEqual(match.group(2), '1.2.3')

    def test_version_replacement(self):
        # 测试版本字符串是否被正确替换
        update_version_strings(self.test_file.name, '2.0.0')
        self.test_file.seek(0)
        content = self.test_file.read()
        self.assertIn('version = "2.0.0"', content)

# 运行测试用例
if __name__ == '__main__':
    unittest.main()
