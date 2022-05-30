from django.shortcuts import redirect, render
from accounts.forms import OrderForm
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

def CreateOrderView(request):
    form = OrderForm()
    context = {
        'form':form,
        'title':'Create Order'
    }
    if request.method == "POST":
        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
            return redirect('home')
    return render(request,'pages/create_order.html',context)

def UpdateOrderView(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {
        'form':form,
        'title':'Update Order'
    }
    if request.method == "POST":
        f = OrderForm(request.POST,instance=order)
        if f.is_valid():
            f.save()
            return redirect('home')
    return render(request,'pages/create_order.html',context)

def DeleteOrderView(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('home')

