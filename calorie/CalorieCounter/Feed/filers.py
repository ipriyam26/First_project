import django_filters

from .models import FoodItem

class foodItemFilter(django_filters.FilterSet):
    class Meta:
        model = FoodItem
        fields = ['name']
