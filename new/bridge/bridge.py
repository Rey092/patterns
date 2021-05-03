import time
from abc import ABC, abstractmethod


class FlightSimulator:

    def __init__(self, aircraft):
        self.aircraft = aircraft

    def take_off(self):
        self.aircraft.brake_off()
        self.aircraft.engine_on()
        self.aircraft.speed_up(100)
        self.aircraft.is_flying = True

    def land_on(self):
        self.aircraft.speed_down(100)
        self.aircraft.is_flying = False
        self.aircraft.engine_off()
        self.aircraft.brake()
        self.aircraft.speed_down(0)

    def speed_up(self, speed):
        if self.aircraft.is_flying:
            self.aircraft.speed_up(speed)

    def speed_down(self, speed):
        if self.aircraft.is_flying:
            self.aircraft.speed_down(speed)
            if self.aircraft.speed < 100:
                self.aircraft.is_falling = True
                print('AirCraft is falling. You lose.')


class AirCraft(ABC):

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def brake_off(self):
        pass

    @abstractmethod
    def engine_on(self):
        pass

    @abstractmethod
    def engine_off(self):
        pass

    @abstractmethod
    def speed_up(self, speed):
        pass

    @abstractmethod
    def speed_down(self, speed):
        pass


class Cessna172(AirCraft):
    def __init__(self):
        self.name = 'Cessna-172'
        self.speed = 0
        self.is_braked = True
        self.is_flying = False
        self.is_engine_running = False
        self.is_falling = False

    def brake(self):
        self.is_braked = True
        print('AirCraft is braked')

    def brake_off(self):
        self.is_braked = False
        print('Brake off')

    def engine_on(self):
        self.is_engine_running = True
        print('Engine is on')

    def engine_off(self):
        self.is_engine_running = False
        print('Engine is off')

    def speed_up(self, speed):
        if self.is_braked and not self.is_flying:
            print(r'You can\'t speed up while aircraft is on the brake')
        else:
            if self.is_engine_running and speed > self.speed:
                for _ in range(int((speed - self.speed) / 20)):
                    time.sleep(0.2)
                    print('AirCraft picking up speed...')
                self.speed = speed

    def speed_down(self, speed):
        if self.is_engine_running and speed < self.speed:
            for _ in range(int((self.speed - speed) / 15)):
                time.sleep(0.3)
                print('AirCraft slowing down...')
            self.speed = speed


class GregaAirCamper(AirCraft):
    def __init__(self):
        self.name = 'Grega GN-1 AirCamper'
        self.speed = 0
        self.is_braked = True
        self.is_flying = False
        self.is_engine_running = False
        self.is_falling = False

    def brake(self):
        self.is_braked = True
        print('AirCraft is braked')

    def brake_off(self):
        self.is_braked = False
        print('Brake off')

    def engine_on(self):
        self.is_engine_running = True
        print('Engine is on')

    def engine_off(self):
        self.is_engine_running = False
        print('Engine is off')

    def speed_up(self, speed):
        if self.is_braked and not self.is_flying:
            print(r'You can\'t speed up while aircraft is on the brake')
        else:
            if self.is_engine_running and speed > self.speed:
                for _ in range(int((speed - self.speed) / 15)):
                    time.sleep(0.3)
                    print('AirCraft picking up speed...')
                self.speed = speed

    def speed_down(self, speed):
        if self.is_engine_running and speed < self.speed:
            for _ in range(int((self.speed - speed) / 25)):
                time.sleep(0.4)
                print('AirCraft slowing down...')
            self.speed = speed


def client_code(interface, upper, downer) -> None:
    print('Take off:')
    interface.take_off()
    print('Speed up:')
    interface.speed_up(upper)
    print('Speed down:')
    interface.speed_down(downer)
    if not interface.aircraft.is_falling:
        print('Land on:')
        interface.land_on()


if __name__ == "__main__":
    aircraft1 = Cessna172()
    simulator1 = FlightSimulator(aircraft1)
    client_code(simulator1, 200, 150)

    print("\n")

    aircraft2 = GregaAirCamper()
    simulator2 = FlightSimulator(aircraft2)
    client_code(simulator2, 300, 40)
