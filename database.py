"""

Файл с управлением базой данных.
Имеет все методы CRUD.

"""


import sqlite3, logging

from datetime import date

from abstractions import SQLiteDatabaseType, HotelDatabaseType

# Ссылка на обьект базы данных
__database: SQLiteDatabaseType = None


class SQLiteDatabase(SQLiteDatabaseType):
    """
    Класс с базовым функционалом для
    SQL базы данных
    """
    
    def __init__(
        self, 
        filepath: str = "database/database.db"
    ) -> None:
        """
        Подключение к файлу базы данных
        """
        
        self.connection = sqlite3.connect(filepath, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, *args) -> tuple:
        """
        Выполняет запросы базы данных
        """
        
        self.cursor.execute(query, args)

        self.connection.commit()

    def single(self) -> None:
        """
        Делает ссылкой на базу
        данных этот обьект
        """
        
        global __database
        
        __database = self

    @classmethod
    def get_single(self) -> SQLiteDatabaseType:
        """
        Получает ссылку на базу данных
        """
        
        return __database


class HotelDatabase(SQLiteDatabase, HotelDatabaseType):
    """
    Класс с функционал для базы данных
    отеля
    """
    
    def create_tables(self) -> None:
        """
        Создает все нужные таблицы
        """
        
        self.execute("""
            CREATE TABLE IF NOT EXISTS Rooms (
                RoomId INTEGER PRIMARY KEY,
                RoomType INT,
                RoomPrice FLOAT
            );
        """)

        self.execute("""      
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeId INTEGER PRIMARY KEY,
                EmployeeFullName STRING, 
                EmployeeAge INTEGER, 
                EmployeeGender BOOLEAN, 
                EmployeeJob INTEGER, 
                EmployeeSalary INTEGER, 
                EmployeePhone STRING, 
                EmployeeAddress STRING, 
                EmployeeMail STRING
            );
        """)

        self.execute("""      
            CREATE TABLE IF NOT EXISTS Occupations (
                OccupationId INTEGER PRIMARY KEY,
                RoomId INTEGER,
                OccupationStart DATE,
                OccupationDays INTEGER,
                OccupationType INTEGER
            );
        """)

    def delete_tables(self) -> None:
        """
        Удаляет все таблицы
        """
        
        self.execute("""
            DROP TABLE IF EXISTS Rooms;             
        """)

        self.execute("""
            DROP TABLE IF EXISTS Employees;             
        """)

        self.execute("""
            DROP TABLE IF EXISTS Occupations;             
        """)

    def create_room(
        self, 
        room_type: int, 
        room_price: float
    ) -> int:
        """
        Создает комнату, принимая ее тип,
        цену, а возвращает ее номер
        """
        
        self.execute("""
                INSERT INTO Rooms VALUES(NULL, ?, ?);
            """, 
            room_type, room_price
        )

        return self.cursor.lastrowid
    
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
        """
        Создает сотрудника принимая его 
        ФИО, возраст, пол, должность,
        оклад, телефон, адрес, почту, а
        возвращает его номер
        """
        
        self.execute("""
                INSERT INTO Employees VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?);
            """, 
            employee_full_name, employee_age, employee_gender, employee_job,
            employee_salary, employee_phone, employee_address, employee_mail
        )

        return self.cursor.lastrowid

    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> int:
        """
        Создает занятость принимая ее
        номер комнаты, начало занятости,
        количество дней, тип, а возвращает
        ее номер
        """
        
        self.execute("""
                INSERT INTO Occupations VALUES(NULL, ?, ?, ?, ?);
            """, 
            room_id, occupation_start, occupation_days, occupation_type
        )

        return self.cursor.lastrowid

    def get_rooms(self) -> list[tuple[int, int, float]]:
        """
        Возвращает список комнат
        """
        
        self.execute("""
            SELECT * FROM Rooms;
        """)

        return list(self.cursor.fetchall())
    
    def get_employees(self) -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
        """
        Возвращает список сотрудников
        """
        
        self.execute("""
            SELECT * FROM Employees;
        """)

        return list(self.cursor.fetchall())

    def get_occupations(self, occupation_type: int = None) -> list[int, int, date, int, int]:
        """
        Возвращает список занятостей,
        принимая тип(необязательно)
        """
        
        if occupation_type is None:
            self.execute("""
                SELECT * FROM Occupations;
            """)
        else:
            self.execute("""
                SELECT * FROM Occupations WHERE OccupationType = ?;
            """, occupation_type)

        return list(self.cursor.fetchall())

    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        """
        Обновляет комнату, принимая ее
        номер, тип, цену
        """
        
        self.execute("""
                UPDATE Rooms
                SET RoomType = ?,
                    RoomPrice = ?
                WHERE RoomId = ?;
            """,
            room_type, room_price, room_id
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
        Обновляет сотрудника, принимая его 
        номер, ФИО, возраст, пол, должность,
        оклад, телефон, адрес, почту
        """
        
        self.execute("""
                UPDATE Employees
                SET EmployeeFullName = ?, 
                    EmployeeAge = ?,
                    EmployeeGender = ?,
                    EmployeeJob = ?,
                    EmployeeSalary = ?,
                    EmployeePhone = ?,
                    EmployeeAddress = ?,
                    EmployeeMail = ?
                WHERE EmployeeId = ?;
            """,
            employee_full_name, employee_age, employee_gender, employee_job,
            employee_salary, employee_phone, employee_address, employee_mail,
            employee_id
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
        Обновляет занятость, принимая ее
        номер, номер комнаты, начальную
        дату, количество дней, тип
        """
        
        self.execute("""
                UPDATE Occupations
                SET RoomId = ?,
                    OccupationStart = ?,
                    OccupationDays = ?,
                    OccupationType = ?
                WHERE OccupationId = ?;
            """,
            room_id, occupation_start, occupation_days, occupation_type, occupation_id
        )

    def delete_room(self, room_id: int) ->  None:
        """
        Удаляет комнату, принимая ее номер
        """
        
        self.execute("""
            DELETE 
            FROM Rooms
            WHERE RoomId = ?;
        """, room_id)

    def delete_employee(self, employee_id: int) ->  None:
        """
        Удаляет сотрудникас принимая его
        номер
        """
        
        self.execute("""
            DELETE 
            FROM Employees
            WHERE EmployeeId = ?;
        """, employee_id)

    def delete_occupation(self, occupation_id: int) ->  None:
        """
        Удаляет занятость, принимая ее
        номер
        """
        
        self.execute("""
            DELETE 
            FROM Occupations
            WHERE OccupationId = ?;
        """, occupation_id)
