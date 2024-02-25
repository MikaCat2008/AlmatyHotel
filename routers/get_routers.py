from .tls import request, jsonify, check_auth, Response, ApplicationType


@check_auth
def get_rooms(app: ApplicationType) -> Response:
    return jsonify({"rooms": app.get_rooms()})


@check_auth
def get_employees(app: ApplicationType) -> Response:
    return jsonify({"employees": app.get_employees()})


@check_auth
def get_rooms_checkerboard(app: ApplicationType) -> Response:
    data = request.json

    year, month = data.get("year"), data.get("month")
    days, rooms = app.get_rooms_checkerboard(year, month)

    return jsonify({
        "days": days, "rooms": rooms
    })


@check_auth
def get_occupations(app: ApplicationType) -> Response:
    data = request.json

    return jsonify({"occupations": app.get_occupations(data.get("occupation_type"))})
