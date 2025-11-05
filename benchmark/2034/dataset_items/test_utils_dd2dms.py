import unittest
from ctx_utils import dd2dms

class TestDd2dms(unittest.TestCase):
    def test_positive_degrees(self):
        self.assertEqual(dd2dms(12.3456), "12:20:44.15999999999622")

    def test_negative_degrees(self):
        self.assertEqual(dd2dms(-12.3456), "-12:20:44.15999999999622")

    def test_zero_degrees(self):
        self.assertEqual(dd2dms(0), "0:0:0")

    def test_degrees_with_no_seconds(self):
        self.assertEqual(dd2dms(1.0), "1:0:0.0")

    def test_degrees_with_full_minutes(self):
        self.assertEqual(dd2dms(1.0001), "1:0:0.36000000000012733")

    def test_degrees_with_negative_full_minutes(self):
        self.assertEqual(dd2dms(-1.0001), "-1:0:0.36000000000012733")

    def test_degrees_with_large_value(self):
        self.assertEqual(dd2dms(999.9999), "999:59:59.640000000130385")

    def test_degrees_with_negative_large_value(self):
        self.assertEqual(dd2dms(-999.9999), "-999:59:59.640000000130385")

    def test_degrees_with_decimal_precision(self):
        self.assertEqual(dd2dms(12.345678), "12:20:44.44079999999667")

    def test_degrees_with_negative_decimal_precision(self):
        self.assertEqual(dd2dms(-12.345678), "-12:20:44.44079999999667")

    def test_add_type_annotations(self):
        annotations = dd2dms.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('dd', annotations)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], str)
        self.assertEqual(annotations['dd'], float)

    def test_update_function_name(self):
        import ctx_utils
        self.assertTrue(callable(dd2dms))
        self.assertNotIn('decdeg2dms', ctx_utils.__dict__)

    def test_return_format(self):
        res = dd2dms(0)
        self.assertIsInstance(res, str)
        self.assertNotIsInstance(res, tuple)

if __name__ == '__main__':
    unittest.main()