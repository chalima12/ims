import django
import uuid 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse, reverse_lazy

user_type = [
    ('Manager', "manager"),
    ('Registeror', "registeror"),
    ('Engineer', "Engineer"),
    ('Admin', "Admin"),
    ('Other', "Other"),
]
status=[("Pending","pending"),("shipped","shipped")]
# models.py


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)  # Add email field
    user_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)  # Rename pass_word to password
    user_type = models.CharField(choices=user_type, default="Engineer", max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "user_name"  
    REQUIRED_FIELDS = ['email']  

    objects = CustomUserManager()

    def has_module_perms(self, app_label):
        return self.is_superuser or self.is_staff

    def __str__(self):
        return f"{self.first_name.upper()} {self.last_name.upper()}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
       
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return self.name

class Stock(models.Model):
    category = models.ForeignKey(Category, related_name='stocks', on_delete=models.CASCADE)
    current_level = models.IntegerField(default=0)
    Stock_no=models.CharField(max_length=50,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return f"Stock {self.id} in {self.category.name} - Current Level: {self.current_level}"

class Item(models.Model):
    stock = models.ForeignKey(Stock, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,related_name='stocks')
    quantity = models.IntegerField()
    order_date = models.DateField()
    status = models.CharField(choices=status,default='penging',max_length=50)

    def __str__(self):
        return f"Order {self.id} - {self.stock.Stock_no}"

class MaterialRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    request_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Request {self.id} by {self.user.user_name}"



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_date = models.DateField()

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notification_date}"
