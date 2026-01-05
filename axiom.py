import typing as t
from .manifold import Manifold, euclidean

class Axiom:
    """
    The Axiom is the fundamental unit of Paradma.
    It holds data (value) and exists within a specific Manifold (mathematical space).
    """
    def __init__(self, value: t.Any, manifold: Manifold = euclidean, **metadata):
        self._value = value
        self.manifold = manifold
        self.temperature = 100.0  # Initial "Data Heat"
        self.metadata = metadata
        self.is_compressed = False
        self.is_pinned = metadata.get("pinned", False) # Critical data protection
        self.entanglements: t.List['Axiom'] = []

    def __getattr__(self, name: str):
        """
        'Law Stealing': If a method isn't found on the Axiom, 
        try to fetch it from its Manifold as a Law.
        """
        try:
            # We return a partial application or a wrapper that calls apply_law
            def law_wrapper(*args, **kwargs):
                return self.manifold.apply_law(name, self, *args, **kwargs)
            return law_wrapper
        except AttributeError:
            raise AttributeError(f"'Axiom' object has no attribute '{name}' and no such Law in {self.manifold.name}")

    def __add__(self, other):
        """Operator overloading delegating to the Manifold's 'add' law."""
        if isinstance(other, Axiom):
            # If both are axioms, let the manifold handle the interaction
            return self.manifold.apply_law("add", self, other)
        # Fallback to simple value addition if 'other' is a primitive
        return self.value + other

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val
        # Notify entanglements (Spooky Action)
        if hasattr(self, 'entanglements'):
            for other in self.entanglements:
                if other.value != new_val:
                    other.value = new_val

    def observe(self):
        """The Observer Effect: Forces the Axiom's wavefunction to collapse (returns value)."""
        # Automatic Rehydration if compressed
        if self.is_compressed:
            from .efficiency import Compressor
            Compressor().decompress(self)
            self.temperature = 50.0 # Heat up slightly upon observation
            
        # Trigger superposition law if the manifold supports it
        try:
            return self.manifold.apply_law("superposition", self)
        except AttributeError:
            return self.value

    def __repr__(self):
        return f"Axiom({self.value})"
