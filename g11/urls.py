from django.urls import path
from g11 import views

urlpatterns=[]

urlpatterns=[
    path('',views.Login,name='login'),
    path('home',views.home,name='home')
]