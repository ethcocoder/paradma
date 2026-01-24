# paradma/learning_manifold.py

## Overview
A specialized `Manifold` designed for the learning transition. It is the active playground where the AI switches from using NumPy to using its own learned "Turbo" operations.

## Purpose
`learning_manifold.py` provides the implementation of standard mathematical operations (Add, Sub, Mul, Div, Dot, Softmax, etc.) that are hooked into the `AutoLearner`. It acts as the "Bridge" between the Python world and the independent Paradox future.

## Key Features

### Self-Learning Operations
Every method in this manifold follows a "Learning Dispatch" pattern:
- **`_learning_add`**, **`_learning_dot`**, etc.
- **Step 1**: Track the call count.
- **Step 2**: If the law is "Graduated," call the high-speed native optimized implementation.
- **Step 3**: If it's still restricted, call NumPy but record the result in the `KnowledgeBase`.

### Turbo Acceleration
- **Numba Integration**: Uses `_try_turbo()` to check if a law has a Numba-jit optimized version available in `turbo_ops.py`. This provides near-C performance for complex matrix math.
- **Hardware Agnostic**: Automatically falls back to standard Python/NumPy if Numba is not available.

## Integrated Learnable Laws
The manifold comes pre-configured with learning hooks for:
- **Arithmetic**: Add, Subtract, Multiply, Divide.
- **Statistics**: Mean, Median, Standard Deviation.
- **Linear Algebra**: Dot Product, Matrix Multiply (`matmul`).
- **Activation/Functions**: Sqrt, Exp, Log, Sin, Cos.

## Statistics & Progress
The `show_learning_progress()` method provides a terminal-friendly dashboard showing:
- Which operations are currently being learned.
- Count of observations for each.
- The "Maturity" percentage of the entire mathematical space.

## Technical Details
- **Instance**: Provides a pre-configured `learning` instance ready for immediate use.
- **Axiom Wrapping**: Automatically wraps learning results back into Paradox `Axiom` objects to maintain manifold consistency.

## Usage
Used as the default manifold for training scripts where the developer wants the AI to improve its own mathematical performance while it learns the language data.
