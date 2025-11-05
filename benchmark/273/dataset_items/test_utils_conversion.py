import unittest

from ctx_utils import conversion


class TestConversion(unittest.TestCase):
    def test_conversion_with_all_fields(self):
        self.assertAlmostEqual(conversion("0°25'30\"S"), -0.425)
        self.assertAlmostEqual(conversion("91°7'W"), -91.1166666667)

    def test_conversion_with_no_seconds(self):
        self.assertAlmostEqual(conversion("0°25'N"), 0.41666666667)
        self.assertAlmostEqual(conversion("91°7'E"), 91.11666666667)

    def test_conversion_with_no_minutes(self):
        self.assertEqual(conversion("0°S"), 0)
        self.assertEqual(conversion("91°W"), -91)

    def test_update_type_conversion(self):
        self.assertAlmostEqual(conversion("0°25'30.50\"S"), -0.42513888889)
        self.assertAlmostEqual(conversion("91°7'50.20\"N"), 91.13061111111)

if __name__ == '__main__':
    unittest.main()
