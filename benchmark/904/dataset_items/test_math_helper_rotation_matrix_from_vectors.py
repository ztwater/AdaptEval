import numpy as np
from math_helper import rotation_matrix_from_vectors
import unittest
import inspect

class TestRotationMatrixFromVectors(unittest.TestCase):

    def test_rotation_matrix_calculation(self):
        # 测试旋转矩阵的计算
        # 设置参考向量和目标向量
        reference = np.array([1, 0, 0])
        target = np.array([0, 1, 0])
        # 计算预期的旋转矩阵
        expected_rotation_matrix = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        # 调用函数并断言结果
        rotation_matrix = rotation_matrix_from_vectors(reference, target)
        self.assertTrue(np.allclose(rotation_matrix, expected_rotation_matrix))

    def test_rename_parameter(self):
        # Get the signature of the method
        signature = inspect.signature(rotation_matrix_from_vectors)

        # Check if the method has the correct annotations
        parameters = signature.parameters
        for name, param in parameters.items():
            self.assertIn(name, ['reference', 'target', 'return'])

    def test_add_type_annotations(self):
        # Get the signature of the method
        signature = inspect.signature(rotation_matrix_from_vectors)

        # Check if the method has the correct annotations
        parameters = signature.parameters
        for name, param in parameters.items():
            if name in ['reference', 'target']:
                self.assertIsNotNone(param.annotation, f"{name} parameter is missing type annotation")
                self.assertEqual(param.annotation, np.ndarray, f"{name} parameter should be annotated as np.ndarray")
            elif name == 'return':
                self.assertIsNotNone(param.annotation, "Return type is missing type annotation")
                self.assertEqual(param.annotation, np.ndarray, "Return type should be annotated as np.ndarray")

if __name__ == '__main__':
    unittest.main()
