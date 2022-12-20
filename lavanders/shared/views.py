from django.shortcuts import render
from .models import Products
from django import forms

class NewForms(forms.Form):
    name=forms.CharField(label='Name')
    email=forms.CharField(label='Email')
    

# Create your views here.
def index(request):
    return render(request, 'shared/index.html',{
        'products':Products.objects.all()
    })

def order(request, prod_id):
    order_prod=Products.objects.get(pk=prod_id)
    return render(request, 'shared/order.html',{
        'order':order_prod,
    })

def buy(request, buy_id):
    ses=None
    quantity=1
    if 'order_products' in request.session:
        if buy_id in request.session['order_products']:
            request.session['order_products'].remove(buy_id)
        request.session['order_products'].insert(0, buy_id)
        ses=Products.objects.filter(pk__in=request.session['order_products'])
        request.session.set_expiry(600)
    else:
        request.session['order_products']=[buy_id]
        
    prod=Products.objects.get(pk=buy_id)
    request.session.modified=True
    return render(request, 'shared/buy.html',{
        'find':ses,
        'buy_id':buy_id,
        'buy_form':NewForms(),
        'prod':prod,
        'quantity':quantity
    })