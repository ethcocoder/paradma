# paradma/efficiency.py

## Overview
A module dedicated to managing "Computational Mass" and data lifecycle. It implements the thermodynamic laws of the Paradox project, specifically regarding data temperature, lazy evaluation, and holographic compression.

## Purpose
In a project with potentially millions of `Axiom` objects, performance and memory management are critical. `efficiency.py` ensures that only the "Hot" (active) data consumes significant system resources, while "Cold" (ignored) data is compressed into a dormant state.

## Key Concepts

### The Observer Effect (`observer` decorator)
Implements **Lazy Evaluation**. When a function is wrapped with `@observer`, it doesn't execute immediately. Instead, it returns an `Axiom` holding a "Recipe" (lambda) for the truth. The actual calculation only happens if and when a user calls `.observe()` on the Axiom.

### Thermal Dynamics (`ThermalCounter`)
Tracks the "Heat" of every Axiom.
- **Heat**: Increases when data is accessed or updated.
- **Cool**: Gradually decays over time if the data is not used.
- **Pinning**: "Pinned" axioms (critical constants or laws) stay hot forever and are immune to compression.

### Holographic Storage (`Hologram`)
A `Hologram` is a "Dehydrated" version of an Axiom. It stores only the recipe to recreate the data, 아니라 the raw values themselves. This consumes minimal RAM compared to full tensors.

### The Entropy Law (`Compressor`)
The mechanism that converts thermal states into physical storage states:
- **`compress()`**: If an Axiom's temperature drops below a `threshold` (default 10.0), the data is cleared and replaced by a Hologram.
- **`decompress()`**: When a Hologram is "Observed," the compressor uses the recipe to "Rehydrate" the Axiom back into its original state.

## Significance in Paradox AI
This module simulates a biological brain's "Forgetting" and "Retrieval" mechanisms. It prevents the AI from being overwhelmed by its own accumulated history, allowing it to maintain focus on the immediate cognitive task while keeping the "Distant Past" searchable but lightweight.

## Usage Example
```python
from paradma.efficiency import Compressor, ThermalCounter

counter = ThermalCounter(decay_rate=0.5)
compressor = Compressor(threshold=20.0)

# Over time, unused data cools down
counter.cool(my_axiom)

# If cold enough, it becomes a Hologram
compressor.compress(my_axiom) 
# The Axiom is now lightweight; its .value is None until observed!
```
