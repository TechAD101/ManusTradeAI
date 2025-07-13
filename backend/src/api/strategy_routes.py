
from flask import Blueprint, jsonify, request
from ..strategies.strategy_loader import StrategyLoader

strategy_bp = Blueprint("strategy_bp", __name__)

strategy_loader = StrategyLoader()

@strategy_bp.route("/available", methods=["GET"])
def get_available_strategies():
    strategies = strategy_loader.get_available_strategies()
    return jsonify(strategies), 200

@strategy_bp.route("/execute", methods=["POST"])
def execute_strategy():
    data = request.get_json()
    strategy_name = data.get("strategy_name")
    params = data.get("params", {})

    if not strategy_name:
        return jsonify({"msg": "Strategy name is required"}), 400

    try:
        result = strategy_loader.execute_strategy(strategy_name, params)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 404
    except Exception as e:
        return jsonify({"msg": f"Error executing strategy: {str(e)}"}), 500


