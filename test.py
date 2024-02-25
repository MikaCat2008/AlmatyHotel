import unittest

from datetime import date

from database import HotelDatabase
from application import Application


def create_rooms() -> list[tuple[int, int, float]]:
    return [
        app.create_room(0, 20),
        app.create_room(2, 180)
    ]


def create_employees() -> list[tuple[int, str, int, bool, int, int, str, str, str]]:
    return [
        app.create_employee(
            "Цветкова Жозефина Михайловна", 20, False, 3, 1200, 
            "+548(4451)359-18-72", "Palm Passage", "lequoperagi-6417@yopmail.com"
        ),
        app.create_employee(
            "Бондаренко Артём Леонидович", 23, True, 6, 1000, 
            "3(684)316-30-17", "Gravel Boulevard", "kellezappaupri-8847@yopmail.com"
        )
    ]


def create_occupations() -> list[tuple[int, int, date, int, int]]:
    return [
        app.create_occupation(
            1, date(2024, 2, 3), 3, 1
        ),
        app.create_occupation(
            2, date(2024, 2, 4), 3, 1
        ),
        app.create_occupation(
            1, date(2024, 2, 6), 2, 2
        ),
        app.create_occupation(
            2, date(2024, 2, 7), 2, 2
        ),
        app.create_occupation(
            1, date(2024, 2, 9), 1, 3
        ),
        app.create_occupation(
            2, date(2024, 2, 10), 1, 3
        )
    ]


def delete_rooms() -> None:
    app.delete_room(1)
    app.delete_room(2)


def delete_employees() -> None:
    app.delete_employee(1)
    app.delete_employee(2)


def delete_occupations() -> None:
    app.delete_occupation(1)
    app.delete_occupation(2)
    app.delete_occupation(3)
    app.delete_occupation(4)
    app.delete_occupation(5)
    app.delete_occupation(6)


