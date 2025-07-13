
class BinanceClient:
    """Mock Binance Client for demonstration purposes."""

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.account_balance = {"USD": 100000.0, "BTC": 0.0, "ETH": 0.0}
        self.open_orders = []
        print("Binance Client initialized (Mock Mode).")

    def get_account_info(self):
        """Returns mock account information."""
        return {"balances": self.account_balance, "canTrade": True}

    def place_order(self, symbol, side, type, quantity, price=None):
        """Places a mock order."""
        print(f"Mock Order Placed: {side} {quantity} {symbol} at {price if price else type}")
        # Simulate order execution
        if type == "MARKET":
            if side == "BUY":
                cost = quantity * self._get_current_price(symbol)
                if self.account_balance["USD"] >= cost:
                    self.account_balance["USD"] -= cost
                    self.account_balance[symbol] = self.account_balance.get(symbol, 0.0) + quantity
                    return {"orderId": "mock_order_123", "status": "FILLED", "executedQty": quantity}
                else:
                    raise ValueError("Insufficient USD balance")
            elif side == "SELL":
                if self.account_balance.get(symbol, 0.0) >= quantity:
                    self.account_balance["USD"] += quantity * self._get_current_price(symbol)
                    self.account_balance[symbol] -= quantity
                    return {"orderId": "mock_order_124", "status": "FILLED", "executedQty": quantity}
                else:
                    raise ValueError(f"Insufficient {symbol} balance")
        else:
            # For LIMIT orders, just add to open_orders for now
            order = {"symbol": symbol, "side": side, "type": type, "quantity": quantity, "price": price, "status": "NEW"}
            self.open_orders.append(order)
            return {"orderId": "mock_order_125", "status": "NEW"}

    def get_open_orders(self, symbol=None):
        """Returns mock open orders."""
        if symbol:
            return [order for order in self.open_orders if order["symbol"] == symbol]
        return self.open_orders

    def _get_current_price(self, symbol):
        """Returns a mock current price for a symbol."""
        # In a real scenario, this would fetch live market data
        if symbol == "BTC":
            return 30000.0
        elif symbol == "ETH":
            return 2000.0
        elif symbol == "AAPL": # Example for a stock
            return 170.0
        return 1.0 # Default


