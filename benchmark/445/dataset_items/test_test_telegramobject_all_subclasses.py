import unittest

from test_telegramobject import all_subclasses

# Define sample classes for testing
class Foo:
    pass

class Bar(Foo):
    pass

class Baz(Foo):
    pass

class Bing(Bar):
    pass

class TestAllSubclasses(unittest.TestCase):

    def test_direct_subclasses(self):
        result = all_subclasses(Foo)
        expected = {Foo, Bar, Baz, Bing}
        self.assertEqual(result, expected)

    def test_single_class(self):
        result = all_subclasses(Baz)
        expected = {Baz}
        self.assertEqual(result, expected)

    def test_nested_subclasses(self):
        result = all_subclasses(Bar)
        expected = {Bar, Bing}
        self.assertEqual(result, expected)

    def test_class_includes_itself(self):
        result = all_subclasses(Foo)
        self.assertIn(Foo, result)

    def test_empty_class(self):
        class Empty:
            pass
        result = all_subclasses(Empty)
        expected = {Empty}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

