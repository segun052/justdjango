from django.db import models
class Product(models.Model):
    title       = models.CharField(max_length= 120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits= 1000)
    summary     = models.TextField(blank= True, default= 'this item is valid')
    instock    = models.BooleanField(default=True)
# Create your models here.
