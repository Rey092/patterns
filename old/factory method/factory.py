from abc import ABC, abstractmethod


class Coffee(ABC):
    def __init__(self):
        self.name = 'Coffee'
        self.price = 0
        self.milk = False
        self.foam = False

    @property
    def milk_status(self):
        status = 'with Milk' if self.milk is True else 'without Milk'
        return status

    @property
    def foam_status(self):
        status = 'with Foam' if self.milk is True else 'without Foam'
        return status

    def add_milk(self):
        if self.milk:
            print('Milk is already in coffee.')
        else:
            print('Milk is added. Price increased (+3 USD)')
            self.milk = True
            self.price = self.price + 3

    def add_foam(self):
        if self.foam:
            print('Foam is already in coffee.')
        else:
            print('Foam is added. Price increased (+2 USD)')
            self.foam = True
            self.price = self.price + 2

    @abstractmethod
    def __str__(self):
        pass


class Americano(Coffee):
    def __init__(self):
        super().__init__()
        self.name = 'Americano'
        self.price = 5

    def __str__(self):
        return f'{self.name} {self.milk_status} and {self.foam_status}. Price {self.price} USD. '


class Espresso(Coffee):
    def __init__(self):
        super().__init__()
        self.name = 'Espresso'
        self.price = 4

    def add_foam(self):
        print("Espresso can't be served with Foam")

    def __str__(self):
        return f'{self.name} {self.milk_status}. Price {self.price} USD.'


class CoffeeEngine(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def make_coffee(self):
        product = self.factory_method()
        print(f"CoffeeEngine: You should pay me {product.price} USD")
        return product

    def make_multiple_coffees(self, num=1):
        products = []
        for _ in range(num):
            product = self.factory_method()
            products.append(product)
            print(f"CoffeeEngine: Coffee is ready")

        print(f"CoffeeEngine: Coffee pack is ready")
        return products


class AmericanoMachine(CoffeeEngine):

    def factory_method(self):
        print('AmericanoMachine: Americano is ready')
        return Americano()


class EspressoMachine(CoffeeEngine):
    def factory_method(self):
        print('EspressoMachine: Espresso is ready')
        return Espresso()


def choose_coffee_machine(machine_type="Americano"):
    machines = {
        "Americano": AmericanoMachine,
        "Espresso": EspressoMachine,
    }
    return machines[machine_type]()


if __name__ == '__main__':
    machine = choose_coffee_machine('Americano')
    coffee = machine.make_coffee()

    print('\n')
    print(coffee)

    print('\n')
    coffee.add_milk()
    coffee.add_milk()
    print(coffee)

    print('\n')
    coffee.add_foam()
    coffee.add_foam()
    print(coffee)

    print('\n')
    machine = choose_coffee_machine('Espresso')
    coffee_pack = machine.make_multiple_coffees(5)

    print('\n')
    for coffee in coffee_pack:
        print(coffee)
