from django.db import models
from django.contrib.auth.models import User

class DateStatus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

# Create your models here.
class Customer(DateStatus):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(null=True,blank=True,default='profile.png')
    

    def __str__(self) -> str:
        return self.user.username

class Tag(DateStatus):
    name = models.CharField(max_length=100,null=True)
    

    def __str__(self) -> str:
        return self.name

class Product(DateStatus):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name

class Order(DateStatus):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=100,choices=STATUS)


    def __str__(self) -> str:
        return self.status