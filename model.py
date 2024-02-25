import calendar

from datetime import date, datetime

from abstractions import HotelModelType, ApplicationType, HotelDatabaseType


def to_days(timestamp: float) -> int:
    return int(timestamp // 86_400)


class HotelModel(HotelModelType):
    def __init__(self, app: ApplicationType, database: HotelDatabaseType) -> None:
        self.app = app
        self.database = database

    def init_database(self) -> None:
        self.database.create_tables()

    def reset_database(self) -> None:
        self.database.delete_tables()
        self.init_database()

    def create_room(
        self, 
        room_type: int, 
        room_price: float
    ) -> tuple[int, int, float]:
        room_id = self.database.create_room(room_type, room_price)

        return room_id, room_type, room_price

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
        employee_id = self.database.create_employee(
            employee_full_name, employee_age, employee_gender, employee_job, 
            employee_salary, employee_phone, employee_address, employee_mail
        )

        return (
            employee_id, employee_full_name, employee_age, employee_gender,
            employee_job, employee_salary, employee_phone, employee_address,
            employee_mail
        )

    def create_occupation(
        self, 
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> tuple[int, int, date, int, int]:
        reservation_id = self.database.create_occupation(
            room_id, occupation_start, occupation_days, occupation_type
        )

        return reservation_id, room_id, occupation_start, occupation_days, occupation_type

    def get_rooms(self) -> list[tuple[int, int, float]]:
        return self.database.get_rooms()
    
    def get_employees(self) -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
        return self.database.get_employees()
    
    def get_occupations(self, occupation_type: int = None) -> list[int, int, date, int, int]:
        return self.database.get_occupations(occupation_type)
    
    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> tuple[list[str], dict[int, list[tuple[int, int, int, int]]]]:
        days_in_month = calendar.monthrange(year, month)[1]

        days = [f"{i:02}" for i in range(1, days_in_month + 1)]

        start_month = to_days(datetime(year, month, 1).timestamp())

        rooms = {}
        for room in self.get_rooms():
            room_id, _, _ = room

            rooms[room_id] = []
        for occupation in self.get_occupations():
            occupation_id, room_id, occupation_start_str, occupation_days, occupation_type = occupation

            if room_id not in rooms:
                self.delete_occupation(occupation_id)
                
                continue

            occupation_start_date = datetime.strptime(occupation_start_str, "%Y-%m-%d")
            occupation_start = to_days(occupation_start_date.timestamp())
            occupation_end = occupation_start + occupation_days

            start = max(0, occupation_start - start_month)
            end = min(days_in_month, occupation_end - start_month)

            if start >= days_in_month:
                continue

            if end < 0:
                continue
            
            rooms[room_id].append((occupation_id, start, end, occupation_type))

        return days, list(rooms.items())

    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        self.database.update_room(room_id, room_type, room_price)

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
        self.database.update_employee(
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
        self.database.update_occupation(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        )

    def delete_room(self, room_id: int) ->  None:
        self.database.delete_room(room_id)

    def delete_employee(self, employee_id: int) ->  None:
        self.database.delete_employee(employee_id)

    def delete_occupation(self, occupation_id: int) ->  None:
        self.database.delete_occupation(occupation_id)
