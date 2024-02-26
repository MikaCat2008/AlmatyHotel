"""

Файл логирования. Здесь находятся
инструменты для вывода в консоль
отчетов, что было сделано на сайте
(например: создана комната, удален
сотрудник)

"""


import logging

from datetime import date

# Отключение логера Flask'а'
log = logging.getLogger('werkzeug')
log.disabled = True


class Logger:
    """
    Класс, содержащий методы для вывода
    отчетов
    """
    
    def run_application(self) -> None:
        """
        Срабатывает при запуске сервера
        """
        
        logging.info("Сервер запущен")

    def stop_application(self) -> None:
        """
        Срабатывает при остановке сервера
        """
        
        logging.info("Сервер остановлен")

    def create_room(
        self,
        room_id: int,
        room_type: int, 
        room_price: float
    ) -> None:
        """
        Срабатывает при создании комнаты
        и выводит ее номер, тип, цену
        """
        
        logging.info("Создана комната[{}](type={}, price={})".format(room_id, room_type, room_price))

    def create_employee(
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
        Срабатывает при создании
        сотрудника и выводит его номер,
        ФИО, возраст, пол, должность,
        оклад, телефон, адрес, почту
        """
        
        logging.info(
            "Создан сотрудник[{}](full_name={}, age={}, gender={}, job={}, salary={}, phone={}, address={}, mail={})".format(
                employee_id, employee_full_name, employee_age, employee_gender, 
                employee_job, employee_salary, employee_phone, employee_address, 
                employee_mail
            )
        )

    def create_occupation(
        self, 
        occupation_id: int,
        room_id: int, 
        occupation_start: date,
        occupation_days: int,
        occupation_type: int
    ) -> None:
        """
        Срабатывает при создании занятости
        и выводит ее номер, номер комнаты, 
        начальную дату, количество дней, 
        тип
        """
        
        logging.info(
            "Создана занятость[{}](room_id={}, start={}, days={}, type={})".format(
                occupation_id, room_id, occupation_start, occupation_days, occupation_type
            )
        )

    def get_rooms(self) -> None:
        """
        Срабатывает при запросе списка
        комнат
        """
        
        logging.info("Запрос на список комнат")

    def get_employees(self) -> None:
        """
        Срабатывает при запросе списка
        сотрудников
        """
        
        logging.info("Запрос на список сотрудников")
    
    def get_occupations(self, occupation_type: int = None) -> None:
        """
        Срабатывает при запросе списка
        занятостей
        """
        
        logging.info("Запрос на список занятостей(type={})".format(occupation_type))
    
    def get_rooms_checkerboard(
        self, year: int, month: int
    ) -> None:
        """
        Срабатывает при запросе шахматки
        комнат
        """
        
        logging.info("Запрос на шахматку комнат(year={}, month={})".format(year, month))

    def update_room(
        self, 
        room_id: int, 
        room_type: int, 
        room_price: float
    ) -> None:
        """
        Срабатывает при обновлении
        комнаты и выводит ее номер,
        тип, цену
        """
        
        logging.info("Обновлена комната[{}](type={}, price={})".format(
            room_id, room_type, room_price
        ))

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
        Срабатывает при обновлении
        сотрудника и выводит его номер,
        ФИО, возраст, пол, должность,
        оклад, телефон, адрес, почту
        """
        
        logging.info(
            "Обновлен сотрудник[{}](full_name={}, age={}, gender={}, job={}, salary={}, phone={}, address={}, mail={})".format(
                employee_id, employee_full_name, employee_age, employee_gender,
                employee_job, employee_salary, employee_phone, employee_address,
                employee_mail
            )
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
        Срабатывает при обновлении
        занятости и выводит ее номер,
        номер комнаты, начальную дату,
        количество дней, тип
        """
        
        logging.info("Обновлена занятость[{}](room_id={}, start={}, days={}, type={})".format(
            occupation_id, room_id, occupation_start, occupation_days, occupation_type
        ))

    def delete_room(self, room_id: int) -> None:
        """
        Срабатывает при удалении комнаты
        и выводит ее номер
        """
        
        logging.info(f"Комната[{room_id}] удалена")

    def delete_employee(self, employee_id: int) -> None:
        """
        Срабатывает при удалении
        сотрудника и выводит его номер
        """
        
        logging.info(f"Сотрудник[{employee_id}] удален")

    def delete_occupation(self, occupation_id: int) -> None:
        """
        Срабатывает при удалении
        занятости и выводит ее номер
        """
        
        logging.info(f"Занятость[{occupation_id}] удалена")


# Настройки логера
logger = Logger()
logging.basicConfig(
    level=logging.INFO, 
    # filename="hotel.log", filemode="w", encoding="UTF-8",
    format="%(asctime)s: %(message)s"
)
