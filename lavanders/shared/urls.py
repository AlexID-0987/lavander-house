from django.urls import path
from . import views
#first page
urlpatterns=[ 
    path('',views.index,name='beginen'),
    path('<int:prod_id>', views.order, name='order'),
    path('buy/<int:buy_id>/', views.buy, name='buy'),
    path('buyProduct/<int:id>/', views.buyProduct, name='buyProd'),
    path('save', views.save, name='save')
]