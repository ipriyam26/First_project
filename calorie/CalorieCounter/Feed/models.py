from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    options = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    name = models.CharField(max_length=50,choices=options)
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField(Category)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True,default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True,default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, null=True,default=0)
    calories = models.DecimalField(max_digits=5, decimal_places=2, null=True,default=0)
    
    def save(self, *args, **kwargs):
        self.calories = self.carbohydrates*4 + self.protein*4 + self.fats*9
        super(FoodItem, self).save(*args, **kwargs)


class UserFoodItem(models.Model):
    customer = models.ManyToManyField(Customer,blank=True)
    food_item = models.ManyToManyField(FoodItem)
    
    
