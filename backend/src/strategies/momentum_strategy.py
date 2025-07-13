
from .base_strategy import BaseStrategy

class MomentumStrategy(BaseStrategy):
    """A simple momentum trading strategy."""

    def __init__(self):
        super().__init__("Momentum Strategy", "Buys assets with upward price momentum, sells with downward.")

    def generate_signal(self, market_data):
        """Generates a trading signal based on simple momentum.

        Args:
            market_data (dict): Dictionary containing market data, e.g., {"price_history": [...

        Returns:
            str: "BUY", "SELL", or "HOLD"
        """
        price_history = market_data.get("price_history")
        if not price_history or len(price_history) < 2:
            return "HOLD"

        latest_price = price_history[-1]
        previous_price = price_history[-2]

        if latest_price > previous_price:
            return "BUY"
        elif latest_price < previous_price:
            return "SELL"
        else:
            return "HOLD"


