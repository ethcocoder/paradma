import functools
import typing as t

def observer(func: t.Callable):
    """
    The Observer Decorator: Implements 'Lazy Evaluation'.
    The function is only executed when the result is explicitly observed.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Instead of returning the result, we return an Axiom that holds the logic
        # This is a form of Superposition
        from .axiom import Axiom
        return Axiom(lambda: func(*args, **kwargs))
    return wrapper

class ThermalCounter:
    """
    ThermalCounter: Tracks and manages the 'Temperature' (Heat) of Axioms.
    Colder data eventually gets compressed or evicted.
    """
    def __init__(self, decay_rate: float = 0.9):
        self.decay_rate = decay_rate

    def cool(self, axiom):
        """Lowers the temperature of an Axiom (unless it is pinned)."""
        if getattr(axiom, 'is_pinned', False):
            axiom.temperature = 100.0 # Pinning keeps it hot forever
            return 100.0
        axiom.temperature *= self.decay_rate
        return axiom.temperature

    def heat(self, axiom):
        """Increases the temperature (activity) of an Axiom."""
        axiom.temperature = min(100.0, axiom.temperature + 10.0)
        return axiom.temperature

class Hologram:
    """
    A Hologram is a dehydrated, low-resolution recipe of an Axiom.
    It takes up minimal space and can be rehydrated back into an Axiom.
    """
    def __init__(self, recipe: t.Callable, metadata: dict):
        self.recipe = recipe
        self.metadata = metadata

    def rehydrate(self):
        """Executes the recipe to restore the original value."""
        return self.recipe()

class Compressor:
    """
    Compressor: Implements the Entropy Law.
    Converts 'Cold' Axioms into Holograms to save 'Computational Mass'.
    """
    def __init__(self, threshold: float = 10.0):
        self.threshold = threshold

    def compress(self, axiom):
        """Converts an Axiom into a Holographic state if it's cold enough and NOT pinned."""
        if getattr(axiom, 'is_pinned', False):
            return False # Pinned data is never compressed
            
        if axiom.temperature <= self.threshold:
            # Create a recipe: for now, it's just a lambda returning the current value
            current_value = axiom.value
            recipe = lambda: current_value
            
            axiom.hologram = Hologram(recipe, axiom.metadata.copy())
            axiom.is_compressed = True
            axiom.value = None # Clear data to "save space"
            return True
        return False

    def decompress(self, axiom):
        """Restores a compressed Axiom."""
        if hasattr(axiom, 'is_compressed') and axiom.is_compressed:
            axiom.value = axiom.hologram.rehydrate()
            axiom.is_compressed = False
            del axiom.hologram
            return True
        return False
