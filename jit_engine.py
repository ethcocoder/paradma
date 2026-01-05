import functools
import typing as t
import time
from .axiom import Axiom

# Try to import numba, fallback gracefully if not available
try:
    from numba import jit
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

def jit_law(nopython=True, parallel=False, cache=True):
    """
    Decorator to compile a Physics Law into machine code using Numba.
    Supports Multi-Core CPU Parallelism via 'parallel=True'.
    """
    def decorator(func: t.Callable):
        # If Numba is present, compile the function
        if HAS_NUMBA:
            compiled_func = jit(func, nopython=nopython, parallel=parallel, cache=cache)
        else:
            compiled_func = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 1. Measure Start Time
            # start = time.time()
            
            # 2. Argument Unpacking (Optional: Advanced logic could happen here)
            # The user is expected to pass primitives to the internal kernel
            
            # 3. Execution
            result = compiled_func(*args, **kwargs)
            
            # 4. Measure End Time (Metrics)
            # duration = time.time() - start
            # print(f"JIT Executed {func.__name__} in {duration:.6f}s")
            
            return result
        return wrapper
    return decorator
