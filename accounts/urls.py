from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name='home' ),
    path('products',views.Product,name='product' ),
    path('customers',views.Customer,name='customer' ),
]
