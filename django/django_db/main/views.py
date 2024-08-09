from django.shortcuts import render
from main.models import Phones


def show_catalog(request):
    template = 'catalog.html'
    sort_params = ['name','min_price','max_price']
    sort_ = request.GET.get("sort")
    phones_obj = Phones.objects.all()
    phones_items = {}
    for p in phones_obj:
        phones_items[p.id] = {
            'id': p.id, 
            'name' : p.name,
            'price' : p.price,
            'image' : p.image,
            'lte_exists' : p.lte_exists,
            'release_date': p.release_date,
            'slug' : p.slug,
        }
    if sort_:
        if sort_params.index(sort_) == 0:
            print(f'Sorting by name..')
            sorted_list = []
            data_list = list(phones_items.values())
            sorted_names = sorted([x["name"] for x in data_list])
            for name in sorted_names:
                for x in data_list:
                    if name == x["name"]:
                        sorted_list.append(x)
            phones_items.clear()
            for x in sorted_list:
                phones_items[x["id"]] = x
    
        elif sort_params.index(sort_) == 1:
            print(f'Sorting by min_price..')
            sorted_list = []
            data_list = list(phones_items.values())
            sorted_price = sorted([x["price"] for x in data_list])
            for price in sorted_price:
                for x in data_list:
                    if price == x["price"]:
                        sorted_list.append(x)
            phones_items.clear()
            for x in sorted_list:
                phones_items[x["id"]] = x        
        else:
            print(f'Sorting by max_price..')
            sorted_list = []
            data_list = list(phones_items.values())
            sorted_price = sorted([x["price"] for x in data_list],reverse=True)
            for price in sorted_price:
                for x in data_list:
                    if price == x["price"]:
                        sorted_list.append(x)
            phones_items.clear()
            for x in sorted_list:
                phones_items[x["id"]] = x

    context = {
        'link_catalog': '/catalog',
        'phones' : phones_items
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phones.objects.filter(slug=slug)
    phone_items = {}
    for p in phone_object:
        phone_items[p.id] = {
            'id': p.id, 
            'name' : p.name,
            'price' : p.price,
            'image' : p.image,
            'lte_exists' : p.lte_exists,
            'release_date': p.release_date,
            'slug' : p.slug,
        }
    #print(phone_items)
    context = {
        'link_catalog': '/catalog',
        "phone" : phone_items
    }
    return render(request, template, context)
