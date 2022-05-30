from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.indexView,name='home' ),
    path('register',views.registerView,name='register'),
    path('login',views.loginView,name='login'),
    path('logout',views.logoutView,name='logout'),
    path('products',views.ProductView,name='product' ),
    path('customers/<int:pk>',views.CustomerView,name='customer'),
    path('create-order/<int:pk>',views.CreateOrderView,name='create-order'),
    path('update-order/<int:pk>',views.UpdateOrderView,name='update-order'),
    path('delete-order/<int:pk>',views.DeleteOrderView,name='delete-order'),
]
