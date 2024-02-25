from datetime import datetime

from .tls import request, jsonify, check_auth, Response, ApplicationType


@check_auth
def create_room(app: ApplicationType) -> Response:
    app.create_room(*request.json.get("room"))
    
    return jsonify({"status": True})


@check_auth
def create_employee(app: ApplicationType) -> Response:
    app.create_employee(*request.json.get("employee"))
    
    return jsonify({"status": True})


@check_auth
def create_occupation(app: ApplicationType) -> Response:
    room_id, occupation_start_str, occupation_days, occupation_type = request.json.get("occupation")
    
    occupation_start = datetime.strptime(occupation_start_str, "%Y-%m-%d").date()

    app.create_occupation(
        room_id, occupation_start, occupation_days, occupation_type
    )
    
    return jsonify({"status": True})
