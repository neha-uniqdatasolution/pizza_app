from statistics import mode
from tokenize import Number
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class counter(models.Model):
    num = models.CharField(max_length=10)


class Client(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=20)
    email = models.EmailField()
    is_admin = models.BooleanField()
    USER = models.OneToOneField(User, on_delete=models.CASCADE)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.FileField()


class Order(models.Model):
    m_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    u_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
