"""

Файл с инструментами для создания 
роутеров


"""


from typing import Callable
from datetime import datetime

from flask import request, Response, jsonify, redirect, make_response, render_template

from abstractions import ApplicationType


def _check_auth(app: ApplicationType, data: dict) -> tuple[bool, str, str]:
    """
    Проверяет правильность данных
    авторизации
    """
    
    user = data.get("user")
    password = data.get("password")

    return app.login(user, password), user, password


def check_auth(f: Callable) -> None:
    """
    Функция-декоратор, что проверяет
    с помощью куки, авторизирован ли
    пользователь
    
    """
    
    def _(app: ApplicationType) -> tuple[bool, str, str]:
        if not _check_auth(request.cookies)[0]:
            return redirect("/")
        f(app)

    return f
