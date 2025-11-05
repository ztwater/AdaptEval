import unittest
import torch
from torch import Tensor
from inference_utils import gkern


class TestGkern(unittest.TestCase):
    def test_add_type_annotations(self):
        annotations = gkern.__annotations__
        self.assertIn('kernlen', annotations)
        self.assertIn('nsig', annotations)
        self.assertIn('return', annotations)
        self.assertEqual(annotations['kernlen'], int)
        self.assertEqual(annotations['nsig'], float)
        self.assertEqual(annotations['return'], Tensor)

    def test_default_parameter_values(self):
        # Test with default parameters
        kernel_default = gkern()
        self.assertEqual(kernel_default.shape, (5, 5), "The default kernel should be 5x5")

    def test_custom_parameter_values(self):
        # Test with custom parameters
        custom_kernel = gkern(kernlen=7, nsig=1.5)
        self.assertEqual(custom_kernel.shape, (7, 7), "The custom kernel should be 7x7")

    def test_conversion_to_torch_tensor(self):
        kernlen = 5
        nsig = 1.0
        kernel = gkern(kernlen, nsig)
        # Check if the conversion to torch.Tensor is successful and the data type is float
        self.assertTrue(torch.is_floating_point(kernel), "The tensor should be of a floating point type")

if __name__ == '__main__':
    unittest.main()