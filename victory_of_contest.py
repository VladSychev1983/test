# нужно вывести каждый 3-й элемент и посчитать их количество.
receipts = [ 123, 145, 346, 246, 235, 166, 112, 351, 436]
index_step = 3
result = list(receipts[2:len(receipts):3])
len_ = len(result)
print(result)
print(len_)
print("=====================")

counter = 0
for item in range(2,len(receipts),3):
    print(item)
    counter += 1;
print('Counter:',counter)

