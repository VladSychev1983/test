items = [1, 4, 6]
items_sq = [item * item for item in items if item > 1]
items_sq_gen = (item * item for item in items if item > 1)
# for item in items:
#     items_sq.append(item * item)
for item in items_sq_gen:
    print(item)
