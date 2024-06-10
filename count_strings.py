def list_of_numbers(n: int) -> list:
    mylist = list(range(1, n+1))
    return mylist
res = list_of_numbers(10)
print(res)

mystr = str(list(range(1,101)))
print(mystr[1:-1])

test_str = '!dlroW olleH'
reverse_str = test_str[::-1]
print(reverse_str)