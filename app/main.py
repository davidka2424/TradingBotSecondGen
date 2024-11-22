from config import TOKEN_FULL
from client import TinkoffAPI
from tinkoff.invest import Client, CandleInterval, RequestError
import datetime
from settings import figi
from dataase import DataBase


def run():
    db = DataBase()
    db.initialize()


    figi_ = figi["ЧМК"]  # Пример FIGI для акции
    from_ = datetime.datetime(2024, 10, 18)
    to_ = datetime.datetime(2024, 11, 20)
    interval = CandleInterval.CANDLE_INTERVAL_DAY  # День

    try:
        with Client(TOKEN_FULL) as client:
            api = TinkoffAPI(client)
            candles = api.get_historical_candles(figi_, from_, to_, interval)

            # Сохранение данных в базу
            with db.connect() as conn:
                cursor = conn.cursor()
                for candle in candles:
                    cursor.execute("""
                            INSERT INTO candles (figi, time, open, high, low, close, volume)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (
                        figi_,
                        candle["time"],
                        float(candle["open"]),
                        float(candle["high"]),
                        float(candle["low"]),
                        float(candle["close"]),
                        candle["volume"],
                    ))
                conn.commit()
                print("Candles data saved to the database.")
    except RequestError as e:
        print(f"RequestError occurred: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    run()