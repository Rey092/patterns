from abc import ABC, abstractmethod


class HouseBuilder(ABC):

    @abstractmethod
    def build_house(self):
        pass

    @abstractmethod
    def build_garden(self):
        pass

    @abstractmethod
    def build_basement(self):
        pass


class WealthyHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House("Wealthy House")

    def build_house(self):
        self.house.add(('walls', 'roof', 'cladding', 'plumbing'))

    def build_garden(self):
        self.house.add(('roses', 'grass', 'tulips', 'fountain'))

    def build_basement(self):
        self.house.add(('big basement', 'mini-bar', 'brazier'))

    def reset_house(self):
        self.house.reset_house()

    def show_house(self):
        self.house.show_house()

    def return_house(self):
        return self.house


class House:
    def __init__(self, name=None):
        self.name = name
        self.structure = []

    def add(self, parts):
        self.structure.extend(parts)

    def reset_house(self):
        self.structure = []

    def show_house(self):
        print(f"House: {', '.join(self.structure)}.")


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, some_builder):
        self.builder = some_builder

    def make_simple_house(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        if builder.house.structure is not None:
            builder.reset_house()
        self.builder.build_house()

    def make_complex_house(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        if builder.house.structure is not None:
            builder.reset_house()
        self.builder.build_house()
        self.builder.build_garden()
        self.builder.build_basement()


if __name__ == "__main__":

    director = Director()
    builder = WealthyHouseBuilder()
    director.builder = builder

    print("Simple house by director: ")
    director.make_simple_house()
    builder.show_house()

    print("\n")
    print("Complex house by director: ")
    director.make_complex_house()
    builder.show_house()

    print("\n")
    print("Custom product: ")
    builder.reset_house()

    builder.build_house()
    builder.build_basement()
    builder.show_house()

    print("\n")
    print("Return house: ")
    house = builder.return_house()
    house.show_house()
    print(house.name)
