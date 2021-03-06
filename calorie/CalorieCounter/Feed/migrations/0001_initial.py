# Generated by Django 4.0.5 on 2022-06-25 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('fats', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('category', models.ManyToManyField(to='Feed.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(blank=True, to='Feed.customer')),
                ('food_item', models.ManyToManyField(to='Feed.fooditem')),
            ],
        ),
    ]
