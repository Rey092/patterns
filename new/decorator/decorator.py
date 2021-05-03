from abc import ABC, abstractmethod
import requests


class Car(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class CarBogdan(Car):
    def __init__(self, cost):
        self.name = 'Bogdan 3000'
        self.cost = cost

    def price(self):
        return f'Price: {self.cost} UAH'

    def notify(self):
        print(f'Notification sent. {self.price()}')


class PriceNotifier(Car):
    def __init__(self, car_bogdan):
        self._wrapped = car_bogdan
        self.cost = car_bogdan.cost
        self.name = car_bogdan.name

    def notify(self):
        print(f'Notification sent. {self.price()}')
        return self._wrapped.notify()

    @abstractmethod
    def price(self):
        pass


class PriceNotifierUSD(PriceNotifier):
    def __init__(self, car_bogdan):
        super().__init__(car_bogdan)

    def price(self):
        rate = exchange_rates_for_uah('USD')
        price = round(self._wrapped.cost / rate, 1)
        return f'Price: {price} USD'


class PriceNotifierEUR(PriceNotifier):
    def __init__(self, car_bogdan):
        super().__init__(car_bogdan)

    def price(self):
        rate = exchange_rates_for_uah('EUR')
        price = round(self._wrapped.cost / rate, 1)
        return f'Price: {price} EUR'


def exchange_rates_for_uah(currency):
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    json = data.json()
    rates = {
        'USD': json[0]['buy'],
        'EUR': json[1]['buy'],
        'RUR': json[2]['buy'],
        'BTC': json[3]['buy'],
    }
    return round(float(rates[currency]), 1)


if __name__ == "__main__":
    car = CarBogdan(485670)
    print(car.price(), '\n')

    car = PriceNotifierUSD(car)
    print(car.price(), '\n')

    car = PriceNotifierEUR(car)
    print(car.price(), '\n')

    car.notify()
    print('\n', car.name)
