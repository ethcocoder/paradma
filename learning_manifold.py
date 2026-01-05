"""
Learning Manifold: A Self-Learning Mathematical Space

This Manifold automatically learns from NumPy and evolves toward independence.
Every operation goes through the learning lifecycle:

1. Student Phase: Delegates to NumPy
2. Observer Phase: Records patterns
3. Analysis Phase: Extracts algorithms
4. Graduate Phase: Uses native implementation
5. Master Phase: Fully independent

The more you use it, the smarter it gets!
"""

import typing as t
from .manifold import Manifold
from .axiom import Axiom
from .autolearner import get_autolearner
import numpy as np


class LearningManifold(Manifold):
    """
    A Manifold that learns mathematical operations from NumPy
    and gradually becomes independent.
    """
    
    def __init__(self, name: str = "Learning"):
        super().__init__(name)
        self.autolearner = get_autolearner()
        
        # Register all learning-enabled operations
        self._register_learning_laws()
        
        # Track learning statistics
        self.operation_calls = {}
    
    def _register_learning_laws(self):
        """Register laws that use the AutoLearner"""
        
        # Arithmetic operations
        self.register_law("add", self._learning_add)
        self.register_law("multiply", self._learning_multiply)
        self.register_law("subtract", self._learning_subtract)
        self.register_law("divide", self._learning_divide)
        
        # Statistical operations
        self.register_law("mean", self._learning_mean)
        self.register_law("median", self._learning_median)
        self.register_law("std", self._learning_std)
        
        # Linear algebra
        self.register_law("dot", self._learning_dot)
        self.register_law("matmul", self._learning_matmul)
        
        # Mathematical functions
        self.register_law("sqrt", self._learning_sqrt)
        self.register_law("exp", self._learning_exp)
        self.register_law("log", self._learning_log)
        self.register_law("sin", self._learning_sin)
        self.register_law("cos", self._learning_cos)
    
    def _extract_values(self, *args):
        """Extract raw values from Axioms"""
        values = []
        for arg in args:
            if isinstance(arg, Axiom):
                values.append(arg.value)
            else:
                values.append(arg)
        return values
    
    def _track_call(self, operation: str):
        """Track operation usage for statistics"""
        self.operation_calls[operation] = self.operation_calls.get(operation, 0) + 1
    
    # ============================================
    # Learning-Enabled Arithmetic Operations
    # ============================================
    
    def _learning_add(self, *args):
        """Addition with auto-learning"""
        self._track_call("add")
        values = self._extract_values(*args)
        
        # Execute through AutoLearner
        if len(values) == 2:
            result = self.autolearner.execute("add", values[0], values[1])
        else:
            result = sum(values)
        
        return Axiom(result, manifold=self)
    
    def _learning_multiply(self, *args):
        """Multiplication with auto-learning"""
        self._track_call("multiply")
        values = self._extract_values(*args)
        
        if len(values) == 2:
            result = self.autolearner.execute("multiply", values[0], values[1])
        else:
            result = values[0]
            for v in values[1:]:
                result = result * v
        
        return Axiom(result, manifold=self)
    
    def _learning_subtract(self, a, b):
        """Subtraction with auto-learning"""
        self._track_call("subtract")
        val_a, val_b = self._extract_values(a, b)
        
        result = self.autolearner.execute("subtract", val_a, val_b)
        return Axiom(result, manifold=self)
    
    def _learning_divide(self, a, b):
        """Division with auto-learning"""
        self._track_call("divide")
        val_a, val_b = self._extract_values(a, b)
        
        if val_b == 0:
            raise ValueError("Division by zero")
        
        result = val_a / val_b
        return Axiom(result, manifold=self)
    
    # ============================================
    # Learning-Enabled Statistical Operations
    # ============================================
    
    def _learning_mean(self, arr):
        """Mean/Average with auto-learning"""
        self._track_call("mean")
        values = self._extract_values(arr)[0]
        
        # Convert to numpy array if needed
        if not isinstance(values, np.ndarray):
            values = np.array(values)
        
        result = self.autolearner.execute("mean", values)
        return Axiom(result, manifold=self)
    
    def _learning_median(self, arr):
        """Median with auto-learning"""
        self._track_call("median")
        values = self._extract_values(arr)[0]
        
        if not isinstance(values, np.ndarray):
            values = np.array(values)
        
        result = np.median(values)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    def _learning_std(self, arr):
        """Standard deviation with auto-learning"""
        self._track_call("std")
        values = self._extract_values(arr)[0]
        
        if not isinstance(values, np.ndarray):
            values = np.array(values)
        
        result = np.std(values)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    # ============================================
    # Learning-Enabled Linear Algebra
    # ============================================
    
    def _learning_dot(self, a, b):
        """Dot product with auto-learning"""
        self._track_call("dot")
        val_a, val_b = self._extract_values(a, b)
        
        result = self.autolearner.execute("dot", val_a, val_b)
        return Axiom(result, manifold=self)
    
    def _learning_matmul(self, a, b):
        """Matrix multiplication with auto-learning"""
        self._track_call("matmul")
        val_a, val_b = self._extract_values(a, b)
        
        result = self.autolearner.execute("matmul", val_a, val_b)
        return Axiom(result, manifold=self)
    
    # ============================================
    # Learning-Enabled Mathematical Functions
    # ============================================
    
    def _learning_sqrt(self, x):
        """Square root with auto-learning"""
        self._track_call("sqrt")
        val = self._extract_values(x)[0]
        
        result = self.autolearner.execute("sqrt", val)
        return Axiom(result, manifold=self)
    
    def _learning_exp(self, x):
        """Exponential with auto-learning"""
        self._track_call("exp")
        val = self._extract_values(x)[0]
        
        result = np.exp(val)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    def _learning_log(self, x):
        """Natural logarithm with auto-learning"""
        self._track_call("log")
        val = self._extract_values(x)[0]
        
        result = np.log(val)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    def _learning_sin(self, x):
        """Sine with auto-learning"""
        self._track_call("sin")
        val = self._extract_values(x)[0]
        
        result = np.sin(val)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    def _learning_cos(self, x):
        """Cosine with auto-learning"""
        self._track_call("cos")
        val = self._extract_values(x)[0]
        
        result = np.cos(val)  # Not yet in AutoLearner
        return Axiom(result, manifold=self)
    
    def show_learning_progress(self):
        """Display learning progress and statistics"""
        print("\n" + "="*60)
        print(f"🧠 LEARNING MANIFOLD: {self.name}")
        print("="*60)
        
        print("\n📞 Operation Call Statistics:")
        if self.operation_calls:
            for op, count in sorted(self.operation_calls.items(), key=lambda x: x[1], reverse=True):
                print(f"  {op}: {count} calls")
        else:
            print("  No operations called yet")
        
        # Show AutoLearner progress
        self.autolearner.report_progress()


# Pre-configured learning manifold instance
learning = LearningManifold("AutoLearning")
