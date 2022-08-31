import requests
import json
from config import headers, currencies


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def new_convert(base, qoute, amount):
        if base == qoute:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?"
                         f"from={base}&to={qoute}&amount={amount}",
                         headers=headers)
        text = round(json.loads(r.content)['result'], 3)
        message = f'{amount} {base} в {qoute}: {text}'
        return message
