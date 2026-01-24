# paradma/autolearner.py

## Overview
The "Brain" of the Paradma project. The `AutoLearner` is a meta-programming engine designed to observe the AI's mathematical operations and gradually replace slow Python code with high-performance native implementations.

## Purpose
Most AI systems rely on external libraries (like NumPy) forever. The `AutoLearner` allows Paradox to eventually become independent of NumPy by:
1. **Teaching Phase**: Watching how NumPy performs operations.
2. **Analysis Phase**: Identifying patterns and algorithms in the observed data.
3. **Graduation Phase**: Generating its own native C/NumPy-equivalent code and using it instead.

## Key Components

### `KnowledgeBase` (Class)
Stores observations of mathematical operations.
- **Recording**: Captures inputs, outputs, and execution metadata.
- **Persistence**: Saves the acquired knowledge to a `.paradma_knowledge` directory, allowing the AI to learn across multiple sessions.

### `PatternAnalyzer` (Class)
The "Learning Brain." It analyzes recorded observations to "Solve" the underlying mathematical formula:
- **`analyze_addition`**: Reconstructs the logic of sum for vectors and scalars.
- **`analyze_sqrt`**: Discovers Newton's method for calculating square roots autonomously.
- **`analyze_dot`/`analyze_matmul`**: Identifies vector/matrix products and wraps them in **Numba (`njit`)** for hardware-speed execution.

### `AutoLearner` (Class)
The central manager of the self-bootstrapping process.
- **Threshold**: Only attempts to learn a law after it has been observed more than $N$ times.
- **Execution**: Dispatches operations to either the "Teacher" (NumPy) or the "Learned Code" (Native/Numba) depending on the operation's maturity.

## Graduation Lifecycle
- **Student**: Law is unknown; we just use NumPy.
- **Apprentice**: We are collecting data points.
- **Scholar**: Algorithm identified; verifying against Teacher.
- **Master**: Law is "Graduated." We now use our own optimized, native-compiled code.

## Significance
This is the heart of the project's "Self-Evolution" philosophy. By learning the very math it uses to think, the AI achieves a higher level of structural autonomy than standard models.

## Usage
The `AutoLearner` is typically accessed via the `get_autolearner()` singleton and works silently in the background of every `Manifold`.
