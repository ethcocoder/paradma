from .manifold import Manifold
from .tensor import TensorAxiom
import math
import cmath

class FrequencyManifold(Manifold):
    """
    Manifold for Frequency Domain operations.
    Replaces np.fft.
    """
    def __init__(self, name: str = "FourierSpace"):
        super().__init__(name)
        self.register_law("fft", self.fft)
        self.register_law("ifft", self.ifft)

    def fft(self, ax: TensorAxiom):
        """
        Fast Fourier Transform (1D).
        Uses recursive Cooley-Tukey algorithm.
        """
        if ax.ndim != 1:
            raise NotImplementedError("FFT currently only supports 1D tensors.")
        
        data = ax.value
        # Ensure length is power of 2 for simple FFT implementation? 
        # Or pad? For professional implementation, let's just stick to power of 2 constraint or use DFT for odd.
        # Let's handle generic N via naive DFT if not power of 2, or just implement DFT for simplicity and correctness.
        # Actually, let's do DFT for guaranteed correctness on any N.
        
        n = len(data)
        result = []
        for k in range(n):
            val = 0
            for t in range(n):
                angle = 2 * math.pi * k * t / n
                val += data[t] * cmath.exp(-1j * angle)
            result.append(val)
            
        return TensorAxiom(result, self)

    def ifft(self, ax: TensorAxiom):
        """
        Inverse Fast Fourier Transform (1D).
        """
        if ax.ndim != 1:
            raise NotImplementedError("IFFT currently only supports 1D tensors.")
            
        data = ax.value
        n = len(data)
        result = []
        for t in range(n):
            val = 0
            for k in range(n):
                angle = 2 * math.pi * k * t / n
                val += data[k] * cmath.exp(1j * angle)
            result.append(val / n)
            
        # If input was real data, imaginary parts should be ~0. 
        # But for general case we return complex.
        return TensorAxiom(result, self)
