from django.forms import ModelForm
from .models import FoodItem,User,UserFoodItem

class food_item_form(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name','category','carbohydrates','protein','fats','calories']
        exclude = ['calories']

class add_user_food_item(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = ['customer','food_item']
    
class create_user_form(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
