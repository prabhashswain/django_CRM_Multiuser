from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_user_permission(allowed_user=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_user:
                return view_func(request,*args,**kwargs)
            else:
                messages.error(request,"You don't have admin permission")
                return redirect('logout')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "customer":
            return redirect('user-page')

        if group == "admin":
            return view_func(request,*args,**kwargs)

        return redirect('logout')
    return wrapper_func