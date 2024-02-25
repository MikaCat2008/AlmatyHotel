from datetime import date

from abstractions import ApplicationType, HotelDatabaseType

from view import HotelView
from model import HotelModel

from logger import logger


class Application(ApplicationType):
    def __init__(
        self, 
        database: HotelDatabaseType,
        host: str = "localhost",
        port: int = 8080
    ) -> None:
        self.database = database

        self.view = HotelView(self, host, port)
        self.model = HotelModel(self, database)

    def login(self, user: str, password: str) -> bool:
        return user == "Admin" and password == "Root"

    def create_room(
        self,
        room_type: int, 
        room_price: float
    ) -> tuple[int, int, float]:
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
        occupation = self.model.create_occupation(
            room_id, occupation_start, occupation_days, occupation_type
        )

        logger.create_occupation(*occupation)
        
        return occupation

    def get_rooms(self) -> list[tuple[int, int, float]]:
        rooms = self.model.get_rooms()

        logger.get_rooms()
        
        return rooms
    
    def get_employees(self) -> list[tuple[int, str, int, int, int, int, str, str, str]]:
        employees = self.model.get_employees()

        logger.get_employees()
        
        return employees
    
    def get_occupations(self, occupation_type: int = None) -> list[tuple[int, int, date, int, int]]:
        occupations = self.model.get_occupations(occupation_type)

        logger.get_occupations(occupation_type)
        
        return occupations

    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> tuple[list[str], dict[int, list[tuple[int, int, int, int]]]]:
        rooms_checkerboard = self.model.get_rooms_checkerboard(year, month)

        logger.get_rooms_checkerboard(year, month)
        
        return rooms_checkerboard

    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
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
        self.model.update_occupation(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        )

        logger.update_occupation(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        )

    def delete_room(self, room_id: int) ->  None:
        self.model.delete_room(room_id)

        logger.delete_room(room_id)

    def delete_employee(self, employee_id: int) ->  None:
        self.model.delete_employee(employee_id)

        logger.delete_employee(employee_id)

    def delete_occupation(self, occupation_id: int) ->  None:
        self.model.delete_occupation(occupation_id)

        logger.delete_occupation(occupation_id)

    def run(self) -> None:
        self.model.init_database()

        try:
            logger.run_application()

            self.view.run()
        finally:
            logger.stop_application()
