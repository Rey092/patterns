import copy


class Pizza:
    d = 4

    def __init__(self, name, cooking_time=5, some_list=None):
        if some_list is None:
            some_list = [1, 2, 3]
        self.name = name
        self.cooking_time = cooking_time
        self.some_list = some_list

    def __str__(self):
        return f"Pizza name: {self.name}, cooking time: {self.cooking_time} minutes"

    def clone(self):
        return type(self)(
            self.name,
            self.cooking_time,
            copy.deepcopy(self.some_list),
        )


if __name__ == "__main__":
    pizza = Pizza("Margarita", 10)

    print(id(pizza))
    new_pizza = pizza.clone()  # клонируем объект
    new_pizza.name = "New_Margarita"
    print(id(new_pizza))
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.name = "Salami"
    print(id(salami_pizza))

    Pizza.d = 6

    print(pizza.some_list)
    pizza.some_list = [9, 9, 9]
    print(pizza.some_list)

    print(new_pizza.some_list)
    print(salami_pizza.some_list)
