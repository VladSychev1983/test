class FlatIterator:
    def __init__(self, list_of_lists):
        self.mylist = sum(list_of_lists,[])
        self.length_mylist = len(self.mylist)
        self.result =  []

    def __iter__(self):
        self.myiter = iter(self.mylist)
        self.counter = 0
        return self
    
    def __next__(self):
        item = next(self.myiter)
        self.counter += 1
        if self.length_mylist < self.counter:
            raise StopIteration
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()