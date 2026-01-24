# paradma/test_autolearner.py

## Overview
A standalone test script to verify the basic functionality of the AutoLearner system. This is the "Hello World" of self-modifying AI code.

## Test Workflow
1. **Observation**: Takes 11 pairs of numbers (e.g., `5+3`, `10+20`) and solves them using NumPy, recording the inputs and outputs.
2. **Analysis**: The AutoLearner analyzes these 11 data points to deduce that the relationship is `Output = A + B`.
3. **Generation**: It generates a native Python function `learned_add(a, b)` that replicates this logic.
4. **Verification**: It tests the new function against unseen data points (e.g., `999+1`) to calculate a "Mastery Score."
5. **Graduation**: If Mastery > 90%, it declares independence from NumPy.

## Purpose
Used by developers to ensure the learning logic works in isolation before integrating it into the full `LearningManifold`.
