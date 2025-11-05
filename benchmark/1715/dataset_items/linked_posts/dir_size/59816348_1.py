class Test(unittest.TestCase):
    def test_du(self):
        root = '/tmp/du_test'
        subprocess.run(['rm', '-rf', root])
        test_utils.mkdir(root)
        test_utils.create_file(root, 'A', '1M')
        test_utils.create_file(root, 'B', '1M')
        sub = '/'.join([root, 'sub'])
        test_utils.mkdir(sub)
        test_utils.create_file(sub, 'C', '1M')
        test_utils.create_file(sub, 'D', '1M')
        subprocess.run(['ln', '-s', '/tmp', '/'.join([root, 'link']), ])
        self.assertEqual(4 << 20, util.du(root))
