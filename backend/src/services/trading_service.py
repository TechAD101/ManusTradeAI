
import os
from ..binance.client import BinanceClient

class TradingService:
    """Handles interaction with exchange APIs for live or paper trading."""

    def __init__(self):
        self.trading_mode = os.environ.get("TRADING_MODE", "paper")
        self.binance_client = None

        if self.trading_mode == "live":
            api_key = os.environ.get("BINANCE_API_KEY")
            api_secret = os.environ.get("BINANCE_API_SECRET")
            if not api_key or not api_secret:
                raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET must be set for live trading.")
            self.binance_client = BinanceClient(api_key, api_secret) # Using mock client for now
        else:
            print("TradingService running in PAPER mode.")
            self.binance_client = BinanceClient("mock_key", "mock_secret") # Use mock client for paper trading

    def place_order(self, symbol, order_type, quantity, price=None):
        """Places a trade order."""
        # In a real application, map order_type to Binance specific types (e.g., MARKET, LIMIT)
        side = "BUY" if order_type.upper() == "BUY" else "SELL"
        type = "MARKET" if price is None else "LIMIT"

        if self.binance_client:
            return self.binance_client.place_order(symbol, side, type, quantity, price)
        else:
            raise Exception("Trading client not initialized.")

    def get_account_info(self):
        """Retrieves account balance and other information."""
        if self.binance_client:
            return self.binance_client.get_account_info()
        else:
            raise Exception("Trading client not initialized.")

    def get_open_orders(self):
        """Retrieves all open orders."""
        if self.binance_client:
            return self.binance_client.get_open_orders()
        else:
            raise Exception("Trading client not initialized.")


