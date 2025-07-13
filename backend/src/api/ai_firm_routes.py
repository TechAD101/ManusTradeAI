
from flask import Blueprint, jsonify, request
from ..ai_firm.initialization import AIFirm

ai_firm_bp = Blueprint("ai_firm_bp", __name__)

# Initialize the AI Firm instance (singleton pattern might be better in a real app)
firm = AIFirm()

@ai_firm_bp.route("/status", methods=["GET"])
def get_firm_status():
    return jsonify(firm.get_status())

@ai_firm_bp.route("/start_shift", methods=["POST"])
def start_shift():
    firm.start_new_shift()
    return jsonify({"message": "New shift started successfully."})

@ai_firm_bp.route("/run_simulation_step", methods=["POST"])
def run_simulation_step():
    firm.run_simulation_step()
    return jsonify({"message": "Simulation step completed."})

@ai_firm_bp.route("/get_daily_report", methods=["GET"])
def get_daily_report():
    date_str = request.args.get("date") # format YYYY-MM-DD
    if not date_str:
        return jsonify({"error": "Date parameter is required"}), 400
    # Basic parsing, consider more robust date handling
    from datetime import datetime
    try:
        report_date = datetime.strptime(date_str, "%Y-%m-%d")
        report = firm.generate_daily_report(report_date)
        return jsonify(report)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

@ai_firm_bp.route("/get_weekly_report", methods=["GET"])
def get_weekly_report():
    date_str = request.args.get("date") # format YYYY-MM-DD
    if not date_str:
        return jsonify({"error": "Date parameter is required"}), 400
    from datetime import datetime
    try:
        report_date = datetime.strptime(date_str, "%Y-%m-%d")
        report = firm.generate_weekly_report(report_date)
        return jsonify(report)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400


