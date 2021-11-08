from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    store_id = models.IntegerField()
    salary = models.FloatField()
    manager = models.BooleanField()
    client = models.BooleanField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} manager = {self.manager} pass = {self.password}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    store_id = models.IntegerField()
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.quantity} - {self.price}"
