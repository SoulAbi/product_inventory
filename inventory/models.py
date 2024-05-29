from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name
