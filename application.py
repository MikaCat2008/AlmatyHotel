"""

Файл с функционалом для управления
приложением. Приложение основано
на архитектурном паттерне MVC, где 
играет роль контроллера(Controller). В
основном все методы перенаправляются
в модель и выводит логи.

"""


from datetime import date

from abstractions import ApplicationType, HotelDatabaseType

from view import HotelView
from model import HotelModel

from logger import logger


class Application(ApplicationType):
    """
    Класс приложения
    """
    
    def __init__(
        self, 
        database: HotelDatabaseType,
        host: str = "localhost",
        port: int = 8080
    ) -> None:
        """
        Создает обьекты отображения и 
        модели
        """
        
        self.database = database

        self.view = HotelView(self, host, port)
        self.model = HotelModel(self, database)

    def login(self, user: str, password: str) -> bool:
        """
        Проверяет логин и пароль, которые
        по умолчанию Admin и Root
        """
        
        return user == "Admin" and password == "Root"

    def create_room(
        self,
        room_type: int, 
        room_price: float
    ) -> tuple[int, int, float]:
        """
        Создает комнату и выводит лог
        """
        
        room = self.model.create_room(
            room_type, room_price
        )

        logger.create_room(*room)
        
        return room
    
    def create_employee(
        self, 
        employee_full_name: str,
        employee_age: int,
        employee_gender: bool,
        employee_job: int,
        employee_salary: int,
        employee_phone: str,
        employee_address: str,
        employee_mail: str
    ) -> tuple[int, str, int, bool, int, int, str, str, str]:
        """
        Создает сотрудника и выводит лог
        """
        
        employee = self.model.create_employee(
            employee_full_name, employee_age, employee_gender, employee_job, 
            employee_salary, employee_phone, employee_address, employee_mail
        )

        logger.create_employee(*employee)
        
        return employee
    
    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> tuple[int, int, date, int, int]:
        """
        Создает занятость и выводит лог
        """
        
        occupation = self.model.create_occupation(
            room_id, occupation_start, occupation_days, occupation_type
        )

        logger.create_occupation(*occupation)
        
        return occupation

    def get_rooms(self) -> list[tuple[int, int, float]]:
        """
        Получает список комнат и выводит
        лог
        """
        
        rooms = self.model.get_rooms()

        logger.get_rooms()
        
        return rooms
    
    def get_employees(self) -> list[tuple[int, str, int, int, int, int, str, str, str]]:
        """
        Получает список сотрудников и
        выводит лог
        """
        
        employees = self.model.get_employees()

        logger.get_employees()
        
        return employees
    
    def get_occupations(self, occupation_type: int = None) -> list[tuple[int, int, date, int, int]]:
        """
        Получает список занятостей и
        выводит лог
        """
        
        occupations = self.model.get_occupations(occupation_type)

        logger.get_occupations(occupation_type)
        
        return occupations

    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> tuple[list[str], dict[int, list[tuple[int, int, int, int]]]]:
        """
        Получает шахматку комнат и выводит
        лог
        """
        
        rooms_checkerboard = self.model.get_rooms_checkerboard(year, month)

        logger.get_rooms_checkerboard(year, month)
        
        return rooms_checkerboard

    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        """
        Обновляет комнату и выводит лог
        """
        
        self.model.update_room(
            room_id, room_type, room_price
        )

        logger.update_room(
            room_id, room_type, room_price
        )

    def update_employee(
        self, 
        employee_id: int,
        employee_full_name: str,
        employee_age: int,
        employee_gender: bool,
        employee_job: int,
        employee_salary: int,
        employee_phone: str,
        employee_address: str,
        employee_mail: str
    ) -> None:
        """
        Обновляет сотрудника и выводит лог
        """
        
        self.model.update_employee(
            employee_id, employee_full_name, employee_age, employee_gender,
            employee_job, employee_salary, employee_phone, employee_address,
            employee_mail
        )

        logger.update_employee(
            employee_id, employee_full_name, employee_age, employee_gender,
            employee_job, employee_salary, employee_phone, employee_address,
            employee_mail
        )
    
    def update_occupation(
        self, 
        occupation_id: int,
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> None:
        """
        Обновляет занятость и выводит лог
        """
        
        self.model.update_occupation(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        )

        logger.update_occupation(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        )

    def delete_room(self, room_id: int) ->  None:
        """
        Удаляет комнату и выводит лог
        """
        
        self.model.delete_room(room_id)

        logger.delete_room(room_id)

    def delete_employee(self, employee_id: int) ->  None:
        """
        Удаляет сотрудника и выводит лог
        """
        
        self.model.delete_employee(employee_id)

        logger.delete_employee(employee_id)

    def delete_occupation(self, occupation_id: int) ->  None:
        """
        Удаляет занятость и выводит лог
        """
        
        self.model.delete_occupation(occupation_id)

        logger.delete_occupation(occupation_id)

    def run(self) -> None:
        """
        Запускает приложение
        """
        
        self.model.init_database()

        try:
            logger.run_application()

            self.view.run()
        finally:
            logger.stop_application()
