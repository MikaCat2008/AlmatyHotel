"""

Главный файл проекта, отсюда
происходит запуск

"""

from database import HotelDatabase
from application import Application

if __name__ == "__main__":
    db = HotelDatabase()
    db.single()

    app = Application(db)

    app.run()
