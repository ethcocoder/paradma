import typing as t

class Manifold:
    """
    A Manifold is a mathematical space that defines the 'Laws' of interaction.
    It acts as a registry for operations that Axioms can perform.
    """
    def __init__(self, name: str):
        self.name = name
        self.laws: t.Dict[str, t.Callable] = {}
        self.config = {
            "gravity_strength": 1.0,
            "time_dilation_coefficient": 1.0,
            "entropy_rate": 1.0
        }

    def update_config(self, key: str, value: float):
        """Updates a configuration parameter."""
        if key in self.config:
            self.config[key] = value

    def register_law(self, name: str, func: t.Callable):
        """Registers a new law (mathematical operation) to this manifold."""
        self.laws[name] = func

    def apply_law(self, law_name: str, *args, **kwargs):
        """Applies a registered law to the given arguments."""
        if law_name not in self.laws:
            raise AttributeError(f"The law '{law_name}' does not exist in the {self.name} manifold.")
        return self.laws[law_name](*args, **kwargs)

    def __repr__(self):
        return f"<Manifold: {self.name}>"

# Pre-defined Euclidean Manifold for testing
euclidean = Manifold("Euclidean")

def euclidean_add(a, b):
    # a and b are Axioms, we use their values
    return a.value + b.value

def antigravity_law(axiom):
    """
    Antigravity Law: Reduces 'Computational Weight' by cooling the data temperature.
    In the Euclidean context, it might also invert or scale the value to represent 'weightlessness'.
    """
    gravity = axiom.manifold.config.get("gravity_strength", 1.0)
    axiom.temperature *= 0.5 # Reduce heat/priority
    return axiom.value * -1 * gravity # Scaled by gravity config

def superposition_law(axiom):
    """
    Superposition Law: Allows an Axiom to be in multiple states.
    If the value is a callable, it's evaluated upon observation.
    """
    if callable(axiom.value):
        return axiom.value()
    return axiom.value

def relativity_law(axiom, velocity=0):
    """
    Relativity Law: Time dilation for high data mass or velocity.
    Simulates slowing down processing by adding an artificial delay or scaling impact.
    """
    # Simplified time dilation: factor = sqrt(1 - v^2/c^2). Let's say c=1.
    c = 1.0
    # Use config factor
    factor = axiom.manifold.config.get("time_dilation_coefficient", 1.0)
    
    if velocity >= c:
        return 0 # Time stops
    dilation_factor = (1 - (velocity**2 / c**2))**0.5
    return dilation_factor * factor

euclidean.register_law("add", euclidean_add)
euclidean.register_law("antigravity", antigravity_law)
euclidean.register_law("superposition", superposition_law)
euclidean.register_law("relativity", relativity_law)
