from django.shortcuts import render
from accounts.models import *

# Create your views here.
def indexView(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()

    context = {
        'customers':customers,
        'orders':orders,
        'total_order':total_order,
        'total_delivered':total_delivered,
        'total_pending':total_pending
    }
    return render(request,'pages/dashboard.html',context)

def ProductView(request):
    products = Product.objects.all()
    return render(request,'pages/product.html',{'products':products})

def CustomerView(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'total_order':total_order
    }
    return render(request,'pages/customers.html',context)