# paradma/test_integration.py

## Overview
An integration test verifying that the standard `Manifold` classes naturally pick up efficiently learned code.

## Purpose
Ensures that once an operation is learned by the `AutoLearner`, it is automatically used by the rest of the system (e.g., the `Euclidean` manifold) without manual code changes. This proves the "Global Upgrade" capability of the system.

## Workflow
1. Checks if `add` has graduated in the AutoLearner.
2. Instantiates standard `Axiom` objects in the `Euclidean` manifold.
3. Performs addition.
4. Confirms that the operation succeeded, verifying the dispatch pipeline.
