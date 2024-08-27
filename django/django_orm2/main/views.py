from django.shortcuts import render
from main.models import Order

def list_orders(request):
    #фильтр по цене больше 600 руб.
    # orders = Order.objects.filter(positions__product__price__gte=600)
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request,'orders.html',context)
