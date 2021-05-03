from threading import Lock

# в logging уже встроен синглтон + в джанго есть log handler


class SingletonBaseClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class CustomLogger(metaclass=SingletonBaseClass):

    @staticmethod
    def log(message):
        print(message)


if __name__ == "__main__":
    logger1 = CustomLogger()
    logger2 = CustomLogger()

    print(logger1)
    print(logger2)

    print(id(logger1) == id(logger2))
