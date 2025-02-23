import uuid
from django.db import models
from django.contrib.auth.models import User


class ProductManager(models.Manager):
    def in_stock(self):
        return self.queryset().filter(stock__gt=0)
    def sort_decay(self):
        return self.queryset().order_by('-field', 'price')
    def sort_increasing(self):
        return self.queryset().order_by('field', 'price')

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    attributes = models.ManyToManyField('Attribute')

    objects = ProductManager()

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Attribute(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quntity = models.IntegerField(default=1)