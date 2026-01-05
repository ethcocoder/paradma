from .manifold import Manifold
from .tensor import TensorAxiom
import typing as t

class LinearAlgebraManifold(Manifold):
    """
    A Manifold dedicated to Linear Algebra operations.
    Replaces np.linalg.
    """
    def __init__(self, name: str = "HilbertSpace"):
        super().__init__(name)
        self.register_law("dot", self.dot_product)
        self.register_law("matmul", self.matrix_multiply)
        self.register_law("transpose", self.transpose)
        self.register_law("det", self.determinant)

    def dot_product(self, ax1: TensorAxiom, ax2: TensorAxiom):
        """
        Dot Product of two vectors.
        """
        # Simplistic 1D implemenation for MVP
        if ax1.ndim != 1 or ax2.ndim != 1:
            raise NotImplementedError("Dot product currently only supports 1D vectors for MVP phase.")
        
        if ax1.shape != ax2.shape:
             raise ValueError(f"Shapes {ax1.shape} and {ax2.shape} not aligned.")

        # Calculate sum of products
        # Zip and sum
        result = sum(x * y for x, y in zip(ax1.value, ax2.value))
        return TensorAxiom(result, self)

    def matrix_multiply(self, ax1: TensorAxiom, ax2: TensorAxiom):
        """
        Matrix Multiplication Replaces np.matmul (@).
        """
        if ax1.ndim != 2 or ax2.ndim != 2:
             raise NotImplementedError("Matmul currently only supports 2D matrices.")
        
        rows1, cols1 = ax1.shape
        rows2, cols2 = ax2.shape
        
        if cols1 != rows2:
             raise ValueError(f"Shapes {ax1.shape} and {ax2.shape} not aligned: {cols1} != {rows2}")
        
        # Result shape (rows1, cols2)
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]
        
        a = ax1.value
        b = ax2.value
        
        # Naive O(n^3) implementation
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += a[i][k] * b[k][j]
                    
        return TensorAxiom(result, self)

    def transpose(self, ax: TensorAxiom):
        """
        Transpose a 2D matrix.
        """
        if ax.ndim != 2:
             raise NotImplementedError("Transpose currently only supports 2D matrices.")
        
        rows, cols = ax.shape
        new_data = [[ax.value[j][i] for j in range(rows)] for i in range(cols)]
        return TensorAxiom(new_data, self)

    def determinant(self, ax: TensorAxiom):
        """
        Calculate Determinant of a matrix.
        """
        if ax.ndim != 2 or ax.shape[0] != ax.shape[1]:
             raise ValueError("Determinant requires a square 2D matrix.")
        
        result = self._recursive_det(ax.value)
        return TensorAxiom(result, self)

    def _recursive_det(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for c in range(n):
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._recursive_det(sub_matrix)
        return det
