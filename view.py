"""

Файл с функционалом для отображения
сайта. Является частью MVC, где играет 
роль отображения(View). Использует
библиотеку Flask

"""


from typing import Callable

import flask

from abstractions import HotelViewType, ApplicationType

from routers import get_routers


class HotelView(HotelViewType):
    """
    Класс отображения сайта отетя
    """
    
    def __init__(
        self, 
        app: ApplicationType,
        host: str = "localhost",
        port: int = 8080
    ) -> None:
        """
        Инициализация отображения
        """
        
        self.app = app
        self.host = host
        self.port = port

    def add_router(self, flask_app: flask.Flask, url: str, handler: Callable, method: str) -> None:
        """
        Добавление роутера, который
        является ссылкой с 
        функцией-обработчиком и методом
        запроса, нужен для возможности
        использовать ссылки на сайте
        """
        
        def _handler() -> flask.Response:
            return handler(self.app)
        
        _handler.__name__ = handler.__name__

        flask_app.add_url_rule(url, None, _handler, methods = [method])

    def run(self) -> None:
        """
        Запуск сервера по умолчанию на 
        http://localhost:8080
        """
        
        flask_app = flask.Flask(__name__)

        for url, handler, method in get_routers():
            self.add_router(flask_app, url, handler, method)

        flask_app.run(
            host = self.host,
            port = self.port
        )
