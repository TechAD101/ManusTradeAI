
import uuid
from datetime import datetime

class SimulatorService:
    """Mock Simulator Service for backtesting strategies."""
    _simulations = {} # In-memory storage for simulation results

    def __init__(self):
        pass

    def run_simulation(self, strategy_name, start_date, end_date):
        """Runs a mock simulation and returns results."""
        simulation_id = str(uuid.uuid4())
        
        # Simulate some P&L and trade data
        pnl = 1500.0 if "momentum" in strategy_name.lower() else 800.0
        trades = [
            {"id": 1, "symbol": "AAPL", "type": "BUY", "qty": 10, "price": 150.0, "pnl": 150.0},
            {"id": 2, "symbol": "GOOG", "type": "SELL", "qty": 5, "price": 2500.0, "pnl": 200.0}
        ]

        results = {
            "simulation_id": simulation_id,
            "strategy_name": strategy_name,
            "start_date": start_date,
            "end_date": end_date,
            "total_pnl": pnl,
            "trades_executed": trades,
            "metrics": {
                "win_rate": 0.65,
                "sharpe_ratio": 1.2,
                "max_drawdown": 0.05
            },
            "timestamp": datetime.now().isoformat()
        }
        self._simulations[simulation_id] = results
        return results

    def get_simulation_results(self, simulation_id):
        """Retrieves simulation results by ID."""
        return self._simulations.get(simulation_id)


