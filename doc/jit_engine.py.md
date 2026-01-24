# paradma/jit_engine.py

## Overview
The Just-In-Time (JIT) compilation engine for Paradma laws. It provides a decorator-based interface to accelerate Python functions using **Numba**.

## Purpose
Python is slow; C is fast. `jit_engine.py` allows Paradma to write high-level Python code that executes at machine-code speeds. It bridges the gap between the flexibility of the `Manifold` system and the raw performance required for deep learning.

## Key Component

### `jit_law` (Decorator)
Wraps a mathematical function to enable compilation.
- **Automatic Detection**: Checks if `numba` is installed. If yes, it compiles the function using LLVM. If no, it falls back gracefully to standard Python execution.
- **Parallelism**: Supports the `parallel=True` flag to automatically distribute loops across multiple CPU cores.
- **No-Python Mode**: Enforces `nopython=True` to ensure the code runs entirely without the Python Global Interpreter Lock (GIL).

## Usage
Developers (or the Code Generator) apply this decorator to heavy mathematical kernels.

```python
from paradma.jit_engine import jit_law

@jit_law(nopython=True)
def heavy_math(a, b):
    # This loop runs at C++ speeds
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
```

## Significance
This is the "Turbo Button" for the Paradox project. It ensures that the custom-built mathematical substrate doesn't suffer from the typical performance penalties of pure Python implementations.
