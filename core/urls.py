from django.urls import path
from . import views

urlpatterns =  [
    path('', views.clothMeasure, name = "clothMeasure"),
    path('prevAmount/', views.prevAmount, name="prevAmount"),
    path('totalInfo/', views.totalInfo, name="totalInfo"),
    path('shopevents/', views.ShopEventView, name="shopevents"),
    path('total/', views.TotalSell)
]