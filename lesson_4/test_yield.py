def hello_world(n):
    for i in range(n):
        yield 'Hello World!'

for item in hello_world(n=3):
    print(item)


#====================
def my_generator():
    yield "One"
    yield "Two"
    yield "Three"

obj_my_generator = my_generator()
for item in obj_my_generator:
    print(item)


#+========================

def my_range(start,end):
    while start <= end:
        yield start
        start += 1
for item in my_range(1,5):
    print(item)