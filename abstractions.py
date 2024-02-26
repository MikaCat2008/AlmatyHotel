"""

Файл со всеми типами

"""


from __future__ import annotations

from abc import ABC, abstractmethod, abstractclassmethod
from typing import Callable

import sqlite3

from datetime import date


class SQLiteDatabaseType(ABC):
    cursor: sqlite3.Cursor
    connection: sqlite3.Connection

    @abstractmethod
    def execute(self, query: str, args: tuple) -> tuple:
        ...

    @abstractmethod
    def single(self) -> None:
        ...

    @abstractclassmethod
    def get_single(self) -> SQLiteDatabaseType:
        ...


class HotelDatabaseType(SQLiteDatabaseType):
    @abstractmethod
    def create_tables(self) -> None:
        ...

    @abstractmethod
    def delete_tables(self) -> None:
        ...

    @abstractmethod
    def create_room(
        self, 
        room_type: int, 
        room_price: float
    ) -> int:
        ...

    @abstractmethod
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
    ) -> int:
        ...

    @abstractmethod
    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> int:
        ...

    @abstractmethod
    def get_rooms(self) -> list[tuple[int, int, float]]:
        ...

    @abstractmethod
    def get_employees(self) -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
        ...

    @abstractmethod
    def get_occupations(self, occupation_type: int = None) -> list[int, int, date, int, int]:
        ...

    @abstractmethod
    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        ...

    @abstractmethod
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
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def update_occupation(
        self, 
        occupation_id: int,
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> None:
        ...

    @abstractmethod
    def delete_room(self, room_id: int) ->  None:
        ...

    @abstractmethod
    def delete_employee(self, employee_id: int) ->  None:
        ...

    @abstractmethod
    def delete_occupation(self, occupation_id: int) ->  None:
        ...


class HotelModelType(ABC):
    app: ApplicationType
    database: HotelDatabaseType

    @abstractmethod
    def init_database(self) -> None:
        ...

    @abstractmethod
    def reset_database(self) -> None:
        ...

    @abstractmethod
    def create_room(
        self, 
        room_type: int, 
        room_price: float
    ) -> tuple[int, int, float]:
        ...

    @abstractmethod
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
        ...
        
    @abstractmethod
    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> tuple[int, int, date, int, int]:
        ...

    @abstractmethod
    def get_rooms(self) -> list[tuple[int, int, float]]:
        ...

    @abstractmethod
    def get_employees(self) -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
        ...

    @abstractmethod
    def get_occupations(self, occupation_type: int = None) -> list[tuple[int, int, date, int, int]]:
        ...

    @abstractmethod
    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> tuple[list[str], dict[int, list[tuple[int, int, int, int]]]]:
        ...

    @abstractmethod
    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def update_occupation(
        self, 
        occupation_id: int,
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> None:
        ...

    @abstractmethod
    def delete_room(self, room_id: int) ->  None:
        ...

    @abstractmethod
    def delete_employee(self, employee_id: int) ->  None:
        ...

    @abstractmethod
    def delete_occupation(self, occupation_id: int) ->  None:
        ...


class HotelViewType(ABC):
    app: ApplicationType
    host: str
    port: int
    debug: bool
    
    @abstractmethod
    def add_router(self, url: str, handler: Callable, method: str) -> None:
        ...

    @abstractmethod
    def run(self) -> None:
        ...


class ApplicationType(ABC):
    database: HotelDatabaseType
    port: int
    hostname: str

    view: HotelViewType
    model: HotelModelType

    @abstractmethod
    def login(self, user: str, password: str) -> bool:
        ...

    @abstractmethod
    def create_room(
        self,
        room_type: int, 
        room_price: float
    ) -> tuple[int, int, float]:
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> tuple[int, int, date, int, int]:
        ...

    @abstractmethod
    def get_rooms(self) -> list[tuple[int, int, float]]:
        ...
    
    @abstractmethod
    def get_employees(self) -> list[tuple[int, str, int, int, int, int, str, str, str]]:
        ...

    @abstractmethod
    def get_occupations(self, occupation_type: int = None) -> list[tuple[int, int, date, int, int]]:
        ...

    @abstractmethod
    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> tuple[list[str], dict[int, list[tuple[int, int, int, int]]]]:
        ...

    @abstractmethod
    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        ...

    @abstractmethod
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
        ...

    @abstractmethod
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
        ...

    @abstractmethod
    def update_occupation(
        self, 
        occupation_id: int,
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> None:
        ...

    @abstractmethod
    def delete_room(self, room_id: int) ->  None:
        ...

    @abstractmethod
    def delete_employee(self, employee_id: int) ->  None:
        ...

    @abstractmethod
    def delete_occupation(self, occupation_id: int) ->  None:
        ...

    @abstractmethod
    def run(self) -> None:
        ...
