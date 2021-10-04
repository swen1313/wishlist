import self as self
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField

    def __str__(self):
        return self.title

