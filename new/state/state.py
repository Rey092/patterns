from abc import ABC, abstractmethod


class MoneyExchanger:

    def __init__(self, state):
        self._state = state
        self._state._context = self

    def transition_to(self, state):
        self.__init__(state)

    def insert_card(self):
        self._state.insert_card()

    def insert_money(self):
        self._state.insert_money()


class State(ABC):

    def __init__(self):
        self._context = None

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def insert_money(self):
        pass


class MoneyExchangerIsWorking(State):
    def insert_card(self):
        print(f"Владелец карты, какую валюту желаете приобрести?")

    def insert_money(self):
        print("Деньги введены успешно. Выберите валюту для обмена.")


class MoneyExchangerIsNotWorking(State):
    def insert_card(self):
        print("Тьфу, не суй мне эту пластмаску. Техработы, скоро включусь.")

    def insert_money(self):
        print("Беее, я не работаю. Техработы. Включусь через 5 часов.")


if __name__ == "__main__":

    context = MoneyExchanger(MoneyExchangerIsNotWorking())

    print('\n')
    context.insert_card()
    context.insert_money()

    context.transition_to(MoneyExchangerIsWorking())

    print('\n')
    context.insert_card()
    context.insert_money()
