from .manifold import Manifold
from .tensor import TensorAxiom
from .efficiency import observer
import random
import math

class StochasticManifold(Manifold):
    """
    Manifold for Randomness and Chaos.
    Replaces np.random.
    """
    def __init__(self, name: str = "MonteCarlo"):
        super().__init__(name)
        self.register_law("uniform", self.uniform)
        self.register_law("normal", self.normal)
        self.register_law("chaos", self.chaos)

    def uniform(self, shape: tuple, low=0.0, high=1.0):
        """Generates a TensorAxiom with uniform random values."""
        data = self._recursive_gen(shape, lambda: random.uniform(low, high))
        return TensorAxiom(data, self)

    def normal(self, shape: tuple, mean=0.0, std_dev=1.0):
        """Generates a TensorAxiom with Gaussian random values."""
        data = self._recursive_gen(shape, lambda: random.gauss(mean, std_dev))
        return TensorAxiom(data, self)

    def chaos(self, shape: tuple, low=0.0, high=1.0):
        """
        Generates a 'Superposed' Tensor.
        The values are NOT determined yet. They are lambdas.
        Use observe() to collapse the wavefunction.
        """
        # Unique to Paradma: Returns functions, not numbers
        def generator():
            return random.uniform(low, high)
        
        # We need a special logic here given TensorAxiom expects data.
        # But if we pass lambdas, TensorAxiom might fail shape calculation if strict.
        # TensorAxiom.shape calculation handles simple types.
        # We'll need to bypass or ensure TensorAxiom handles callables as 'scalars'.
        # For now, let's just generate values on Observe?
        # Actually, let's make it simple: Chaos means the value IS a lambda.
        
        data = self._recursive_gen(shape, lambda: generator)
        return TensorAxiom(data, self)

    def _recursive_gen(self, shape, generator_func):
        if not shape:
            return generator_func()
        return [self._recursive_gen(shape[1:], generator_func) for _ in range(shape[0])]
