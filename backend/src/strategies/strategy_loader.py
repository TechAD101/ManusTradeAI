
import os
import importlib.util
from .base_strategy import BaseStrategy

class StrategyLoader:
    """Loads trading strategies dynamically from a specified directory."""

    def __init__(self, strategy_dir=None):
        # Default to the directory where this script resides, then 'strategies' folder
        if strategy_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.strategy_dir = current_dir
        else:
            self.strategy_dir = strategy_dir
        self.strategies = self._load_strategies()

    def _load_strategies(self):
        """Discovers and loads all strategy classes inheriting from BaseStrategy."""
        loaded_strategies = {}
        for filename in os.listdir(self.strategy_dir):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "base_strategy.py":
                module_name = filename[:-3] # Remove .py extension
                file_path = os.path.join(self.strategy_dir, filename)

                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, BaseStrategy) and obj is not BaseStrategy:
                        # Instantiate the strategy and store it
                        strategy_instance = obj()
                        loaded_strategies[strategy_instance.name] = strategy_instance
        return loaded_strategies

    def get_available_strategies(self):
        """Returns a list of names and descriptions of loaded strategies."""
        return [{
            "name": strategy.name,
            "description": strategy.description
        } for strategy in self.strategies.values()]

    def execute_strategy(self, strategy_name, market_data):
        """Executes a specific strategy with given market data."""
        strategy = self.strategies.get(strategy_name)
        if not strategy:
            raise ValueError(f"Strategy \'{strategy_name}\' not found.")
        
        # In a real scenario, market_data would be fetched live or from a data source
        # For this mock, we expect market_data to be passed in the correct format
        signal = strategy.generate_signal(market_data)
        return {"strategy_name": strategy_name, "signal": signal}


