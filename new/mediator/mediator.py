from abc import ABC
from old.factory_method.factory import AmericanoMachine, EspressoMachine

americano_maker = AmericanoMachine()
espresso_maker = EspressoMachine()


class Mediator(ABC):

    def make(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def make(self, sender, event):
        if event == "americano":
            print("Mediator reacts on make_americano:")

            coffee = americano_maker.make_coffee()
            print(coffee)

        elif event == "espresso":
            print("Mediator reacts on make_espresso:")

            if isinstance(sender, CoffeeMachine):
                print('No espresso in coffee machine.')
            else:
                coffee = espresso_maker.make_coffee()
                print(coffee)


class CoffeeMaker:
    def __init__(self, mediator=None):
        self.mediator = mediator


class Barista(CoffeeMaker):
    def make_americano(self):
        print("Barista wants to make Americano and inform Mediator")
        self.mediator.make(self, "americano")

    def make_espresso(self):
        print("Barista wants to make Espresso and inform Mediator")
        self.mediator.make(self, "espresso")


class CoffeeMachine(CoffeeMaker):
    def make_americano(self):
        print("Coffee-Machine wants to make Americano and inform Mediator")
        self.mediator.make(self, "americano")

    def make_espresso(self):
        print("Coffee-Machine wants to make Espresso and inform Mediator")
        self.mediator.make(self, "espresso")


if __name__ == "__main__":
    barista = Barista()
    machine = CoffeeMachine()

    mediator = ConcreteMediator(barista, machine)

    print("Client wants to buy coffee from barista")
    barista.make_americano()

    print("\n")

    print("Client wants to buy coffee in coffee machine")
    machine.make_espresso()
