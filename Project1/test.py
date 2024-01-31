import unittest
import numpy as np
from function import invert_matrix_with_changed_column

class TestInvertMatrixFunction(unittest.TestCase):
    def test_invert_matrix_with_changed_column(self):
        A = np.array([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
        A_inv = np.linalg.inv(A)
        x = np.array([1, 0, 1])
        i = 2

        B_inv_expected = np.array([[1, 1, -1], [0, 1, 0], [0, 0, 1]])
        B_inv_actual = invert_matrix_with_changed_column(A, A_inv, x, i)

        np.testing.assert_allclose(B_inv_actual, B_inv_expected, atol=1e-10)

    def test_invert_matrix_with_changed_column_singular_matrix(self):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        try:
            A_inv = np.linalg.inv(A)
            x = np.array([1, 2, 3])
            i = 1
            B_inv_actual = invert_matrix_with_changed_column(A, A_inv, x, i)
            self.assertIsNone(B_inv_actual)
        except np.linalg.LinAlgError:
            A_inv = None


if __name__ == '__main__':
    unittest.main()
