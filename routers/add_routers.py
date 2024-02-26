"""

Файл с роутерами добавления


"""


from .tls import check_auth, render_template, Response, ApplicationType


@check_auth
def add_room(app: ApplicationType) -> Response:
    return render_template("add_room.html")


@check_auth
def add_employee(app: ApplicationType) -> Response:
    return render_template("add_employee.html")


@check_auth
def add_reservation(app: ApplicationType) -> Response:
    return render_template("add_reservation.html")


@check_auth
def add_renovation(app: ApplicationType) -> Response:
    return render_template("add_renovation.html")


@check_auth
def add_cleaning(app: ApplicationType) -> Response:
    return render_template("add_cleaning.html")
