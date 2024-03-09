import re
import os

cook_book ={}
with open("recipes.txt","r",encoding="utf-8") as file:
    data = file.read().strip()
    dishes = re.split(r"\n\n",data)
    for idx,dish in enumerate(dishes):
        ingredients = dish.split("\n")
        list_ingredients = []
        for x in ingredients[2:]:
            ingredient_name,quantity,measure = x.split("|")
            list_ingredients.append({'ingredient_name': ingredient_name.strip(),'quantity': quantity.strip() ,'measure': measure.strip()})
            cook_book[ingredients[0]] = list_ingredients
print("===Task1===")
print(cook_book)

def get_shop_list_by_dishes(dishes,person_count):
    result_dict = {}
    for find_dish in dishes:
        for dish,lists in cook_book.items():
            if find_dish == dish:
                for dicts in lists:
                    new_quantity = int(dicts["quantity"]) * 2
                    result_dict[dicts["ingredient_name"]] = {'measure': dicts["measure"], 'quantity' : new_quantity}
    
    print("===Task2===")
    print(result_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print("===Task3===")

def sum_files():
    file1_lines = []
    file2_lines = []

    with open("1.txt", "r",encoding="utf-8") as f:
       filename_extension = os.path.basename(os.path.abspath("1.txt")).split('/')[-1]
       print(os.path.basename(os.path.abspath("1.txt")).split('/')[-1])
       filename,extension = filename_extension.split(".")
       file1_lines.append(filename_extension +'\n')
       file1_lines.append(filename +'\n')
       for line in f:
           file1_lines.append(line)

    with open("2.txt", "r",encoding="utf-8") as f:
         filename_extension = os.path.basename(os.path.abspath("2.txt")).split('/')[-1]
         filename,extension = filename_extension.split(".")
         file2_lines.append(filename_extension +'\n')
         file2_lines.append(filename +'\n')
         for line in f:
           file2_lines.append(line)

    file1_lines[-1] = file1_lines[-1] + '\n'
    file2_lines[-1] = file2_lines[-1] + '\n'

    print(file1_lines)
    print(file2_lines)

    if len(file1_lines) < len(file2_lines):
        with open("result.txt","w",encoding="utf-8") as f:
            for line in file1_lines:
                f.write(line)
        with open("result.txt","a",encoding="utf-8") as f:
            for line in file2_lines:
                f.write(line)
    else:
        with open("result.txt","w",encoding="utf-8") as f:
            for line in file2_lines:
                f.write(line)
        with open("result.txt","a",encoding="utf-8") as f:
            for line in file1_lines:
                f.write(line)
        print("Done")

sum_files()

