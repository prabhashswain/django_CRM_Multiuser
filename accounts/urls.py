from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.indexView,name='home' ),
    path('products',views.ProductView,name='product' ),
    path('customers/<int:pk>',views.CustomerView,name='customer' ),
]
