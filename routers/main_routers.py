from datetime import datetime

from .tls import request, make_response, check_auth, _check_auth, render_template, Response, ApplicationType

MONTH_NAMES = (
    "Январь", "Февраль", "Март", "Апрель",
    "Май", "Июнь", "Июль", "Август", 
    "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
)


def index(app: ApplicationType) -> Response:
    if _check_auth(app, request.cookies)[0]:
        just_logged = request.args.get("just_logged")

        return render_template("_admin_panel.html", **{
            "just_logged": just_logged or 0
        })

    return render_template("index.html")


@check_auth
def rooms(app: ApplicationType) -> Response:
    return render_template("rooms.html")


@check_auth
def employees(app: ApplicationType) -> Response:
    return render_template("employees.html")


@check_auth
def reservations(app: ApplicationType) -> Response:
    return render_template("reservations.html")


@check_auth
def renovations(app: ApplicationType) -> Response:
    return render_template("renovations.html")


@check_auth
def cleaning(app: ApplicationType) -> Response:
    return render_template("cleaning.html")


@check_auth
def rooms_checkerboard(app: ApplicationType) -> Response:
    year = request.args.get("year")
    month = request.args.get("month")

    if year is None or month is None:
        date = datetime.now().date()

        year, month = date.year, date.month

    month_name = MONTH_NAMES[int(month) - 1]

    return render_template(
        "rooms_checkerboard.html", **{
            "year": year, 
            "month": month, 
            "month_name": month_name
        }
    )
