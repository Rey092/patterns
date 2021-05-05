from abc import ABC, abstractmethod


class SmoothieMaker(ABC):
    def make_smoothie(self):
        self.prepare_shaker()
        self.prepare_liquid()
        self.prepare_ingredients()
        self.shake()
        self.prepare_glass()
        self.fill_glass()

    def prepare_shaker(self):
        print("Shaker prepared")

    def shake(self):
        print("Let's shake it up")

    def prepare_glass(self):
        print("Glass prepared")

    def fill_glass(self):
        print("Smoothie is ready")

    @abstractmethod
    def prepare_liquid(self):
        pass

    @abstractmethod
    def prepare_ingredients(self):
        pass

    def prepare_ice(self):
        pass


class MilkSmoothieMaker(SmoothieMaker):

    def prepare_liquid(self) -> None:
        print("Milk prepared")

    def prepare_ingredients(self) -> None:
        print("Peaches, Strawberries are prepared")


class YogurtSmoothieMaker(SmoothieMaker):

    def prepare_liquid(self):
        print("Yogurt prepared")

    def prepare_ingredients(self):
        print("Mandarins, Bananas and honey are prepared")

    def prepare_ice(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


if __name__ == "__main__":
    milk_smoothie_maker = MilkSmoothieMaker()
    milk_smoothie_maker.make_smoothie()

    print('\n')

    yogurt_smoothie_maker = YogurtSmoothieMaker()
    yogurt_smoothie_maker.make_smoothie()
