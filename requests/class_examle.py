import requests
import time as t
import os
from datetime import datetime, date, time
time_now = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
print(f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}')
print(time_now)

# url = "https://netology.ru"
# response = requests.get(url)
# print(response.text)


def myFun(*argv):
    for arg in argv:
        print(arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun1(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# Driver code
myFun1(first='Geeks', mid='for', last='Geeks')


# defining car class
class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
 
 
# creating objects of car class
audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')
 
# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)


# defining car class
class car1():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']
 

# creating objects of car class
audi = car1(s=200, c='red')
bmw = car1(s=250, c='black')
mb = car1(s=190, c='white')
 
# printing the color and speed of cars
print(bmw.color)
print(bmw.speed)


t.sleep(10)

# current_directory = os.getcwd()
# print(current_directory)
# if not os.path.isdir(current_directory +'/vk_images'):
#     os.makedirs(current_directory +'/vk_images')
dict_test = {"href": { "file_name":"ll", "size":"z"} }

print(dict_test["href"]["file_name"])

