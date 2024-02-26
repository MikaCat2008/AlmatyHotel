"""

Файл с роутерами удаления


"""


from .tls import request, jsonify, check_auth, Response, ApplicationType


@check_auth
def delete_room(app: ApplicationType) -> Response:
    app.delete_room(request.json.get("room_id"))
    
    return jsonify({"status": True})


@check_auth
def delete_employee(app: ApplicationType) -> Response:
    app.delete_employee(request.json.get("employee_id"))
    
    return jsonify({"status": True})


@check_auth
def delete_occupation(app: ApplicationType) -> Response:
    app.delete_occupation(request.json.get("occupation_id"))
    
    return jsonify({"status": True})
