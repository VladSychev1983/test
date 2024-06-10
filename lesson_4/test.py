class HelloWorldIterator:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.counter = 0
        print("Цикл начинается")
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter > self.n:
            print("Цикл завершается")
            raise StopIteration
        return 'Hello World!'

hello_world_iterator = HelloWorldIterator(n=3)
for item in hello_world_iterator:
    print(item)


# как работает iter и next итерирование построчное.

mylist = [1,2,3,4,5]
myiter = iter(mylist)
print(next(myiter))
print(next(myiter))
print(next(myiter))