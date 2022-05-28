from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/dashboard.html')

def Product(request):
    return render(request,'pages/product.html')

def Customer(request):
    return render(request,'pages/customers.html')