# backend/utils/helpers.py
from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    """
    Returns a standardized JSON success response.
    Example:
        return success_response({"reply": "Hello!"})
    """
    payload = {
        "success": True,
        "message": message,
        "data": data or {}
    }
    return jsonify(payload), status_code


def error_response(error_message="An error occurred", status_code=400):
    """
    Returns a standardized JSON error response.
    Example:
        return error_response("Invalid input", 422)
    """
    payload = {
        "success": False,
        "error": error_message
    }
    return jsonify(payload), status_code


def validate_json(required_fields, data):
    """
    Validates that all required fields are present in the request JSON.
    Returns (True, None) if valid, or (False, missing_field) if not.
    Example:
        is_valid, missing = validate_json(["message"], data)
    """
    for field in required_fields:
        if field not in data or data[field] == "":
            return False, field
    return True, None
