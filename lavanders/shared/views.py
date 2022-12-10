from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    return render(request, 'shared/index.html',{
        'products':Products.objects.all()
    })

def order(request, prod_id):
    order_prod=Products.objects.get(pk=prod_id)
    return render(request, 'shared/order.html',{
        'order':order_prod
    })