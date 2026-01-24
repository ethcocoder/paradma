# paradma/__init__.py

## Overview
The initialization entry point for the Paradma mathematical substrate. It orchestrates the loading of the Axiom-Manifold system and initializes the AutoLearning engine.

## Exposed Components
- **`Axiom`**: The fundamental unit of data.
- **`TensorAxiom`**: Multi-dimensional data units.
- **`Manifold`**: The registry for mathematical laws.
- **`LearningManifold`**: The space where self-bootstrapping occurs.
- **`AutoLearner`**: The engine for learning from NumPy.
- **`CodeGenerator`**: The system for self-modifying source code.

## Package Architecture
Paradma follow a specific dependency chain:
1. **Low-Level Math**: `linalg.py`, `stochastic.py`.
2. **Substrate Core**: `axiom.py` and `manifold.py`.
3. **Advanced Structures**: `tensor.py`.
4. **Learning Layer**: `autolearner.py` and `code_generator.py`.
5. **Applied Spaces**: `learning_manifold.py`, `finance.py`, `efficiency.py`.

## Core Philosophy
Paradma is built on the idea that "Math is Living." By making every number an `Axiom` in a `Manifold`, the project creates a world where the AI's internal logic can evolve, optimize, and even rewrite itself to achieve maximum intelligence and structural autonomy.

## Basic Usage
```python
import paradma

# Access the global learning space
m = paradma.learning

# Perform some math that Paradma will learn from
a = paradma.Axiom([1, 2, 3], manifold=m)
b = a.dot(a) # Paradma records this observation!
```
