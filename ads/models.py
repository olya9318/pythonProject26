from django.db import models


# Create your models here.

class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=60)
