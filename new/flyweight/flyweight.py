import requests
from random import randint


class HumanFlyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def attack(self, hit_points):
        unit_type = self._shared_state['title']
        atk = self._shared_state['ATK']
        print(f"{unit_type} ({hit_points} HP) attacks and deals [{atk}] damage")


class Soldier:
    def __init__(self, hit_points, flyweight):
        self.hit_points = hit_points
        self._flyweight = flyweight

    def attack(self):
        self._flyweight.attack(self.hit_points)


class HumanFlyweightFactory:

    def __init__(self):
        self._flyweights = {}

    @staticmethod
    def __get_key(state):
        return hash("_".join((state['title'],
                              str(state['ATK']),
                              str(state['DEF']))))

    def get_flyweight(self, shared_state):
        key = self.__get_key(shared_state)
        data = self._flyweights.get(key)

        if not data:
            print("Creating new flyweight.")
            self._flyweights[key] = HumanFlyweight(shared_state)
        else:
            print("Reusing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self):
        print(list(self._flyweights.values()))


def create_soldier(fly_factory, shared_state, hit_points):
    flyweight = fly_factory.get_flyweight(shared_state)
    soldier_inst = Soldier(hit_points=hit_points, flyweight=flyweight)
    return soldier_inst


if __name__ == "__main__":

    spearman_model = requests.get(
        'https://w7.pngwing.com/pngs/785/29/png-transparent-one-piece-treasure-cruise-spearman-s-rank'
        '-correlation-coefficient-sabo-grand-line-one-piece.png')
    archer_model = requests.get(
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.ie%2Fpin%2F364932376031679216%2F&psig'
        '=AOvVaw0aBXiKQmsjAd2GYvEV2ScY&ust=1620043605715000&source=images&cd=vfe&ved'
        '=0CAIQjRxqFwoTCKihuO_6qvACFQAAAAAdAAAAABAD')

    factory = HumanFlyweightFactory()

    shared_state_spearman = {'model': spearman_model, 'title': 'England Spearman', 'ATK': 40, 'DEF': 35}
    shared_state_archer = {'model': archer_model, 'title': 'England Archer', 'ATK': 50, 'DEF': 15}

    army = []

    for i in range(10):
        spearman = create_soldier(fly_factory=factory,
                                  shared_state=shared_state_spearman,
                                  hit_points=randint(40, 50))
        army.append(spearman)
        if i > 2 and i % 3 == 0:
            archer = create_soldier(fly_factory=factory,
                                    shared_state=shared_state_archer,
                                    hit_points=randint(10, 15))
            army.append(archer)

    for soldier in army:
        soldier.attack()

    print('\nflyweights:')
    factory.list_flyweights()
