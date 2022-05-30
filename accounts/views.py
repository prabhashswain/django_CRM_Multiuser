from django.shortcuts import redirect, render
from accounts.filters import OrderFilter
from accounts.forms import CustomerForm, OrderForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *
from accounts.decorators import admin_only, unauthenticated_user,allowed_user_permission


# Create your views here.
@unauthenticated_user
def registerView(request):
    form = UserForm()
    context = {'form':form}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'auth/register.html',context)

@unauthenticated_user
def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'auth/login.html')

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def indexView(request):
    print(request.user)
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

@login_required(login_url='login')
@allowed_user_permission(allowed_user=['customer'])
def userView(request):
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()
    context = {
        'orders':orders,
        'total_order':total_order,
        'total_delivered':total_delivered,
        'total_pending':total_pending
    }
    return render(request,'pages/user.html',context)

@login_required(login_url='login')
@allowed_user_permission(allowed_user=['admin'])
def ProductView(request):
    products = Product.objects.all()
    return render(request,'pages/product.html',{'products':products})

@login_required(login_url='login')
def CustomerView(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    # filter added
    myfilter = OrderFilter(request.GET,queryset=orders)
    orders = myfilter.qs

    total_order = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'total_order':total_order,
        'myfilter':myfilter
    }
    return render(request,'pages/customers.html',context)

@login_required(login_url='login')
def CreateOrderView(request,pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def DeleteOrderView(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('home')

@login_required(login_url='login')
@allowed_user_permission(allowed_user=['customer'])
def accountSettingView(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    context = {
        'form':form
    }
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('settings')
    return render(request,'pages/account_settings.html',context)