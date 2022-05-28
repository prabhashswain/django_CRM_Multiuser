from django.contrib import admin
from accounts.models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','created_at','updated_at']
    list_filter = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','description','get_tags']

    def get_tags(self, obj):
        return "\n".join([p.name for p in obj.tag.all()])

@admin.register(Tag)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status']

