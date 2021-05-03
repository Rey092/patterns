from abc import ABC, abstractmethod
from faker import Faker
fake = Faker()


class NewArticleHandler(ABC):

    @abstractmethod
    def attach(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def published_new_article(self):
        pass


class ScienceArticleHandler(NewArticleHandler):

    def __init__(self):
        self.articles_count = 5
        self.subscriptions = []

    def attach(self, subscription):
        print("Subscriber attached.")
        self.subscriptions.append(subscription)

    def detach(self, subscription):
        print("Subscriber detached.")
        self.subscriptions.remove(subscription)

    def notify(self):
        print("Notifying Subscribers...")
        email_list = []
        for subscription in self.subscriptions:
            email_list.append(subscription.email)

        send_email(email_list)

    def published_new_article(self):
        self.articles_count += 1
        self.notify()


def send_email(email_list):
    # async task
    for email in email_list:
        print(f'Email sent on {email}')
        # TODO: implement email sending


class Subscription:
    def __init__(self):
        self.email = f'{fake.email()}'


if __name__ == "__main__":
    event_handler = ScienceArticleHandler()

    print('\n')
    subscription_1 = Subscription()
    event_handler.attach(subscription_1)

    print('\n')
    subscription_2 = Subscription()
    event_handler.attach(subscription_2)

    print('\n')
    event_handler.published_new_article()
    event_handler.published_new_article()

    print('\n')
    event_handler.detach(subscription_2)

    print('\n')
    event_handler.published_new_article()
