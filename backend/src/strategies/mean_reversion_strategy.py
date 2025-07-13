
from .base_strategy import BaseStrategy

class MeanReversionStrategy(BaseStrategy):
    """A simple mean reversion trading strategy."""

    def __init__(self):
        super().__init__("Mean Reversion Strategy", "Sells when price is above average, buys when below average.")

    def generate_signal(self, market_data):
        """Generates a trading signal based on simple mean reversion.

        Args:
            market_data (dict): Dictionary containing market data, e.g., {"price_history": [...

        Returns:
            str: "BUY", "SELL", or "HOLD"
        """
        price_history = market_data.get("price_history")
        if not price_history or len(price_history) < 10: # Need enough data for average
            return "HOLD"

        latest_price = price_history[-1]
        average_price = sum(price_history[-10:]) / 10 # Simple moving average

        if latest_price > average_price * 1.01: # Price is 1% above average
            return "SELL"
        elif latest_price < average_price * 0.99: # Price is 1% below average
            return "BUY"
        else:
            return "HOLD"


