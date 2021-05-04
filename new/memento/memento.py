
class Memento:
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        return self.__state[:]


class House:
    def __init__(self):
        self.__state = []

    def add(self, parts):
        print(f"В дом добавлены элементы: {', '.join(parts)}")
        self.__state.extend(parts)

    def reset_house(self):
        self.__state = []

    def create_memento(self):
        return Memento(self.__state[:])

    def load_memento(self, memento):
        self.__state = memento.get_state()

    def show_house(self):
        if self.__state:
            print(f"House: {', '.join(self.__state[:])}.")
        else:
            print('House: no elements')


class Builder:
    def __init__(self, house):
        self.house = house
        self.house_states = []

    def build_house(self):
        self.house_states.append(self.house.create_memento())
        self.house.add(('walls', 'roof', 'cladding', 'plumbing'))

    def build_garden(self):
        self.house_states.append(self.house.create_memento())
        self.house.add(('roses', 'grass', 'tulips', 'fountain'))

    def build_basement(self):
        self.house_states.append(self.house.create_memento())
        self.house.add(('big basement', 'mini-bar', 'brazier'))

    def reset_house(self):
        self.house_states.append(self.house.create_memento())
        self.house.reset_house()

    def show_house(self):
        self.house.show_house()

    def return_house(self):
        return self.house

    def undo(self):
        if len(self.house_states) == 0:
            print('История отсутствует. Вы ещё не строили дом.')
        elif len(self.house_states) == 1:
            self.house.load_memento(self.house_states[0])
            print("Дом в первичном состоянии")
            self.house.show_house()
        else:
            print("Отмена предыдущего действия")
            state = self.house_states.pop()
            self.house.load_memento(state)
            self.house.show_house()


if __name__ == "__main__":
    house1 = House()
    builder = Builder(house1)

    builder.undo()

    print("\n")
    builder.build_house()
    builder.show_house()

    print("\n")
    builder.build_garden()
    builder.show_house()

    print("\n")
    builder.build_basement()
    builder.show_house()

    print("\n")
    builder.undo()
    builder.undo()
    builder.undo()
    builder.undo()
    builder.undo()