class MainTestCase(unittest.TestCase):
    def test_create_room(self) -> None:
        room1, room2 = create_rooms()

        self.assertEqual(room1, (1, 0, 20))
        self.assertEqual(room2, (2, 2, 180))

        delete_rooms()

    def test_create_employee(self) -> None:
        employee1, employee2 = create_employees()

        self.assertEqual(employee1, (
            1, "Цветкова Жозефина Михайловна", 20, False, 3, 1200, 
            "+548(4451)359-18-72", "Palm Passage", "lequoperagi-6417@yopmail.com"
        ))
        self.assertEqual(employee2, (
            2, "Бондаренко Артём Леонидович", 23, True, 6, 1000, 
            "3(684)316-30-17", "Gravel Boulevard", "kellezappaupri-8847@yopmail.com"
        ))

        delete_employees()

    def test_create_occupation(self) -> None:
        occupation1, occupation2, occupation3, \
        occupation4, occupation5, occupation6 = create_occupations()

        self.assertEqual(occupation1, (
            1, 1, date(2024, 2, 3), 3, 1
        ))
        self.assertEqual(occupation2, (
            2, 2, date(2024, 2, 4), 3, 1
        ))
        self.assertEqual(occupation3, (
            3, 1, date(2024, 2, 6), 2, 2
        ))
        self.assertEqual(occupation4, (
            4, 2, date(2024, 2, 7), 2, 2
        ))
        self.assertEqual(occupation5, (
            5, 1, date(2024, 2, 9), 1, 3
        ))
        self.assertEqual(occupation6, (
            6, 2, date(2024, 2, 10), 1, 3
        ))

        delete_occupations()

    def test_get_rooms(self) -> None:
        create_rooms()
        
        rooms = app.get_rooms()

        self.assertEqual(rooms, [
            (1, 0, 20),
            (2, 2, 180)
        ])

        delete_rooms()

    def test_get_employees(self) -> None:
        create_employees()

        employees = app.get_employees()
        
        self.assertEqual(employees, [
            (
                1, "Цветкова Жозефина Михайловна", 20, False, 3, 1200, 
                "+548(4451)359-18-72", "Palm Passage", "lequoperagi-6417@yopmail.com"
            ),
            (
                2, "Бондаренко Артём Леонидович", 23, True, 6, 1000, 
                "3(684)316-30-17", "Gravel Boulevard", "kellezappaupri-8847@yopmail.com"
            )
        ])

        delete_employees()

    def test_get_reservations(self) -> None:
        create_occupations()

        reservations = app.get_occupations(1)

        self.assertEqual(reservations, [
            (1, 1, "2024-02-03", 3, 1),
            (2, 2, "2024-02-04", 3, 1)
        ])

        delete_occupations()

    def test_get_renovations(self) -> None:
        create_occupations()

        renovations = app.get_occupations(2)

        self.assertEqual(renovations, [
            (3, 1, "2024-02-06", 2, 2),
            (4, 2, "2024-02-07", 2, 2)
        ])

        delete_occupations()

    def test_get_cleaning(self) -> None:
        create_occupations()

        cleaning = app.get_occupations(3)

        self.assertEqual(cleaning, [
            (5, 1, "2024-02-09", 1, 3),
            (6, 2, "2024-02-10", 1, 3)
        ])

        delete_occupations()

    def test_get_occupations(self) -> None:
        create_occupations()

        occupations = app.get_occupations()

        self.assertEqual(occupations, [
            (1, 1, "2024-02-03", 3, 1),
            (2, 2, "2024-02-04", 3, 1),
            (3, 1, "2024-02-06", 2, 2),
            (4, 2, "2024-02-07", 2, 2),
            (5, 1, "2024-02-09", 1, 3),
            (6, 2, "2024-02-10", 1, 3)
        ])

        delete_occupations()

    def test_get_rooms_checkboard(self) -> None:
        create_rooms()
        create_occupations()

        rooms_checkerboard = app.get_rooms_checkerboard(2024, 2)

        self.assertEqual(rooms_checkerboard, (
            [
                '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                '21', '22', '23', '24', '25', '26', '27', '28', '29'
            ], 
            [
                (1, [(1, 2, 5, 1), (3, 5, 7, 2), (5, 8, 9, 3)]), 
                (2, [(2, 3, 6, 1), (4, 6, 8, 2), (6, 9, 10, 3)])
            ]
        ))

        delete_rooms()
        delete_occupations()

    def test_update_room(self) -> None:
        room1, room2 = create_rooms()

        room_id1, room_type1, room_price1 = room1
        room_id2, room_type2, room_price2 = room2

        app.update_room(room_id1, room_type2, room_price2)
        app.update_room(room_id2, room_type1, room_price1)

        rooms = app.get_rooms()

        self.assertEqual(rooms, [
            (1, 2, 180),
            (2, 0, 20)
        ])

        delete_rooms()

    def test_update_employee(self) -> None:
        employee1, employee2 = create_employees()

        employee_id1,     employee_full_name1, employee_age1, \
        employee_gender1, employee_job1,      employee_salary1, \
        employee_phone1,  employee_address1,  employee_mail1 = employee1

        employee_id2,     employee_full_name2, employee_age2, \
        employee_gender2, employee_job2,      employee_salary2, \
        employee_phone2,  employee_address2,  employee_mail2 = employee2

        app.update_employee(
            employee_id1, employee_full_name2, employee_age2, employee_gender2,
            employee_job2, employee_salary2, employee_phone2, employee_address2,
            employee_mail2
        )
        app.update_employee(
            employee_id2, employee_full_name1, employee_age1, employee_gender1,
            employee_job1, employee_salary1, employee_phone1, employee_address1,
            employee_mail1
        )

        employees = app.get_employees()

        self.assertEqual(employees, [
            (
                1, "Бондаренко Артём Леонидович", 23, True, 6, 1000, 
                "3(684)316-30-17", "Gravel Boulevard", "kellezappaupri-8847@yopmail.com"
            ),
            (
                2, "Цветкова Жозефина Михайловна", 20, False, 3, 1200, 
                "+548(4451)359-18-72", "Palm Passage", "lequoperagi-6417@yopmail.com"
            )
        ])

        delete_employees()

    def test_update_occupation(self) -> None:
        occupation1, occupation2, occupation3, \
        occupation4, occupation5, occupation6 = create_occupations()

        occupation_id1, room_id1, occupation_start1, occupation_days1, occupation_type1 = occupation1 
        occupation_id2, room_id2, occupation_start2, occupation_days2, occupation_type2 = occupation2 
        occupation_id3, room_id3, occupation_start3, occupation_days3, occupation_type3 = occupation3 
        occupation_id4, room_id4, occupation_start4, occupation_days4, occupation_type4 = occupation4 
        occupation_id5, room_id5, occupation_start5, occupation_days5, occupation_type5 = occupation5 
        occupation_id6, room_id6, occupation_start6, occupation_days6, occupation_type6 = occupation6 

        app.update_occupation(
            occupation_id1, room_id2, occupation_start2, occupation_days2, occupation_type2
        )
        app.update_occupation(
            occupation_id2, room_id1, occupation_start1, occupation_days1, occupation_type1
        )
        app.update_occupation(
            occupation_id3, room_id4, occupation_start4, occupation_days4, occupation_type4
        )
        app.update_occupation(
            occupation_id4, room_id3, occupation_start3, occupation_days3, occupation_type3
        )
        app.update_occupation(
            occupation_id5, room_id6, occupation_start6, occupation_days6, occupation_type6
        )
        app.update_occupation(
            occupation_id6, room_id5, occupation_start5, occupation_days5, occupation_type5
        )

        occupations = app.get_occupations()

        self.assertEqual(occupations, [
            (1, 2, "2024-02-04", 3, 1),
            (2, 1, "2024-02-03", 3, 1),
            (3, 2, "2024-02-07", 2, 2),
            (4, 1, "2024-02-06", 2, 2),
            (5, 2, "2024-02-10", 1, 3),
            (6, 1, "2024-02-09", 1, 3)
        ])

        delete_occupations()

    def test_delete_room(self) -> None:
        create_rooms()
        delete_rooms()

        rooms = app.get_rooms()

        self.assertEqual(rooms, [])

    def test_delete_employee(self) -> None:
        create_employees()
        delete_employees()

        employees = app.get_employees()

        self.assertEqual(employees, [])

    def test_delete_occupation(self) -> None:
        create_occupations()
        delete_occupations()

        occupations = app.get_occupations()

        self.assertEqual(occupations, [])


if __name__ == "__main__":
    db = HotelDatabase("database/test_database.db")
    db.single()

    app = Application(db)
    app.model.reset_database()

    unittest.main()
