import unittest
from unittest.mock import patch
import pandas as pd
from Utils_plotter import plot_candle_patter
import finplot as fplt
import inspect


class TestPlotCandlePatter(unittest.TestCase):
    
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'Open': [100, 105, 102, 108, 110],
            'Close': [105, 102, 108, 110, 107],
            'High': [106, 106, 109, 112, 111],
            'Low': [99, 100, 101, 106, 105],
            'Volume': [1000, 1200, 1100, 1300, 1150]
        }
        self.df = pd.DataFrame(data)

    @patch('finplot.show', wraps=fplt.show(qt_exec=True))
    def test_function(self, mock_show):
        try:
            # Call the function to test if it executes without errors
            plot_candle_patter(self.df)
            # If the plot was created and displayed, the function should work as expected
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"plot_candle_patter() raised an exception: {e}")

    def test_encapsulate(self):
        self.assertTrue(callable(plot_candle_patter))
        parameters = inspect.signature(plot_candle_patter).parameters
        self.assertIn('df', parameters)

    @patch('finplot.show', wraps=fplt.show(qt_exec=True))
    @patch('finplot.create_plot', wraps=fplt.create_plot)
    def test_update_creation_string(self, mock_plot, mock_show):
        plot_candle_patter(self.df)
        mock_plot.assert_called_with('symbol')

if __name__ == '__main__':
    unittest.main()
