import datetime

from app.config import TOKEN
from tinkoff.invest import Client


try:
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id
        result = client.operations.get_operations(
            account_id = account_id,
            from_=datetime.datetime(2023, 11, 11),
            to=datetime.datetime.now()
        )
    print(result)
except:
    print("Ошибка, что-то пошло не так...")