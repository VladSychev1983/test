
hare_distances =  [8, 5, 3, 2, 0, 1, 1]
turtle_distances = [3, 3, 3, 3, 3, 3, 3]

hare_all = 0
for a in hare_distances:
    hare_all +=  a
turtle_all = 0
for b in turtle_distances:
    turtle_all += b

if hare_all < turtle_all:
    result = 'черепаха'
elif hare_all > turtle_all:
    result = 'заяц'
else:
    result = 'одинаково'
return result

    