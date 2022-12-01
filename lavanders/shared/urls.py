from django.urls import path
from . import views
#first page
urlpatterns=[ 
    path('',views.index,name='beginen')
]