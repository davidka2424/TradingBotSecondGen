import sqlite3


class DataBase:

    def __init__(self, db_name="trading_bot_db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def initialize(self):
        with self.connect() as conn:
            cursor = conn.cursor()

            cursor.execute("DROP TABLE IF EXISTS candles")

            # Возможно ли хранить время в базе данных в виде time/datetime?
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS candles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    figi TEXT NOT NULL, 
                    time TEXT NOT NULL,
                    open REAL NOT NULL,
                    high REAL NOT NULL,
                    low REAL NOT NULL,
                    close REAL NOT NULL,
                    volume INTEGER NOT NULL
                )
                """
            )
            conn.commit()

            print("Database created succesfully")
