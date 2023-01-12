from django.shortcuts import render
from .models import Products, Order
from django import forms



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
    mess='Not key'
    if 'order_products' in request.session:
        if buy_id in request.session['order_products']:
            request.session['order_products'].insert(0, buy_id)
            request.session['order_products'].remove(buy_id)
        request.session['order_products'].insert(0, buy_id)
        ses=Products.objects.filter(pk__in=request.session['order_products'])
        sesionKey=request.session.session_key
        request.session.set_expiry(600)
    else:
        request.session['order_products']=[buy_id]
        
    prod=Products.objects.get(pk=buy_id)
    request.session.modified=True


    return render(request, 'shared/buy.html',{
        'find':ses,
        'buy_id':buy_id,
        'prod':prod,
        
        
        
        
        
        
    })

def buyProduct(request, id):
    quant=1
    buyprod=Products.objects.get(pk=id)
    
    return render(request, 'shared/buyProduct.html',{
        'myProd':buyprod,
        'quant':quant,
    
        
        
        
        
    })

def save(request):
    price=int(request.POST['price'])
    quantity=int(request.POST['quantity'])
    rez=price*quantity
    order=Order()
    order.name=request.POST['user']
    order.phone=request.POST['phone']
    order.email=request.POST['email']
    order.products=request.POST['product']
    order.price=request.POST['price']
    order.quantity=request.POST['quantity']
    order.summa=rez
    order.save()
    id=request.POST['id']
    
    return render(request, 'shared/buyProduct.html',{
        'id':id,
        'rez':rez
    }) 