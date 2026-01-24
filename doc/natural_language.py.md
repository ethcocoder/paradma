# paradma/natural_language.py

## Overview
A high-level interface that allows users (and potentially the AI itself) to define physical laws using simple English sentences.

## Purpose
Paradma envisions a future where physics is programmable via natural language. `natural_language.py` is the prototype for this "Semantic Physics" engine. It translates strings like "Apply Antigravity" into rigorous API calls.

## Key Components

### `Universe` (Class)
A container that strictly manages a collection of Axioms.
- **`add(value)`**: Injects new matter (Axioms) into the universe.
- **`apply(law_name)`**: Broadcasts a law across *every* axiom in the universe simultaneously.

### `NaturalLanguage` (Class)
The parser/interpreter.
- **`execute(sentence)`**:
  - **"Apply [Law]"**: Triggers `universe.apply(law)`.
  - **"Add [Number]"**: Triggers `universe.add(number)`.

## Significance
This module represents the "User Interface" for the substrate. It allows a developer to interact with the AI's internal simulator without writing Python code, paving the way for a CLI or Chat-based physics debugger.

## Usage Example
```python
from paradma.natural_language import NaturalLanguage, Universe

u = Universe()
nlp = NaturalLanguage(u)

# Create matter
nlp.execute("Add 100")

# Change physics
nlp.execute("Apply Antigravity")
```
