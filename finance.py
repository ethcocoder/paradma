from .manifold import Manifold
from .axiom import Axiom
import time
import math
import typing as t

class FinanceManifold(Manifold):
    """
    A specialized Manifold for High-Frequency Trading (HFT) and Financial analysis.
    It replaces NumPy arrays with living, self-cleaning Market Axioms.
    """
    def __init__(self, name: str = "WallStreet"):
        super().__init__(name)
        # Initialize default finance config
        self.config["ttl"] = 60.0
        
        # Register default laws
        self.register_law("volatility", self.calculate_volatility)
        self.register_law("ma", self.calculate_moving_average)
        self.register_law("decay", self.apply_entropy)

    def calculate_volatility(self, axiom_group: t.List[Axiom], window: int = 10):
        """
        Calculates standard deviation (volatility) of a group of Axioms.
        Replaces np.std().
        """
        # Extract values
        values = [a.value for a in axiom_group[-window:] if a.value is not None]
        if not values:
            return 0.0
        
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)

    def calculate_moving_average(self, axiom_group: t.List[Axiom], window: int = 5):
        """
        Calculates Simple Moving Average (SMA).
        Replaces np.mean() over a sliding window.
        """
        values = [a.value for a in axiom_group[-window:] if a.value is not None]
        if not values:
            return 0.0
        return sum(values) / len(values)

    def apply_entropy(self, axiom: Axiom):
        """
        Entropy Law for Finance:
        Data older than 'TTL' (Time To Live) cools down and is compressed.
        """
        # Assume axiom.metadata has 'timestamp'
        ttl = self.config.get("ttl", 60) # Default 60 seconds
        now = time.time()
        
        # Check if timestamp exists in metadata
        if 'timestamp' in axiom.metadata:
            age = now - axiom.metadata['timestamp']
            if age > ttl:
                # Cool down rapidly BELOW the threshold (e.g. 5.0)
                axiom.temperature = 5.0
                return True
        return False

class StockAxiom(Axiom):
    """
    A specialized Axiom for financial data.
    """
    def __init__(self, price: float, ticker: str, manifold: Manifold):
        timestamp = time.time()
        # Ensure metadata is passed as kwargs so Axiom stores it in self.metadata
        super().__init__(price, manifold, ticker=ticker, timestamp=timestamp)

    def __repr__(self):
        return f"Stock({self.metadata['ticker']}: {self.value})"
