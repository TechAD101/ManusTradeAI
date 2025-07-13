
from flask import Blueprint, request, jsonify
from ..services.trading_service import TradingService

trading_bp = Blueprint("trading_bp", __name__)

trading_service = TradingService()

@trading_bp.route("/place_order", methods=["POST"])
def place_order():
    data = request.get_json()
    symbol = data.get("symbol")
    order_type = data.get("order_type")
    quantity = data.get("quantity")
    price = data.get("price") # Optional for market orders

    if not symbol or not order_type or not quantity:
        return jsonify({"msg": "Missing symbol, order_type, or quantity"}), 400

    try:
        result = trading_service.place_order(symbol, order_type, quantity, price)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": f"Error placing order: {str(e)}"}), 500

@trading_bp.route("/account_info", methods=["GET"])
def get_account_info():
    info = trading_service.get_account_info()
    return jsonify(info), 200

@trading_bp.route("/open_orders", methods=["GET"])
def get_open_orders():
    orders = trading_service.get_open_orders()
    return jsonify(orders), 200


