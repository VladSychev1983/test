from django.shortcuts import render
from main.models import Order

def list_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request,'orders.html',context)
