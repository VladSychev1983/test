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
    items = {key : round(value * int(servings),1) for key, value in DATA[dish].items()}
    context = {
        "recipe" : items 
    }
    return render(request, template_name, context)