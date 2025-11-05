import inspect
import unittest
import torch
from e2vid_image_utils import gkern
 
class TestGkern(unittest.TestCase):
    def test_kernel_shape(self):
        # 测试生成的高斯核的形状
        kernlen = 5
        kernel = gkern(kernlen=kernlen)
        self.assertEqual(kernel.shape, (kernlen, kernlen))

    def test_kernel_sum(self):
        # 测试高斯核的总和是否接近1
        kernlen = 5
        kernel = gkern(kernlen=kernlen)
        self.assertAlmostEqual(kernel.sum().item(), 1.0, places=5)

    def test_kernel_center(self):
        # 测试高斯核中心元素是否为最大值
        kernlen = 5
        kernel = gkern(kernlen=kernlen)
        self.assertEqual(kernel.max(), kernel[int(kernlen / 2), int(kernlen / 2)])

    def test_kernel_symmetry(self):
        # 测试高斯核是否关于中心对称
        kernlen = 5
        kernel = gkern(kernlen=kernlen)
        for i in range(kernlen):
            for j in range(kernlen):
                self.assertEqual(kernel[i, j], kernel[kernlen - i - 1, kernlen - j - 1])

    def test_different_nsig(self):
        # 测试不同的nsig参数是否影响高斯核
        kernlen = 5
        nsig1 = 1.0
        nsig2 = 2.0
        kernel1 = gkern(kernlen=kernlen, nsig=nsig1)
        kernel2 = gkern(kernlen=kernlen, nsig=nsig2)
        self.assertFalse(torch.allclose(kernel1, kernel2))

    def test_default_values(self):
        parameters = inspect.signature(gkern).parameters
        self.assertEqual(parameters['kernlen'].default, 5)
        self.assertEqual(parameters['nsig'].default, 1.0)

    def test_kernel_conversion(self):
        kernel = gkern()
        self.assertIsInstance(kernel, torch.Tensor, "Kernel should be a torch tensor")
        self.assertEqual(kernel.dtype, torch.float32, "Kernel dtype should be torch.float32")


if __name__ == '__main__':
    unittest.main()
