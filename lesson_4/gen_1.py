def my_generator():

    for item in range(1, 10):
        ...
        yield item


for item in my_generator():
    print(item)
