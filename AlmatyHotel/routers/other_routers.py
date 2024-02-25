from .tls import request, jsonify, redirect, _check_auth, Response, ApplicationType


def login(app: ApplicationType) -> Response:
    status, user, password = _check_auth(app, request.json)

    response = jsonify({"status": status})

    if status:
        response.set_cookie("user", user)
        response.set_cookie("password", password)

    return response


def exit(app: ApplicationType) -> Response:
    response = redirect("/")

    response.delete_cookie("user")
    response.delete_cookie("password")
    
    return response
