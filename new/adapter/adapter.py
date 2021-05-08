class CarAnalyticsForUSA:
    @staticmethod
    def parameters_for_usa(data):
        return f"Car parameters: Length: {data['length']} ft, Width: {data['width']} ft"


class Car:
    __price = 5
    __price2 = {}

    def __init__(self, length, width):
        self.length = length
        self.width = width
        # self.__dict__.update({'price': Car.__price})

    @property
    def price(self):
        return Car.__price

    @price.setter
    def price(self, value):
        Car.__price = value

    @property
    def price2(self):
        return Car.__price2[str(id(self))]

    @price2.setter
    def price2(self, value):
        Car.__price2[str(id(self))] = value


    def parameters(self):
        # metric data system
        return {
            'length': self.length,
            'width': self.width,
        }


class CarAdapted(Car, CarAnalyticsForUSA):

    def parameters_for_usa(self):
        length = round(self.length * 3.28084, 1)
        width = round(self.width * 3.28084, 1)
        result = {
            'length': length,
            'width': width,
        }
        return super(CarAdapted, CarAdapted).parameters_for_usa(result)


if __name__ == "__main__":
    car1 = Car(5.1, 2.2)
    analytics = CarAnalyticsForUSA()

    print(analytics.parameters_for_usa(car1.parameters()))
    print("Its wrong\n\n")

    print("Adapter:")
    car2 = CarAdapted(5.1, 2.2)
    print(car2.parameters_for_usa())
    print(car2.price)
    car1.price2 = 'car1 value'
    car2.price2 = 'car2 value'
    print(car1.price2, '///', car2.price2)
