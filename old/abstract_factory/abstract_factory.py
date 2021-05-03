from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Table(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Bed(ABC):
    @abstractmethod
    def __str__(self):
        pass


class VictorianChair(Chair):
    def __init__(self):
        self.name = "VictorianChair"

    def __str__(self):
        return f'Furniture: {self.name}'


class VictorianTable(Table):
    def __init__(self):
        self.name = "VictorianTable"

    def __str__(self):
        return f'Furniture: {self.name}'


class VictorianBed(Bed):
    def __init__(self):
        self.name = "VictorianBed"

    def __str__(self):
        return f'Furniture: {self.name}'


class GothicChair(Chair):
    def __init__(self):
        self.name = "GothicChair"

    def __str__(self):
        return f'Furniture: {self.name}'


class GothicTable(Table):
    def __init__(self):
        self.name = "GothicTable"

    def __str__(self):
        return f'Furniture: {self.name}'


class GothicBed(Bed):
    def __init__(self):
        self.name = "GothicBed"

    def __str__(self):
        return f'Furniture: {self.name}'


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def get_chair(self):
        pass

    @abstractmethod
    def get_table(self):
        pass

    @abstractmethod
    def get_bed(self):
        pass


class VictorianFurnitureFactory(AbstractFurnitureFactory):
    def get_chair(self):
        return VictorianChair()

    def get_table(self):
        return VictorianTable()

    def get_bed(self):
        return VictorianBed()


class GothicFurnitureFactory(AbstractFurnitureFactory):
    def get_chair(self):
        return GothicChair()

    def get_table(self):
        return GothicTable()

    def get_bed(self):
        return GothicBed()


class Application:
    def __init__(self, concrete_factory):
        self._factory = concrete_factory
        self.chair = None
        self.table = None
        self.bed = None

    def create_furniture(self):
        self.chair = self._factory.get_chair()
        self.table = self._factory.get_table()
        self.bed = self._factory.get_bed()


if __name__ == '__main__':
    factory = GothicFurnitureFactory()

    app = Application(factory)
    print(app.chair)
    app.create_furniture()
    print(app.chair, '///', app.table, '///', app.bed)
