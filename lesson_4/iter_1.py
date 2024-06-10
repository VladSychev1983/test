class MyIterator:

    def __init__(self):
        pass

    def __iter__(self):
        print("Вход в цикл")
        return self

    def __next__(self):
        print("Новая итерация")

        if ...:
            raise StopIteration

        return "item"


my = MyIterator()

for item in my:
    pass

for item in MyIterator():
    print(item)
