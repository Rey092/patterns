from abc import ABC, abstractmethod


class MacBook(ABC):
    @abstractmethod
    def accept(self, visitor_inst):
        pass


class MacBookPro(MacBook):
    def __init__(self):
        self.price = 2000
        self.discount = 0.10

    def accept(self, visitor_inst):
        return visitor_inst.visit(self)


class MacBookAir(MacBook):
    def __init__(self):
        self.price = 1400
        self.discount = 0.15

    def accept(self, visitor_inst):
        return visitor_inst.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, macbook):
        pass


class Visitor1(Visitor):
    def visit(self, macbook):
        return macbook.price


class Visitor2(Visitor):
    def visit(self, macbook):
        return int(macbook.price * (1 - macbook.discount))


if __name__ == "__main__":
    macbook1 = MacBookPro()
    macbook2 = MacBookAir()
    macbook3 = MacBookAir()

    components = [macbook1, macbook2, macbook3]

    visitor1 = Visitor1()
    visitor2 = Visitor2()

    total_price = 0
    for component in components:
        price = component.accept(visitor1)
        total_price += price
    print('Visitor 1. Total price without discount:', total_price)

    total_price = 0
    for component in components:
        price = component.accept(visitor2)
        total_price += price
    print('Visitor 2. Total price with discount:', total_price)
