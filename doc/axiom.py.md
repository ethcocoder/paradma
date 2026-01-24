# paradma/axiom.py

## Overview
The `Axiom` is the fundamental unit of information in the Paradma system. It represents a piece of data (the `value`) existing within a specific mathematical space (the `Manifold`).

## Purpose
In standard programming, data is just a value (like an `int` or `float`). In Paradma, data is an "Object of Truth" that is bound by the specific laws of the space it lives in. This allows the AI to perform complex operations like "Observing" a value or "Entangling" it with others.

## Key Component

### `Axiom` (Class)

#### Core Attributes
- **`value`**: The actual numerical or structured data.
- **`manifold`**: The mathematical space (e.g., `Euclidean` or `Learning`) this axiom belongs to. Laws of this manifold dictate how the axiom interacts with others.
- **`temperature`**: A project-specific metric representing "Data Heat" or information entropy.
- **`entanglements`**: A list of other Axioms this specific one is linked to via "Spooky Action at a Distance."

#### Key Mechanics
- **Law Stealing (`__getattr__`)**: If you call a method on an Axiom that isn't explicitly defined (like `.add()` or `.sin()`), the Axiom "Steals" the corresponding law from its parent Manifold and applies it to itself.
- **Operator Overloading**: Basic python operators like `+` are mapped to the manifold's laws (e.g. the `"add"` law).
- **Spooky Action (Setter)**: When an Axiom's value is updated, it automatically propagates that change to all entangled Axioms, ensuring constant synchronization across the cognitive system.
- **The Observer Effect (`observe()`)**:
  - Automatically rehydrates/decompresses if the data was optimized.
  - Collapses the "Wavefunction" of the data if the manifold supports probabilistic states.

## Technical Details
- **Determinism**: Axioms ensure that mathematical operations are performed consistently within their designated spaces.
- **Metadata**: Can carry arbitrary extra information (e.g. `pinned=True` for critical constants).

## Usage Example
```python
from paradma.axiom import Axiom
from paradma.manifold import euclidean

# Create two axioms in the Euclidean space
a = Axiom(10, manifold=euclidean)
b = Axiom(20, manifold=euclidean)

# Add them using the manifold's laws
c = a + b 
print(c) # Axiom(30)
```
