from django.shortcuts import render
from main.models import Phones


def show_catalog(request):
    template = 'catalog.html'
    phones_obj = Phones.objects.all()
    phones_items = {}
    for p in phones_obj:
        phones_items[p.id] = { 
            'name' : p.name,
            'price' : p.price,
            'image' : p.image,
            'lte_exists' : p.lte_exists,
            'release_date': p.release_date,
            'slug' : p.slug,
        }
    context = {
        'phones' : phones_items
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
