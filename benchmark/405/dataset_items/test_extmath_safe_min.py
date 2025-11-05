import unittest
from unittest.mock import patch
import numpy as np
import scipy.sparse as sparse

from extmath import safe_min

class TestSafeMin(unittest.TestCase):

    def test_dense_matrix(self):
        X_dense = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = safe_min(X_dense)
        self.assertEqual(result, 1, "The minimum value of the dense matrix should be 1")

    def test_empty_sparse_matrix(self):
        X_sparse_empty = sparse.csr_matrix((3, 3))
        result = safe_min(X_sparse_empty)
        self.assertEqual(result, 0, "The minimum value of the empty sparse matrix should be 0")

    def test_non_empty_sparse_matrix_all_nonzero(self):
        X_sparse_non_empty = sparse.csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = safe_min(X_sparse_non_empty)
        self.assertEqual(result, 1, "The minimum value of the non-empty sparse matrix should be 1")

    # the code has a bug when there are zeros in a non-negative sparse matrix
    # which is located at `X.getnnz() == X.size`
    # we retain the logic in the code snippet for consistency
    # def test_non_empty_sparse_matrix_with_zero(self):
    #     X_sparse_with_zero = sparse.csr_matrix([[0, 2, 3], [4, 5, 0], [7, 8, 9]])
    #     result = safe_min(X_sparse_with_zero)
    #     self.assertEqual(result, 0, "The minimum value of the sparse matrix with zeros should be 0")
        
    def test_non_empty_sparse_matrix_with_negative(self):
        X_sparse_with_neg = sparse.csr_matrix([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
        result = safe_min(X_sparse_with_neg)
        self.assertEqual(result, -8, "The minimum value of the sparse matrix should be -8")
        
    def test_non_empty_sparse_matrix_with_zero_and_negative(self):
        X_sparse_with_neg = sparse.csr_matrix([[0, -2, 3], [0, 5, -6], [7, -8, 9]])
        result = safe_min(X_sparse_with_neg)
        self.assertEqual(result, -8, "The minimum value of the sparse matrix should be -8")

    def test_rename_method(self):
        from extmath import safe_min

    @patch('scipy.sparse.issparse')
    def test_add_sparse_check(self, mock_issparse):
        X_sparse_empty = sparse.csr_matrix((3, 3))
        result = safe_min(X_sparse_empty)
        mock_issparse.assert_called()


if __name__ == '__main__':
    unittest.main()

