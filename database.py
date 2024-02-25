import sqlite3, logging

from datetime import date

from abstractions import SQLiteDatabaseType, HotelDatabaseType

__database: SQLiteDatabaseType = None


class SQLiteDatabase(SQLiteDatabaseType):
    def __init__(self, filepath: str = "database/database.db") -> None:        
        super().__init__()

        self.connection = sqlite3.connect(filepath, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, *args) -> tuple:
        self.cursor.execute(query, args)

        self.connection.commit()

    def single(self) -> None:
        global __database
        
        __database = self

    @classmethod
    def get_single(self) -> SQLiteDatabaseType:
        return __database


class HotelDatabase(SQLiteDatabase, HotelDatabaseType):
    def create_tables(self) -> None:
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
        self.execute("""
                INSERT INTO Occupations VALUES(NULL, ?, ?, ?, ?);
            """, 
            room_id, occupation_start, occupation_days, occupation_type
        )

        return self.cursor.lastrowid

    def get_rooms(self) -> list[tuple[int, int, float]]:
        self.execute("""
            SELECT * FROM Rooms;
        """)

        return list(self.cursor.fetchall())
    
    def get_employees(self) -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
        self.execute("""
            SELECT * FROM Employees;
        """)

        return list(self.cursor.fetchall())

    def get_occupations(self, occupation_type: int = None) -> list[int, int, date, int, int]:
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
        self.execute("""
            DELETE 
            FROM Rooms
            WHERE RoomId = ?;
        """, room_id)

    def delete_employee(self, employee_id: int) ->  None:
        self.execute("""
            DELETE 
            FROM Employees
            WHERE EmployeeId = ?;
        """, employee_id)

    def delete_occupation(self, occupation_id: int) ->  None:
        self.execute("""
            DELETE 
            FROM Occupations
            WHERE OccupationId = ?;
        """, occupation_id)
