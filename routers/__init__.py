"""

Файл со всеми роутерами сайта


"""


from typing import Callable

from .main_routers import (
    index, rooms, employees, reservations, renovations, cleaning, rooms_checkerboard,
)
from .add_routers import (
    add_room, add_employee, add_reservation, add_renovation, add_cleaning
)
from .create_routers import (
    create_room, create_employee, create_occupation
)
from .get_routers import (
    get_rooms, get_employees, get_occupations, get_rooms_checkerboard
)
from .update_routers import (
    update_room, update_employee, update_occupation
)
from .delete_routers import (
    delete_room, delete_employee, delete_occupation
)
from .other_routers import (
    login, exit
)


def get_routers() -> list[tuple[str, Callable, str]]:
    """
    Получает все роутеры
    """
    
    return [
        ("/", index, "GET"),
        ("/rooms", rooms, "GET"),
        ("/employees", employees, "GET"),
        ("/reservations", reservations, "GET"),
        ("/renovations", renovations, "GET"),
        ("/cleaning", cleaning, "GET"),
        ("/rooms-checkerboard", rooms_checkerboard, "GET"),

        ("/add-room", add_room, "GET"),
        ("/add-employee", add_employee, "GET"),
        ("/add-reservation", add_reservation, "GET"),
        ("/add-renovation", add_renovation, "GET"),
        ("/add-cleaning", add_cleaning, "GET"),

        ("/create-room", create_room, "POST"),
        ("/create-employee", create_employee, "POST"),
        ("/create-occupation", create_occupation, "POST"),

        ("/get-rooms", get_rooms, "POST"),
        ("/get-employees", get_employees, "POST"),
        ("/get-occupations", get_occupations, "POST"),
        ("/get-rooms-checkerboard", get_rooms_checkerboard, "POST"),

        ("/update-room", update_room, "POST"),
        ("/update-employee", update_employee, "POST"),
        ("/update-occupation", update_occupation, "POST"),

        ("/delete-room", delete_room, "POST"),
        ("/delete-employee", delete_employee, "POST"),
        ("/delete-occupation", delete_occupation, "POST"),

        ("/login", login, "POST"),
        ("/exit", exit, "GET")
    ]
