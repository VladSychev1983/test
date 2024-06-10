tuple1 = ("яблоко","апельсин","гранат")
tuple2 = ("груша", "гранат", "груйпфрут")
tuple3 = tuple1 + tuple2
print("Кортеж",tuple3)

tuple1_list = list(tuple1)
tuple2_list = list(tuple2)
tuple1_list.extend(tuple2_list)
tuple3_list = tuple1_list.copy()

print("Список",tuple3_list)


tuple1_set = set(tuple1)
tuple2_set = set(tuple2)
tuple3_set = tuple1_set.union(tuple2_set)

print(tuple1_set)
print(tuple2_set)
print(tuple3_set)





