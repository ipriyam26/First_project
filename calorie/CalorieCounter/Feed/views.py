from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from CalorieCounter.Feed.forms import add_user_food_item, create_user_form, food_item_form
from .decorators import admin_only,unauthorized_user,allowed_users
from .models import *
from .filers import fooditemFilter
# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snack')[0].fooditem_set.all()[:5]
    customers = Customer.objects.all()
    context = {
        'breakfast':breakfast,
        'lunch':lunch,
        'dinner':dinner,
        'snacks':snacks,
        'customers':customers
    }
    return render(request, 'main.html', context)

@login_required(login_url='login')
@admin_only
def fooditem(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snack')[0].fooditem_set.all()
    scnt = snacks.count()
    context={'breakfast':breakfast,
              'bcnt':bcnt,
              'lcnt':lcnt,
              'scnt':scnt,
              'dcnt':dcnt,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
            }
    
    
    return render(request, 'fooditem.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createfooditem(request):
    form = food_item_form()
    if request.method == 'POST':
        form = food_item_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'createfooditem.html', context)

@unauthorized_user
def registerPage(request):
    form = create_user_form()
    if request.method == 'POST':
        form = create_user_form(request.POST)
        if form.is_valid():
            
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=username,email=email,user=user)
            messages.success(request, f'Account was created for {username}')
            return redirect('/login')
    context = {'form':form}
    return render(request, 'register.html', context)

@unauthorized_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    user = request.user
    cust = user.customer
    fooditems = FoodItem.objects.filter()
    myfilter = fooditemFilter(request.GET, queryset=fooditems)
    fooditems= myfilter.qs
    total = UserFoodItem.objects.all()
    myFooditems = total.filter(customer=cust)
    cnt = myFooditems.count()
    querysetFood = [food.fooditem.all() for food in myFooditems]
    finalFoodItems =[]
    for items in querysetFood:
        finalFoodItems.extend(iter(items))
    totalCalories = sum(food.calories for food in finalFoodItems)
    CaloriesLeft = 2000 - totalCalories
    context = {'CalorieLeft':CaloriesLeft,'totalCalories':totalCalories,'cnt':cnt,'foodlist':finalFoodItems,'fooditem':fooditems,'myfilter':myfilter}
    return render(request, 'user.html', context)

def addFooditem(request):
    user=request.user
    cust=user.customer
    if request.method=="POST":
        form =add_user_food_item(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=add_user_food_item()
    context={'form':form}
    return render(request,'addUserFooditem.html',context)

    