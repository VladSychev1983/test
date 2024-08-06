from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def cookbook(request,dish):
    context ={}
    template_name = 'recipes.html'
    servings = request.GET.get("servings", 1)
    items_list = [DATA[dish] for item in DATA]
    for key,value in items_list[0].items():    
        context[key] = round(value * int(servings),1)
    context_new = {
        "recipe" : context 
    }
    return render(request, template_name, context_new)