from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(Item):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def price(self):
        return self.cost

    def __str__(self):
        return f'Product: {self.name}, Cost: {self.price()}'


class Box(Item):
    def __init__(self, name):
        self.name = name
        self.products = []

    def price(self):
        cost = 0
        for product in self.products:
            cost += product.price()
        return cost

    def __str__(self):
        return f'Box: {self.name}, Total cost: {self.price()}'

    def add_products(self, *products):
        self.products.extend(products)

    def remove_product(self, product):
        self.products.remove(product)

    def clear(self):
        self.products = []


class GiftBox(Box):
    def __init__(self, name):
        super().__init__(name)

    def price(self):
        cost = 0
        for product in self.products:
            cost += product.price()
        return cost

    def __str__(self):
        return f'GiftBox: {self.name}, Total cost: {self.price()}'


if __name__ == "__main__":
    birthday_gift = GiftBox('birthday_gift')

    smartphone = Product('smartphone', 4500)
    charger = Product('charger', 250)
    airpods = Product('airpods', 400)
    flowers = Product('flowers', 310)
    candies = Product('candies', 140)

    smartphone_box = Box('smartphone_box')

    smartphone_box.add_products(smartphone, charger, airpods)

    birthday_gift.add_products(smartphone_box, flowers, candies)

    print(birthday_gift)
    print(smartphone_box)
    print(candies, ' /// ', flowers)
