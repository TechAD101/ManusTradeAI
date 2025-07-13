
from flask import Blueprint, request, jsonify
from ..models.journal import JournalEntry

journal_bp = Blueprint("journal_bp", __name__)

@journal_bp.route("/entries", methods=["POST"])
def add_journal_entry():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    user_id = data.get("user_id") # In a real app, get from JWT token

    if not title or not content or not user_id:
        return jsonify({"msg": "Missing title, content, or user_id"}), 400

    new_entry = JournalEntry(title=title, content=content, user_id=user_id)
    new_entry.save()

    return jsonify({"msg": "Journal entry added successfully"}), 201

@journal_bp.route("/entries/<string:user_id>", methods=["GET"])
def get_journal_entries(user_id):
    entries = JournalEntry.find_by_user_id(user_id)
    return jsonify([entry.to_dict() for entry in entries]), 200


