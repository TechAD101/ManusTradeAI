
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    """Abstract base class for all trading strategies."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def generate_signal(self, market_data):
        """Generates a trading signal (e.g., BUY, SELL, HOLD)."""
        pass

    def get_info(self):
        return {"name": self.name, "description": self.description}


