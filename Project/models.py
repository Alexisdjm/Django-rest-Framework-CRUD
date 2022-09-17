from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=128)