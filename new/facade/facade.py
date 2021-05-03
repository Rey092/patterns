from __future__ import annotations


class FastFood:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class MacDonalds:
    def __init__(self):
        self.__make_burger = MakeBurger()
        self.__make_french_fry = MakeFrenchFry()
        self.__make_soda = MakeSoda()

    def buy_mac_menu(self, burger='BigMac', french_fry='FrenchFry', soda='CocaCola'):
        result = []
        result.append(self.__make_burger.make(burger))
        result.append(self.__make_french_fry.make(french_fry))
        result.append(self.__make_soda.make(soda))

        return result


class MakeBurger:
    @staticmethod
    def make(burger):
        products = {
            'BigMac': FastFood('BigMac', 50),
            'BigTasty': FastFood('BigTasty', 40),
            'McRoyale': FastFood('McRoyale', 60),
        }
        return products[burger]


class MakeFrenchFry:
    @staticmethod
    def make(french_fry):
        products = {
            'FrenchFry': FastFood('FrenchFry', 30),
            'PeasantPotatoes': FastFood('PeasantPotatoes', 50),
        }
        return products[french_fry]


class MakeSoda:
    @staticmethod
    def make(soda):
        products = {
            'CocaCola': FastFood('CocaCola', 25),
            'Fanta': FastFood('Fanta', 20),
        }
        return products[soda]


if __name__ == "__main__":
    mac = MacDonalds()
    mac_menu = mac.buy_mac_menu(soda='Fanta')

    print(mac_menu, '\n')
    for item in mac_menu:
        print(item, f'/ Price: {item.price}')
