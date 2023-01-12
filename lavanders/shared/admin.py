from django.contrib import admin
from .models import Products,Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product','price')
    
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','products','summa')

admin.site.register(Products, ProductAdmin)
admin.site.register(Order, OrderAdmin)

