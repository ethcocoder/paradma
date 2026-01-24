# paradma/linalg.py

## Overview
A `Manifold` dedicated to Linear Algebra operations (the "Hilbert Space"). It replaces `numpy.linalg` with self-contained Paradma laws for matrix operations.

## Purpose
Linear algebra is the engine of deep learning. By moving these operations into a Paradma Manifold, the AI gains the ability to:
1. Track the "Temperature" and "Entropy" of matrix operations.
2. Use the `AutoLearner` to optimize matrix multiplication over time.
3. Apply "Spooky Action" across entire tensor structures.

## Key Laws

### `matmul` (Matrix Multiplication)
- Replaces the `@` operator.
- Implementation: Includes a naive $O(N^3)$ Python implementation for bootstrapping, which the AutoLearner is expected to eventually replace with a Numba-optimized version.
- Shape checking ensures rigorous alignment of dimensions.

### `determinant` (`det`)
- Computes the scalar determinant of a square matrix.
- Implementation: Uses a recursive Laplace expansion. This is computationally expensive ($O(N!)$) and serves as a prime target for the AI to learn a faster Gaussian elimination method.

### `dot` & `transpose`
- Standard vector inner products and matrix transposition.

## Usage
Used heavily by the `Transformer` module for attention mechanism calculations (Subject to AutoLearning optimization).

```python
from paradma.linalg import LinearAlgebraManifold
from paradma.tensor import TensorAxiom

hilbert = LinearAlgebraManifold()
A = TensorAxiom([[1, 2], [3, 4]], manifold=hilbert)
B = TensorAxiom([[1, 0], [0, 1]], manifold=hilbert)

# Matrix multiply
C = hilbert.apply_law("matmul", A, B)
```
