def next_edge(side1, side2):
    side3 = (side1 + side2) - 1
    return side3

#print(next_edge(8,10))

# Верни мне что-то!

def give_me_something(a):
    #a = a.replace(" ","")
    #a = a.strip()
    str_ = ""
    if (a.isspace() == True):
        str_ = "something" + a
    elif a == "":
        str_ = "something"
    else:
        str_ = "something" + " " + a
    return str_

#print(give_me_something("   "))
#print(give_me_something("is better than"))

def convert_hours_minutes_2_seconds(hours, minutes):
    seconds = (hours * 60 * 60 ) + (minutes * 60)
    return seconds
    
print(convert_hours_minutes_2_seconds(1, 3))

print(9**2)


def difference(nums):
    diff = max(nums) - min(nums)
    return diff
    
print(difference([10, 15, 20, 2, 10, 6]))
# 20 - 2 = 18

def flip(y):
    y = y + 5
    y = str(y)
    y = y.replace("5","1")
    y = y.replace("6","0")
    return y
print(flip(0))
print(flip(1))

def count_syllables(string):
    string = string.lower()
    counter = string.count(string[0:2])
    return counter

print(count_syllables("Hehehehehehe"))     #6

def divides_evenly(a, b):
    return True if a % b == 0 else False
print(divides_evenly(98, 7))   #True
print(divides_evenly(85, 4))

def get_case(string):
    if(string.isupper()):
        return 'верхний'
    elif(string.islower()):
        return 'нижний'
    else:
        return 'смешанный'

print(get_case("whisper..."))   #"нижний"
print(get_case("SHOUT!"))  #"верхний"
print(get_case("Indoor Voice"))

def distance_home(my_list):
    return sum(my_list)
print(distance_home([2, 4, 2, 5]))
print(distance_home([-1, -4, -3, -2]))
print(distance_home([3, 4, -5, -2]))
