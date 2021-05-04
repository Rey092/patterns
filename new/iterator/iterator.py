from collections.abc import Iterable, Iterator


class EvenIndexIterator(Iterator):

    def __init__(self, lst):
        self._lst = lst
        self._position = 0

    def __next__(self):
        try:
            value = self._lst[self._position]
            self._position += 2
        except IndexError:
            raise StopIteration()

        return value


class OddIndexIterator(Iterator):

    def __init__(self, lst):
        self._lst = lst
        self._position = 1

    def __next__(self):
        try:
            value = self._lst[self._position]
            self._position += 2
        except IndexError:
            raise StopIteration()

        return value


class Collection(Iterable):

    def __init__(self):
        self._lst = []

    def __iter__(self):
        # even iterator
        return EvenIndexIterator(self._lst)

    def odd_index_iterator(self):
        # odd iterator
        return OddIndexIterator(self._lst)

    def add_item(self, element):
        self._lst.append(element)


if __name__ == "__main__":

    collection = Collection()
    collection.add_item("Index 0")
    collection.add_item("Index 1")
    collection.add_item("Index 2")
    collection.add_item("Index 3")
    collection.add_item("Index 4")
    collection.add_item("Index 5")

    print('even iterator:')
    for item in collection:
        print(item)

    print('\nodd iterator:')
    for item in collection.odd_index_iterator():
        print(item)
