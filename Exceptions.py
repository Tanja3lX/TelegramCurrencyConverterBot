import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(f'Please enter two different currencies: {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Сurrency entered in invalid format: {base}\nList available currencies: /values')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Сurrency entered in invalid format: {quote}\nList available currencies: /values')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Invalid input: {amount}\nIt is possible to process the operation only when entering integers')

        if amount >= 100000000000:
            raise APIException('You have entered a number that exceeds the maximum input. Try it again.')

        if amount <= 0:
            raise APIException('Negative numbers or 0 cannot be entered. Please enter a positive number.')

        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
            data = json.loads(r.content)
            total_base = data[quote_ticker] * amount
        except Exception as e:
            raise APIException(f'Error during API request or processing: {e}')

        return round(total_base,2)
