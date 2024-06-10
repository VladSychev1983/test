def my_range(start, end):
    while start < end:
        yield start
        start += 1


for item in my_range(1, 5):
    print(item)
