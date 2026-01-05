from .axiom import Axiom
from .manifold import Manifold, euclidean
import typing as t
import numbers

class TensorAxiom(Axiom):
    """
    TensorAxiom: A Multi-Dimensional Axiom.
    Replaces np.array. It holds a structured grid of values but acts as a single
    living entity in the Paradma universe (has Temperature, Manifold, etc.).
    """
    def __init__(self, data: t.Union[t.List, numbers.Number, t.Any], manifold: Manifold = euclidean, **metadata):
        super().__init__(data, manifold, **metadata)
        self._shape = self._calculate_shape(data)
        self._is_dense = self._check_if_dense(data)

    def _check_if_dense(self, data):
        """Checks if the data is a dense buffer (NumPy array)."""
        try:
            import numpy as np
            return isinstance(data, np.ndarray)
        except ImportError:
            return False
    
    def _calculate_shape(self, data):
        """Recursively calculates the shape of the data."""
        if isinstance(data, (numbers.Number, str, bool)) or data is None:
            return ()
        if isinstance(data, list):
            if not data:
                return (0,)
            # recursive check
            outer_dim = len(data)
            inner_shape = self._calculate_shape(data[0])
            # verify consistency (simple check)
            for item in data[1:]:
                if self._calculate_shape(item) != inner_shape:
                    raise ValueError("Inconsistent shape in TensorAxiom data")
            return (outer_dim,) + inner_shape
        
        # Support for NumPy arrays
        try:
            import numpy as np
            if isinstance(data, np.ndarray):
                return data.shape
        except ImportError:
            pass
            
        return ()

    @property
    def shape(self):
        return self._shape

    @property
    def ndim(self):
        return len(self._shape)
    
    @property
    def size(self):
        s = 1
        for dim in self.shape:
            s *= dim
        return s

    def __getitem__(self, key):
        """
        Implements Slicing and Indexing.
        Returns a new TensorAxiom representing the View.
        """
        # We'll rely on basic list slicing for the MVP perfect implementation
        # For multi-dim slicing (e.g. [:, 1]), we need recursive helper
        if self.ndim == 0:
             raise IndexError("0-d tensor has no items")
        
        if isinstance(key, int):
            # Select simple row
            return TensorAxiom(self.value[key], self.manifold, **self.metadata)
        
        if isinstance(key, slice):
            return TensorAxiom(self.value[key], self.manifold, **self.metadata)
            
        if isinstance(key, tuple):
            # Complex slicing [0, 1] or [:, 0]
            # This requires a deeper "get_view" implementation logic
            # For Phase 1 MVP, let's implement basic tuple indexing
            current_data = self.value
            try:
                for k in key:
                    current_data = current_data[k]
            except (IndexError, TypeError):
                 raise IndexError(f"Index {key} out of bounds for tensor of shape {self.shape}")
            return TensorAxiom(current_data, self.manifold, **self.metadata)
            
        raise TypeError(f"Invalid index type: {type(key)}")

    def __add__(self, other):
        """
        Broadcasting Addition.
        """
        # 1. Scalar Broadcasting
        if isinstance(other, (int, float)):
            # Recursive addition
            new_data = self._recursive_op(self.value, other, lambda x, y: x + y)
            return TensorAxiom(new_data, self.manifold)
        
        # 2. Tensor Addition (Element-wise)
        if isinstance(other, TensorAxiom):
            if other.shape != self.shape:
                raise ValueError(f"Shapes {self.shape} and {other.shape} not aligned for basic add (Broadcasting v2 Pending)")
            
            new_data = self._recursive_tensor_op(self.value, other.value, lambda x, y: x + y)
            return TensorAxiom(new_data, self.manifold)
            
        return super().__add__(other)

    def _recursive_op(self, data, scalar, op):
        if isinstance(data, list):
            return [self._recursive_op(item, scalar, op) for item in data]
        return op(data, scalar)

    def _recursive_tensor_op(self, data1, data2, op):
        if isinstance(data1, list) and isinstance(data2, list):
             return [self._recursive_tensor_op(x, y, op) for x, y in zip(data1, data2)]
        return op(data1, data2)

    def __repr__(self):
        # Format similar to Numpy
        return f"Tensor(shape={self.shape}, dtype={type(self._flat_sample()).__name__})\n{self.value}"

    def _flat_sample(self):
        """Helper to find one value for type checking"""
        d = self.value
        if self._is_dense:
            return d.flatten()[0] if d.size > 0 else None
            
        while isinstance(d, list):
            if not d: return None
            d = d[0]
        return d

    def condense(self):
        """
        'Condensation': Converts a nested list of data into a high-speed NumPy Buffer.
        Transitions the Axiom from 'Gas' to 'Solid'.
        """
        import numpy as np
        if self._is_dense:
            return self
        
        self._value = np.array(self._value)
        self._is_dense = True
        return self

    def evaporate(self):
        """
        'Evaporation': Converts a dense buffer back into a nested list of living Axioms.
        Transitions the Axiom from 'Solid' to 'Gas'.
        """
        if not self._is_dense:
            return self
        
        self._value = self._value.tolist()
        self._is_dense = False
        return self
