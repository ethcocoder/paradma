# paradma/stochastic.py

## Overview
A `Manifold` for randomness, chaos, and probabilistic generation. It replaces `numpy.random` with a system that treats uncertainty as a fundamental property of the data.

## Purpose
In Paradma, a random number isn't just a value; it's a "State." `stochastic.py` introduces the concept of **Superposed Chaos**, where a value is not determined until it is observed.

## Key Laws

### `chaos`
- Generates a **Superposed Tensor**.
- **Lazy Collapse**: Instead of returning a number, it returns a list of *generator functions* (lambdas).
- **The Wavefunction**: The `TensorAxiom` produced by this law holds potential values. The actual numbers are only instantiated when `axiom.observe()` is called, simulating quantum wavefunction collapse.

### `uniform` & `normal`
- Standard random generation laws that immediately collapse into fixed values (Classical Probabilities).

## Cognitive Role
Used to inject creativity and exploration into the AI's thinking. The "Chaos" law allows the AI to hold a "Maybe" state deep into its reasoning pipeline before deciding on a concrete value.

```python
from paradma.stochastic import StochasticManifold

monte_carlo = StochasticManifold()

# Create a cloud of undefined possibilities
cloud = monte_carlo.apply_law("chaos", shape=(3, 3))

# cloud.value contains callables, not numbers!

# Collapse the state
real_cloud = cloud.observe() # Now it contains numbers
```
