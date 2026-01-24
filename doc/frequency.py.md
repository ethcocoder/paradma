# paradma/frequency.py

## Overview
A `Manifold` dedicated to operating in the Frequency Domain (Fourier Space). It replaces standard `numpy.fft` logic with Paradma-integrated laws.

## Purpose
Signal processing requires a different set of mathematical rules than Euclidean geometry. `frequency.py` defines a space where the primary operations are transformations between the Time Domain and the Frequency Domain.

## Key Laws

### `fft` (Fast Fourier Transform)
- Converts a time-series `TensorAxiom` into its frequency components.
- Implementation: Uses a Discrete Fourier Transform (DFT) logic (currently $O(N^2)$ for simplicity/correctness in the axiom system, though named `fft`).
- Returns a new TensorAxiom containing complex numbers representing magnitude and phase.

### `ifft` (Inverse FFT)
- Converts frequency components back into a time-series signal.

## Technical Details
- **Complex Numbers**: The manifold handles Python's `complex` type naturally.
- **1D Support**: Currently specialized for 1D signals (like audio or price series).

## Cognitive Role
Used by the AI to analyze periodicity in data. For example, discovering the "Rhythm" of a user's typing or the cyclic patterns in a dataset.
