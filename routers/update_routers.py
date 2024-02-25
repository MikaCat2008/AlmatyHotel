from datetime import datetime

from .tls import request, jsonify, check_auth, Response, ApplicationType


@check_auth
def update_room(app: ApplicationType) -> Response:
    app.update_room(*request.json["room"])

    return jsonify({"status": True})


@check_auth
def update_employee(app: ApplicationType) -> Response:
    app.update_employee(*request.json["employee"])

    return jsonify({"status": True})


@check_auth
def update_occupation(app: ApplicationType) -> Response:
    occupation_id, room_id, occupation_start_str, occupation_days, occupation_type = request.json.get("occupation")
    
    occupation_start = datetime.strptime(occupation_start_str, "%Y-%m-%d").date()

    app.update_occupation(
        occupation_id, room_id, occupation_start, occupation_days, occupation_type
    )

    return jsonify({"status": True})
