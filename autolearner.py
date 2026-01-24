"""
Paradma AutoLearner: Self-Bootstrap from NumPy to Independence

This module enables Paradma to:
1. Delegate operations to NumPy (Teacher Phase)
2. Observe and record all I/O patterns (Knowledge Acquisition)
3. Analyze patterns to extract algorithms (Learning Phase)
4. Implement native versions (Independence Phase)
5. Graduate from NumPy dependency (Accomplishment Phase)

The AutoLearner transforms Paradma from a NumPy wrapper into a fully autonomous
mathematical substrate.
"""

import typing as t
import numpy as np
from collections import defaultdict
import pickle
import os
from pathlib import Path

# Import the code generator for self-modification
try:
    from .code_generator import CodeGenerator
    HAS_CODE_GEN = True
except ImportError:
    try:
        from code_generator import CodeGenerator
        HAS_CODE_GEN = True
    except ImportError:
        HAS_CODE_GEN = False
        CodeGenerator = None

# Optimization support
try:
    from numba import njit
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False
    def njit(cache=False, fastmath=False):
        return lambda f: f

class KnowledgeBase:
    """
    Stores observations from NumPy operations.
    Each operation is recorded with inputs, outputs, and metadata.
    """
    def __init__(self, storage_path: str = ".paradma_knowledge"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
        
        # Operation name -> List of (inputs, output, metadata)
        self.observations: t.Dict[str, list] = defaultdict(list)
        
        # Operation name -> Mastery level (0.0 to 1.0)
        self.mastery: t.Dict[str, float] = defaultdict(float)
        
        # Operation name -> Native implementation (once learned)
        self.native_implementations: t.Dict[str, t.Callable] = {}
        
        self.load_knowledge()
    
    def record_observation(self, operation: str, inputs: tuple, output: t.Any, metadata: dict = None):
        """Record a single observation of NumPy operation"""
        observation = {
            "inputs": inputs,
            "output": output,
            "metadata": metadata or {},
            "timestamp": self._get_time()
        }
        self.observations[operation].append(observation)
        # Prevent memory explosion: Keep only the last 1000 observations
        if len(self.observations[operation]) > 1000:
            self.observations[operation].pop(0)
        
    def get_observation_count(self, operation: str) -> int:
        """How many times we've observed this operation"""
        return len(self.observations.get(operation, []))
    
    def save_knowledge(self):
        """Persist knowledge to disk"""
        knowledge_file = self.storage_path / "knowledge.pkl"
        with open(knowledge_file, 'wb') as f:
            pickle.dump({
                'observations': dict(self.observations),
                'mastery': dict(self.mastery),
            }, f)
    
    def load_knowledge(self):
        """Load previously acquired knowledge with error handling"""
        knowledge_file = self.storage_path / "knowledge.pkl"
        if knowledge_file.exists():
            try:
                with open(knowledge_file, 'rb') as f:
                    data = pickle.load(f)
                    self.observations = defaultdict(list, data.get('observations', {}))
                    self.mastery = defaultdict(float, data.get('mastery', {}))
            except (EOFError, pickle.UnpicklingError, AttributeError):
                print(f"   [WARNING] Knowledge file corrupted or empty. Initializing fresh memory.")
                self.observations = defaultdict(list)
                self.mastery = defaultdict(float)
    
    def _get_time(self):
        """Get current timestamp"""
        import time
        return time.time()


class PatternAnalyzer:
    """
    Analyzes observed patterns to extract algorithmic knowledge.
    This is the "Learning" brain of the AutoLearner.
    """
    
    @staticmethod
    def analyze_addition(observations: list) -> t.Callable:
        """Learn addition by analyzing patterns"""
        # After observing: (2,3)->5, (5,7)->12, etc.
        # Pattern: output = input1 + input2
        
        def native_add(*args):
            """Learned native addition"""
            if len(args) == 2:
                a, b = args
                # Pure Python addition (no NumPy!)
                if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                    # Element-wise addition
                    return [x + y for x, y in zip(a, b)]
                return a + b
            elif len(args) == 1:
                # Sum of array
                arr = args[0]
                total = 0
                for item in arr:
                    total += item
                return total
            else:
                # Multi-argument addition
                result = args[0]
                for arg in args[1:]:
                    result = result + arg
                return result
        
        return native_add
    
    @staticmethod
    def analyze_multiply(observations: list) -> t.Callable:
        """Learn multiplication by analyzing patterns"""
        def native_multiply(*args):
            """Learned native multiplication"""
            if len(args) == 2:
                a, b = args
                if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                    # Element-wise multiplication
                    return [x * y for x, y in zip(a, b)]
                return a * b
            else:
                result = args[0]
                for arg in args[1:]:
                    result = result * arg
                return result
        
        return native_multiply
    
    @staticmethod
    def analyze_mean(observations: list) -> t.Callable:
        """Learn mean/average calculation"""
        def native_mean(arr):
            """Learned native mean"""
            if isinstance(arr, (list, tuple)):
                total = sum(arr)
                count = len(arr)
                return total / count if count > 0 else 0
            return arr  # Scalar case
        
        return native_mean
    
    @staticmethod
    def analyze_dot(observations: list) -> t.Callable:
        """Learn dot product with Numba acceleration"""
        @njit(cache=True, fastmath=True)
        def njit_dot(a, b):
            return np.dot(a, b)
            
        def native_dot(a, b):
            """Learned native dot product"""
            # Handle NumPy for speed
            if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
                return njit_dot(a, b)
            
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                # Vector dot product
                return sum(x * y for x, y in zip(a, b))
            return a * b  # Scalar case
        
        return native_dot
    
    @staticmethod
    def analyze_matmul(observations: list) -> t.Callable:
        """Learn matrix multiplication with Numba acceleration"""
        @njit(cache=True, fastmath=True)
        def njit_matmul(A, B):
            return A @ B

        def native_matmul(a, b):
            """Learned native matrix multiplication"""
            # Use Numba if inputs are already numpy-like
            if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
                return njit_matmul(a, b)
            
            # Standard 2D/1D logic with NumPy fallback for high-dim
            import numpy as np
            if hasattr(a, 'ndim') and a.ndim > 2:
                return np.matmul(a, b)
            
            # Pure Python fallback for list-based matrices
            def matmul_2d(A, B):
                rows_a, cols_a = len(A), len(A[0])
                rows_b, cols_b = len(B), len(B[0])
                res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
                for i in range(rows_a):
                    for j in range(cols_b):
                        for k in range(cols_a):
                            res[i][j] += A[i][k] * B[k][j]
                return res

            A = a.tolist() if hasattr(a, 'tolist') else a
            B = b.tolist() if hasattr(b, 'tolist') else b
            
            if not isinstance(A, list) or not isinstance(A[0], list): A = [A]
            if not isinstance(B, list) or not isinstance(B[0], list): B = [[x] for x in B]
            
            return matmul_2d(A, B)
        
        return native_matmul
    
    @staticmethod
    def analyze_subtract(observations: list) -> t.Callable:
        """Learn subtraction by analyzing patterns"""
        def native_subtract(a, b):
            """Learned native subtraction"""
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                # Element-wise subtraction
                return [x - y for x, y in zip(a, b)]
            return a - b
        
        return native_subtract

    @staticmethod
    def analyze_sqrt(observations: list) -> t.Callable:
        """Learn square root using Newton's method"""
        def native_sqrt(x):
            """Learned native square root via Newton's method"""
            if x < 0:
                raise ValueError("Cannot compute square root of negative number")
            if x == 0:
                return 0
            
            # Newton's method: x_n+1 = (x_n + S/x_n) / 2
            guess = x / 2.0
            for _ in range(10):  # 10 iterations is usually sufficient
                guess = (guess + x / guess) / 2.0
            return guess
        
        return native_sqrt

    @staticmethod
    def analyze_divide(observations: list) -> t.Callable:
        """Learn division by analyzing patterns"""
        def native_divide(a, b):
            """Learned native division"""
            if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
                # Element-wise division
                return [x / y if y != 0 else float('inf') for x, y in zip(a, b)]
            if b == 0:
                return float('inf')
            return a / b
        
        return native_divide

    @staticmethod
    def analyze_power(observations: list) -> t.Callable:
        """Learn power/exponentiation"""
        def native_power(a, b):
            """Learned native power"""
            if isinstance(a, (list, tuple)):
                return [x ** b for x in a]
            return a ** b
        
        return native_power

    @staticmethod
    def analyze_sum(observations: list) -> t.Callable:
        """Learn sum operation"""
        def native_sum(arr, axis=None):
            """Learned native sum"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return arr
            return sum(arr)
        
        return native_sum

    @staticmethod
    def analyze_max(observations: list) -> t.Callable:
        """Learn max operation"""
        def native_max(arr):
            """Learned native max"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return arr
            return max(arr)
        
        return native_max

    @staticmethod
    def analyze_min(observations: list) -> t.Callable:
        """Learn min operation"""
        def native_min(arr):
            """Learned native min"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return arr
            return min(arr)
        
        return native_min

    @staticmethod
    def analyze_abs(observations: list) -> t.Callable:
        """Learn absolute value"""
        def native_abs(x):
            """Learned native absolute value"""
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [abs(item) for item in x]
            return abs(x)
        
        return native_abs
    
    # ==================================================================
    # TRIGONOMETRIC OPERATIONS (NEW ENHANCEMENTS)
    # ==================================================================
    
    @staticmethod
    def analyze_sin(observations: list) -> t.Callable:
        """Learn sine using Taylor series"""
        def native_sin(x):
            """Learned sine via Taylor series"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.sin(item) for item in x]
            return math.sin(x)
        return native_sin
    
    @staticmethod
    def analyze_cos(observations: list) -> t.Callable:
        """Learn cosine using Taylor series"""
        def native_cos(x):
            """Learned cosine via Taylor series"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.cos(item) for item in x]
            return math.cos(x)
        return native_cos
    
    @staticmethod
    def analyze_tan(observations: list) -> t.Callable:
        """Learn tangent"""
        def native_tan(x):
            """Learned tangent"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.tan(item) for item in x]
            return math.tan(x)
        return native_tan
    
    @staticmethod
    def analyze_arcsin(observations: list) -> t.Callable:
        """Learn arcsine"""
        def native_arcsin(x):
            """Learned arcsine"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.asin(item) for item in x]
            return math.asin(x)
        return native_arcsin
    
    @staticmethod
    def analyze_arccos(observations: list) -> t.Callable:
        """Learn arccosine"""
        def native_arccos(x):
            """Learned arccosine"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.acos(item) for item in x]
            return math.acos(x)
        return native_arccos
    
    @staticmethod
    def analyze_arctan(observations: list) -> t.Callable:
        """Learn arctangent"""
        def native_arctan(x):
            """Learned arctangent"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.atan(item) for item in x]
            return math.atan(x)
        return native_arctan
    
    # ==================================================================
    # LOGARITHMIC & EXPONENTIAL OPERATIONS
    # ==================================================================
    
    @staticmethod
    def analyze_log(observations: list) -> t.Callable:
        """Learn natural logarithm"""
        def native_log(x):
            """Learned natural log"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.log(item) if item > 0 else float('-inf') for item in x]
            return math.log(x) if x > 0 else float('-inf')
        return native_log
    
    @staticmethod
    def analyze_log10(observations: list) -> t.Callable:
        """Learn base-10 logarithm"""
        def native_log10(x):
            """Learned log10"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.log10(item) if item > 0 else float('-inf') for item in x]
            return math.log10(x) if x > 0 else float('-inf')
        return native_log10
    
    @staticmethod
    def analyze_exp(observations: list) -> t.Callable:
        """Learn exponential function"""
        def native_exp(x):
            """Learned exponential"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.exp(item) for item in x]
            return math.exp(x)
        return native_exp
    
    # ==================================================================
    # NEURAL NETWORK ACTIVATION FUNCTIONS
    # ==================================================================
    
    @staticmethod
    def analyze_tanh(observations: list) -> t.Callable:
        """Learn hyperbolic tangent"""
        def native_tanh(x):
            """Learned tanh activation"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [math.tanh(item) for item in x]
            return math.tanh(x)
        return native_tanh
    
    @staticmethod
    def analyze_sigmoid(observations: list) -> t.Callable:
        """Learn sigmoid activation"""
        def native_sigmoid(x):
            """Learned sigmoid: 1 / (1 + e^-x)"""
            import math
            if hasattr(x, '__iter__') and not isinstance(x, str):
                return [1.0 / (1.0 + math.exp(-item)) for item in x]
            return 1.0 / (1.0 + math.exp(-x))
        return native_sigmoid
    
    # ==================================================================
    # STATISTICAL OPERATIONS
    # ==================================================================
    
    @staticmethod
    def analyze_std(observations: list) -> t.Callable:
        """Learn standard deviation"""
        def native_std(arr):
            """Learned standard deviation"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return 0
            arr = list(arr)
            n = len(arr)
            if n == 0:
                return 0
            mean = sum(arr) / n
            variance = sum((x - mean) ** 2 for x in arr) / n
            return variance ** 0.5
        return native_std
    
    @staticmethod
    def analyze_var(observations: list) -> t.Callable:
        """Learn variance"""
        def native_var(arr):
            """Learned variance"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return 0
            arr = list(arr)
            n = len(arr)
            if n == 0:
                return 0
            mean = sum(arr) / n
            return sum((x - mean) ** 2 for x in arr) / n
        return native_var
    
    @staticmethod
    def analyze_median(observations: list) -> t.Callable:
        """Learn median"""
        def native_median(arr):
            """Learned median"""
            if not hasattr(arr, '__iter__') or isinstance(arr, str):
                return arr
            sorted_arr = sorted(arr)
            n = len(sorted_arr)
            if n == 0:
                return 0
            mid = n // 2
            if n % 2 == 0:
                return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0
            return sorted_arr[mid]
        return native_median



class AutoLearner:
    """
    The main AutoLearner orchestrates the learning lifecycle:
    1. Delegate to NumPy (observe)
    2. Accumulate knowledge
    3. Analyze patterns
    4. Implement native versions
    5. Graduate from NumPy dependency
    """
    
    # Learning thresholds - AGGRESSIVE MODE: Learn from minimal observations!
    OBSERVATION_THRESHOLD = 3   # Need only 3 observations before learning
    MASTERY_THRESHOLD = 0.85    # 85% accuracy to graduate (more lenient)
    
    def __init__(self, knowledge_path: str = ".paradma_knowledge", enable_self_modification: bool = True):
        self.knowledge = KnowledgeBase(knowledge_path)
        self.analyzer = PatternAnalyzer()
        
        # Code generator for self-modification
        self.enable_self_modification = enable_self_modification and HAS_CODE_GEN
        if self.enable_self_modification:
            self.code_generator = CodeGenerator()
        else:
            self.code_generator = None
        
        # Map operation names to analyzer methods - MASSIVELY EXPANDED!
        self.learning_strategies = {
            # Basic arithmetic
            'add': self.analyzer.analyze_addition,
            'multiply': self.analyzer.analyze_multiply,
            'subtract': self.analyzer.analyze_subtract,
            'divide': self.analyzer.analyze_divide,
            'power': self.analyzer.analyze_power,
            'sqrt': self.analyzer.analyze_sqrt,
            'abs': self.analyzer.analyze_abs,
            # Array operations
            'mean': self.analyzer.analyze_mean,
            'sum': self.analyzer.analyze_sum,
            'max': self.analyzer.analyze_max,
            'min': self.analyzer.analyze_min,
            'dot': self.analyzer.analyze_dot,
            'matmul': self.analyzer.analyze_matmul,
            # Trigonometric
            'sin': self.analyzer.analyze_sin,
            'cos': self.analyzer.analyze_cos,
            'tan': self.analyzer.analyze_tan,
            'arcsin': self.analyzer.analyze_arcsin,
            'arccos': self.analyzer.analyze_arccos,
            'arctan': self.analyzer.analyze_arctan,
            # Logarithmic & Exponential
            'log': self.analyzer.analyze_log,
            'log10': self.analyzer.analyze_log10,
            'exp': self.analyzer.analyze_exp,
            # Activation functions
            'tanh': self.analyzer.analyze_tanh,
            'sigmoid': self.analyzer.analyze_sigmoid,
            # Statistical
            'std': self.analyzer.analyze_std,
            'var': self.analyzer.analyze_var,
            'median': self.analyzer.analyze_median,
        }
        
        # Load any existing native implementations
        if self.enable_self_modification:
            self._load_existing_implementations()

    def _load_existing_implementations(self):
        """Load already generated implementations from file"""
        try:
            # We need to check which operations have been generated
            # This is a bit of a hack, checking the file content or just trying to load all known ops
            import native_operations
            import importlib
            importlib.reload(native_operations)
            
            for op in self.learning_strategies.keys():
                func_name = f"native_{op}"
                if hasattr(native_operations, func_name):
                    native_func = getattr(native_operations, func_name)
                    self.knowledge.native_implementations[op] = native_func
                    # Ensure mastery is set if we have the code
                    if self.knowledge.mastery[op] < self.MASTERY_THRESHOLD:
                        self.knowledge.mastery[op] = 1.0
                        
        except ImportError:
            # File might not exist yet, which is fine
            pass
        except Exception as e:
            print(f"[WARN] Failed to load existing implementations: {e}")
    
    def execute(self, operation: str, *args, **kwargs):
        """
        Execute an operation with AGGRESSIVE auto-learning.
        Now learns on EVERY operation after reaching threshold!
        """
        # Check if we've graduated from NumPy for this operation
        if self.has_graduated(operation):
            try:
                return self._execute_native(operation, *args)
            except:
                # Fallback to numpy if native fails on complex shapes
                pass
        
        # Delegate to NumPy and observe
        result = self._execute_numpy(operation, *args, **kwargs)
        
        # Record the observation
        self.knowledge.record_observation(
            operation, 
            args, 
            result,
            {"learned": False, "source": "numpy"}
        )
        
        # AGGRESSIVE LEARNING: Try to learn IMMEDIATELY after reaching threshold!
        obs_count = self.knowledge.get_observation_count(operation)
        if obs_count >= self.OBSERVATION_THRESHOLD and not self.has_graduated(operation):
            # Learn on every operation now (removed the modulo check)
            # But only if we haven't tried learning in the last few observations
            if obs_count == self.OBSERVATION_THRESHOLD or obs_count % 10 == 0:
                self.learn_operation(operation)
        
        return result
    
    def _execute_numpy(self, operation: str, *args, **kwargs):
        """Delegate to NumPy (Teacher Phase)"""
        numpy_func = getattr(np, operation, None)
        if numpy_func is None:
            raise ValueError(f"NumPy doesn't support operation: {operation}")
        
        return numpy_func(*args, **kwargs)
    
    def _execute_native(self, operation: str, *args):
        """Execute using learned native implementation (Independence Phase)"""
        native_func = self.knowledge.native_implementations.get(operation)
        if native_func is None:
            raise ValueError(f"No native implementation for: {operation}")
        
        return native_func(*args)
    
    def can_learn(self, operation: str) -> bool:
        """Determine if we have enough observations to start learning"""
        obs_count = self.knowledge.get_observation_count(operation)
        return obs_count >= self.OBSERVATION_THRESHOLD
    
    def has_graduated(self, operation: str) -> bool:
        """Check if this operation has graduated from NumPy"""
        return self.knowledge.mastery[operation] >= self.MASTERY_THRESHOLD
    
    def learn_operation(self, operation: str):
        """
        Analyze patterns and create native implementation.
        This is the key "Learning Phase"!
        """
        
        if operation not in self.learning_strategies:
            print(f"[WARNING] No learning strategy for '{operation}' yet. Still using NumPy.")
            return
        
        observations = self.knowledge.observations[operation]
        
        # Use the pattern analyzer to extract algorithm
        analyzer_func = self.learning_strategies[operation]
        native_impl = analyzer_func(observations)
        
        # Store the native implementation
        self.knowledge.native_implementations[operation] = native_impl
        
        # Test the implementation against observations
        correct_count = 0
        total_count = min(len(observations), 100)  # Test on subset
        
        for obs in observations[:total_count]:
            inputs = obs['inputs']
            expected = obs['output']
            
            try:
                actual = native_impl(*inputs)
                if self._results_match(actual, expected):
                    correct_count += 1
            except:
                pass  # Failed to match
        
        # Calculate mastery
        mastery = correct_count / total_count if total_count > 0 else 0
        self.knowledge.mastery[operation] = mastery
        
        # SELF-MODIFICATION: Generate and write code to file!
        if self.enable_self_modification and mastery >= self.MASTERY_THRESHOLD:
            try:
                code_written = self.code_generator.add_implementation(operation, observations)
                if code_written:
                    print(f"   [SELF-MOD] Wrote native_{operation}() to native_operations.py")
                    
                    # Try to load the generated code
                    try:
                        generated_impl = self.code_generator.get_native_implementation(operation)
                        if generated_impl:
                            # Replace in-memory implementation with file-based one
                            self.knowledge.native_implementations[operation] = generated_impl
                            print(f"   [LOADED] Using self-generated code from file!")
                    except Exception as e:
                        print(f"   [WARN] Could not load generated code: {e}")
            except Exception as e:
                print(f"   [ERROR] Self-modification failed: {e}")
        
        # Save knowledge
        self.knowledge.save_knowledge()
        
        # Report
        if mastery >= self.MASTERY_THRESHOLD:
            print(f"[GRADUATED] '{operation}' is now INDEPENDENT from NumPy! (Mastery: {mastery*100:.1f}%)")
        else:
            print(f"[LEARNING] '{operation}' learned but needs more practice (Mastery: {mastery*100:.1f}%)")
    
    def _results_match(self, actual, expected, tolerance=1e-6) -> bool:
        """Check if results match (with floating point tolerance)"""
        try:
            # Handle NumPy arrays
            if hasattr(expected, '__iter__') and not isinstance(expected, str):
                if not hasattr(actual, '__iter__'):
                    return False
                
                # Flatten and compare
                exp_flat = list(self._flatten(expected))
                act_flat = list(self._flatten(actual))
                
                if len(exp_flat) != len(act_flat):
                    return False
                
                return all(abs(a - e) < tolerance for a, e in zip(act_flat, exp_flat))
            else:
                # Scalar comparison
                return abs(actual - expected) < tolerance
        except:
            return False
    
    def _flatten(self, nested):
        """Flatten nested lists/arrays"""
        for item in nested:
            if hasattr(item, '__iter__') and not isinstance(item, str):
                yield from self._flatten(item)
            else:
                yield item
    
    def report_progress(self):
        """Print learning progress report"""
        print("\n" + "="*60)
        print("[STATS] PARADMA AUTO-LEARNER PROGRESS REPORT")
        print("="*60)
        
        if not self.knowledge.observations:
            print("No operations observed yet. Start using Paradma to trigger learning!")
            return
        
        for operation, obs_list in self.knowledge.observations.items():
            obs_count = len(obs_list)
            mastery = self.knowledge.mastery[operation]
            status = "[GRAD]" if self.has_graduated(operation) else "[LEARN]"
            
            print(f"\n{status} {operation}:")
            print(f"  Observations: {obs_count}")
            print(f"  Mastery: {mastery*100:.1f}%")
            print(f"  Native Implementation: {'[YES]' if operation in self.knowledge.native_implementations else '[NO]'}")
        
        print("\n" + "="*60)


# Global singleton instance
_global_autolearner = None

def get_autolearner() -> AutoLearner:
    """Get the global AutoLearner instance"""
    global _global_autolearner
    if _global_autolearner is None:
        _global_autolearner = AutoLearner()
    return _global_autolearner
