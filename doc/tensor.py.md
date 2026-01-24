# paradma/tensor.py

## Overview
The `TensorAxiom` is an extension of the basic `Axiom` that handles multi-dimensional data grids. It is the Paradma equivalent of a NumPy `ndarray`, but one that possesses "Lifelike" properties such as temperature and manifold affiliation.

## Purpose
Standard tensors are just passive arrays of numbers. A `TensorAxiom` is a "Living Entity" in the mathematical substrate. It allows the AI to perform complex tensor math (like broadcasting addition) while keeping the data integrated with the project's cognitive and thermodynamic laws.

## Key Components

### `TensorAxiom` (Class)

#### Structural Properties
- **`shape`**: The dimensions of the tensor (e.g., `(3, 128)`).
- **`ndim`**: The number of axes.
- **`size`**: The total number of elements.
- **`_is_dense`**: Tracks whether the data is stored as a high-speed NumPy/CuPy buffer or a list of living Axioms.

#### State Transitions (The Phase Law)
- **Condensation (`condense()`)**: Converts a nested list of individual Axioms into a high-speed, contiguous memory buffer (NumPy). This is the "Solid" state, optimized for high-performance math.
- **Evaporation (`evaporate()`)**: Converts a dense buffer back into a nested list of individual living Axioms. This is the "Gas" state, optimized for granular modification and law-based reasoning.

#### Interaction Logic
- **Broadcasting Addition**: Supports adding scalars or other tensors. It uses recursive logic to ensure that Paradma laws are applied correctly across the entire multi-dimensional structure.
- **Integrated Slicing**: Supports standard Python slicing (e.g., `tensor[0:5, :]`) while returning new `TensorAxiom` views that preserve the manifold context.

## Technical Strategy
`TensorAxiom` ensures that no matter how complex the data structure, it never loses its "Truth Identity" (its connection to the Laws of the Manifold).

## Usage Example
```python
from paradma.tensor import TensorAxiom

# Create a 2D tensor in a learning manifold
t = TensorAxiom([[1, 2], [3, 4]], manifold=my_learning_space)

# Condense it for fast matrix math
t.condense()

# Perform addition
t2 = t + 5
```
