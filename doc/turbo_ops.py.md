# paradma/turbo_ops.py

## Overview
A library of high-performance mathematical kernels optimized with **Numba**. These are the "Muscle" of the Paradma system.

## Purpose
While `jit_engine.py` provides the tools to compile code, `turbo_ops.py` contains the actual, hand-tuned implementations of critical operations. These functions are designed to bypass the CPython interpreter and run at near-native C speeds.

## Key Kernels

### `matmul_turbo(A, B)`
- A JIT-compiled matrix multiplication algorithm.
- Supports Matrix-Vector and Matrix-Matrix multiplication.
- Uses `fastmath=True` for aggressive compiler optimizations (e.g., SIMD instructions).

### `cosine_similarity_turbo(vectors, query)`
- The workhorse for the RAG (Retrieval-Augmented Generation) system.
- Calculates the similarity between a query and thousands of vectors in a tight, unrolled loop.
- **Zero Allocation**: Designed to minimize memory overhead during search.

### `euclidean_distance_turbo`
- Optimized distance calculation for spatial analysis.

## Significance
This file makes the "AutoLearner" possible. It serves as the "Gold Standard" library that the AutoLearner can fallback to or aspire to reproduce. Any operation found here runs orders of magnitude faster than standard Python.

## Usage
These functions are typically not called directly by users. Instead, the `LearningManifold` or `JITEngine` detects their presence and dynamically swaps standard Python logic for these turbo kernels at runtime.
