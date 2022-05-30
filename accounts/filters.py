import django_filters
from accounts.models import Order

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ["product","status"]