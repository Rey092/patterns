from abc import ABC, abstractmethod


class Executor(ABC):
    @abstractmethod
    def get_data(self):
        pass


class CharField:
    def __init__(self, text):
        self.text = text

    def get_data(self):
        return self.text


class EmailField:
    def __init__(self, email):
        self.email = email

    def get_data(self):
        return self.email


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Print(Command):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        print('Print:', self.__executor.get_data())


class Save(Command):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        with open('log.txt', 'a+') as file:
            file.write(self.__executor.get_data())
            file.write('\n')


class Handler:

    @staticmethod
    def char_field_handler(char_field):
        print(f'CharField: {char_field.get_data()}')

    @staticmethod
    def email_handler(email_field):
        print(f'EmailField: {email_field.get_data()}')


class SendTo(Command):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self):
        if isinstance(self.__executor, CharField):
            Handler.char_field_handler(self.__executor)
        elif isinstance(self.__executor, EmailField):
            Handler.email_handler(self.__executor)
        else:
            raise Exception('Wrong data type')


class CommandManager:
    def __init__(self):
        self.command_list = []

    def add_command(self, command):
        self.command_list.append(command)

    def execute(self):
        if not self.command_list:
            print("Command list is empty")
        else:
            for command in self.command_list:
                command.execute()
        self.command_list.clear()


if __name__ == "__main__":
    char1 = CharField('Hello World!')
    email1 = EmailField('hello@world.com')
    email2 = EmailField('email@field.com')

    manager = CommandManager()

    manager.add_command(Save(char1))
    manager.add_command(Print(email1))
    manager.add_command(SendTo(email2))

    manager.execute()
