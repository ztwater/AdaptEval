import unittest
from datetime import datetime, timedelta
from lang import pretty_date

class TestPrettyDate(unittest.TestCase):

    def setUp(self):
        # Set up a fixed "now" time for consistent test results
        self.now = datetime(2024, 7, 1, 12, 0)
        # This will be used to test the function without passing 'now' parameter
        self.fixed_time = datetime(2024, 1, 1, 12, 0)

    def test_check_parameter_type(self):
        with self.assertRaises(ValueError):
            pretty_date("invalid_type")

    def test_change_parameter_type(self):
        with self.assertRaises(TypeError):
            pretty_date()

    def test_add_optional_now_parameter_with_default_value(self):
        # Test with the default value
        expected_result = "yesterday"
        self.assertEqual(pretty_date(datetime.now() - timedelta(days=1)), expected_result)

    def test_add_optional_now_parameter(self):
        # Test with custom 'now' parameter
        custom_now = datetime(2023, 12, 31, 12, 0)
        time_1_day_before_custom_now = custom_now - timedelta(days=1)
        expected_result = "yesterday"
        self.assertEqual(pretty_date(time_1_day_before_custom_now, now=custom_now), expected_result)

    def test_change_if_condition(self):
        # Test the new condition for 'day_diff' < 28
        self.assertEqual(pretty_date(self.now - timedelta(days=27), self.now), "3 weeks ago")
        self.assertEqual(pretty_date(self.now - timedelta(days=30), self.now), "a month ago")

    def test_add_if_condition_for_week(self):
        self.assertEqual(pretty_date(self.now - timedelta(days=10), self.now), "a week ago")

    def test_add_if_condition_for_month(self):
        self.assertEqual(pretty_date(self.now - timedelta(days=35), self.now), "a month ago")

    def test_add_if_condition_for_year(self):
        self.assertEqual(pretty_date(self.now - timedelta(days=370), self.now), "a year ago")

    def test_yesterday_condition(self):
        # Test the new condition for 'day_diff' < 28
        self.assertEqual(pretty_date(self.now - timedelta(days=1), self.now), "yesterday")


# This allows us to run the tests from the command line
if __name__ == '__main__':
    unittest.main()