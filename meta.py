
class Meta1(type):

    def __new__(mcs, *a, **kw):
        # конструируем класс

        print("entering Meta1.__new__()")
        cls = super(Meta1, mcs).__new__(mcs, *a, **kw)
        print("exiting Meta1.__new__()\n")

        return cls

    def __init__(cls, *a, **kw):
        # инициализируем класс

        print("executing Meta1.__init__()")
        super(Meta1, cls).__init__(*a, **kw)

    def __call__(cls, *a, **kw):
        # вызов класса

        print("-before Class1 instance creation -----")
        obj = super(Meta1, cls).__call__(*a, **kw)
        print("-after Class1 instance creation -----")

        return obj


class Class1(metaclass=Meta1):
    a = 1

    def __init__(self):
        self.name = 'obj 1'
        self.b = 2
        print('init')

    def __new__(cls, *a, **kw):
        print("entering Class_1.__new__()")
        obj = super(Class1, cls).__new__(cls, *a, **kw)
        obj.g = 11
        print("exiting Class_1.__new__()")
        return obj

    def __call__(self, *a, **kw):
        print('hi')


if __name__ == "__main__":
    obj1 = Class1()
