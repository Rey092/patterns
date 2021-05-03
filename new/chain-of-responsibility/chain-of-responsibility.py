from abc import abstractmethod


class Order:
    def __init__(self, *dishes):
        self.list = dishes


class Menu:
    list = ['Макароны', 'Борщ', 'Пельмени']


class AbstractHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class WaiterHandler(AbstractHandler):
    def handle(self, order_inst):
        dishes = []
        for dish in order_inst:
            if dish in Menu.list:
                dishes.append(dish)
        if self._next_handler:
            if dishes:
                return super().handle(dishes)
        return None


class ChefHandler(AbstractHandler):
    def handle(self, dishes):
        for dish in dishes:
            print(f'Chef makes a {dish}')


if __name__ == "__main__":
    waiter = WaiterHandler()
    chef = ChefHandler()

    waiter.set_next(chef)

    order = Order('Макароны', 'Пельмени', 'Пицца')

    waiter.handle(order.list)
