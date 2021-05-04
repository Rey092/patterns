import time
from abc import ABC, abstractmethod
from random import randint
from termcolor import colored


class GameCharacter(ABC):
    def change_strategy(self, new_strategy):
        pass

    def action(self, enemy):
        pass

    @staticmethod
    @abstractmethod
    def attack(enemy):
        pass

    @staticmethod
    @abstractmethod
    def power_attack(enemy):
        pass


class Hero(GameCharacter):
    def __init__(self, strategy):
        self._strategy = strategy
        self._strategy.character = self
        self.hp = 300
        self.defence = False
        self.magic_power = 7

    def change_strategy(self, new_strategy):
        self._strategy = new_strategy
        self._strategy.character = self

    def action(self, enemy):
        self._strategy.do_algorithm(enemy)

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def heal(self):
        self.hp += self.magic_power
        print(f'Hero heal up {self.magic_power} HP')
        self.magic_power += 1

    @staticmethod
    def attack(enemy):
        attack = randint(20, 30)
        print(f'Hero attacks and deals {attack} Damage')
        enemy.hp -= attack

    @staticmethod
    def power_attack(enemy):
        attack = randint(40, 50)
        print(f'Hero casts fireball and deals {attack} Damage')
        enemy.hp -= attack

    def defend(self):
        print('Hero uses defence')
        self.defence = True


class Goblin(GameCharacter):
    def __init__(self, strategy):
        self._strategy = strategy
        self._strategy.character = self
        self.hp = 1200
        self.defence = False
        self.last_attack = None

    def change_strategy(self, new_strategy):
        self._strategy = new_strategy
        self._strategy.character = self

    def action(self, enemy):
        self._strategy.do_algorithm(enemy)

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self, enemy):
        attack = randint(10, 25)
        if enemy.defence:
            attack = int(attack/2)
        print(f'Goblin attacks and deals {attack} Damage')
        enemy.hp -= attack
        self.last_attack = attack

    @staticmethod
    def power_attack(enemy):
        attack = randint(13, 20) * 2
        if enemy.defence:
            attack = int(attack/2)
        print(f'Goblin uses power attack and deals {attack} Damage')
        enemy.hp -= attack


class Strategy(ABC):
    def __init__(self):
        self._character = None

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        self._character = character

    @abstractmethod
    def do_algorithm(self, enemy):
        pass


class HeroStandardStrategy(Strategy):
    def do_algorithm(self, enemy):
        self.character.attack(enemy)
        self.character.heal()
        self.character.defend()
        if self.character.hp > 200:
            self.character.change_strategy(HeroAttackStrategy())
            print(colored('Hero chooses HeroAttackStrategy', 'red'))
        elif self.character.hp < 100:
            self.character.change_strategy(HeroHealingStrategy())
            print(colored('Hero chooses HeroHealingStrategy', 'green'))


class HeroHealingStrategy(Strategy):
    def do_algorithm(self, enemy):
        self.character.heal()
        self.character.heal()
        self.character.defend()
        if self.character.hp > 100:
            self.character.change_strategy(HeroStandardStrategy())
            print(colored('Hero chooses HeroStandardStrategy', 'blue'))


class HeroAttackStrategy(Strategy):
    def do_algorithm(self, enemy):
        self.character.attack(enemy)
        self.character.attack(enemy)
        self.character.power_attack(enemy)
        if self.character.hp < 200:
            self.character.change_strategy(HeroStandardStrategy())
            print(colored('Hero chooses HeroStandardStrategy', 'blue'))
        elif self.character.hp < 100:
            self.character.change_strategy(HeroHealingStrategy())
            print(colored('Hero chooses HeroHealingStrategy', 'green'))


class GoblinStandardStrategy(Strategy):
    def do_algorithm(self, enemy):
        self.character.attack(enemy)
        self.character.attack(enemy)
        self.character.attack(enemy)
        self.character.attack(enemy)
        enemy.defence = False
        if self.character.last_attack < 13:
            self.character.change_strategy(GoblinAngryStrategy())


class GoblinAngryStrategy(Strategy):
    def do_algorithm(self, enemy):
        self.character.power_attack(enemy)
        self.character.attack(enemy)
        self.character.power_attack(enemy)
        enemy.defence = False
        self.character.change_strategy(GoblinStandardStrategy())


if __name__ == "__main__":

    hero = Hero(HeroStandardStrategy())
    goblin = Goblin(GoblinStandardStrategy())

    while True:
        hero.action(goblin)
        goblin.action(hero)

        battle_log = f'Hero - {hero.hp} HP /// Goblin - {goblin.hp} HP'
        print(colored(battle_log, 'cyan'))

        time.sleep(0.3)

        if hero.is_dead():
            print('Hero is dead. Game Over.')
            break
        if goblin.is_dead():
            print('Goblin is dead. Hero wins.')
            break
