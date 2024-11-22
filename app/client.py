from config import TOKEN_FULL
from tinkoff.invest import Client, CandleInterval
#
#
# class TinkoffAPI:
#     def __init__(self, client):
#         self.client = client
#
#     def get_historical_candles(self, figi, from_date, to_date, interval):
#         candles = []
#         response = self.client.get_candles(figi=figi, from_=from_date, to=to_date, interval=interval)
#         for candle in response.candles:
#             candles.append({
#                 "time": candle.time,
#                 "open": self.cast_money(candle.open),
#                 "high": self.cast_money(candle.high),
#                 "low": self.cast_money(candle.low),
#                 "close": self.cast_money(candle.close),
#                 "volume": candle.volume
#             })
#         return candles
#
#     @staticmethod
#     def cast_money(money):
#         return money.units + money.nano / 1e9


from tinkoff.invest import Client, CandleInterval

#
# class TinkoffAPI:
#     def __init__(self, client):
#         self.client = client
#
#     def get_historical_candles(self, figi, from_date, to_date, interval):
#         candles = []
#
#         with self.client as client:
#             request = client.market_data.get_candles(
#                 figi=figi, from_=from_date, to=to_date, interval=interval
#         )
#         for candle in request.candles:
#             candles.append({
#                 "time": candle.time,
#                 "open": self.cast_money(candle.open),
#                 "high": self.cast_money(candle.high),
#                 "low": self.cast_money(candle.low),
#                 "close": self.cast_money(candle.close),
#                 "volume": candle.volume
#             })
#         return candles
#
#     @staticmethod
#     def cast_money(money):
#         return money.units + money.nano / 1e9


from tinkoff.invest import Client, CandleInterval


class TinkoffAPI:
    def __init__(self, client):
        self.client = client

    def get_historical_candles(self, figi, from_date, to_date, interval):
        candles = []

        try:
            # Используем client из конструктора, не создавая новый объект Client внутри
            response = self.client.market_data.get_candles(
                figi=figi, from_=from_date, to=to_date, interval=interval
            )
            # Отладочный вывод
            print("Candles response received")
            for candle in response.candles:
                candles.append({
                    "figi": figi,  # Добавляем FIGI в данные
                    "time": candle.time.isoformat(),  # Преобразуем datetime в строку
                    "open": self.cast_money(candle.open),  # Преобразуем Quotation в float
                    "high": self.cast_money(candle.high),  # Преобразуем Quotation в float
                    "low": self.cast_money(candle.low),  # Преобразуем Quotation в float
                    "close": self.cast_money(candle.close),  # Преобразуем Quotation в float
                    "volume": candle.volume
                })
        except Exception as e:
            print(f"Error occurred while fetching candles: {str(e)}")

        return candles

    @staticmethod
    def cast_money(money):
        return money.units + money.nano / 1e9

# Если что вернуться ко 2й версии