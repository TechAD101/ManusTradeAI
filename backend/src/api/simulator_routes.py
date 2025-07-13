
from flask import Blueprint, request, jsonify
from ..services.simulator_service import SimulatorService

simulator_bp = Blueprint("simulator_bp", __name__)

simulator_service = SimulatorService()

@simulator_bp.route("/run", methods=["POST"])
def run_simulation():
    data = request.get_json()
    strategy_name = data.get("strategy_name")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if not strategy_name or not start_date or not end_date:
        return jsonify({"msg": "Missing strategy_name, start_date, or end_date"}), 400

    results = simulator_service.run_simulation(strategy_name, start_date, end_date)
    return jsonify(results), 200

@simulator_bp.route("/results/<string:simulation_id>", methods=["GET"])
def get_simulation_results(simulation_id):
    results = simulator_service.get_simulation_results(simulation_id)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"msg": "Simulation results not found"}), 404


