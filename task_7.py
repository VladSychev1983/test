import re

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
print(cook_book)

def get_shop_list_by_dishes(dishes,person_count):
    result_dict = {}
    for find_dish in dishes:
        for dish,lists in cook_book.items():
            if find_dish == dish:
                for dicts in lists:
                    new_quantity = int(dicts["quantity"]) * 2
                    result_dict[dicts["ingredient_name"]] = {'measure': dicts["measure"], 'quantity' : new_quantity}
    print(result_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    