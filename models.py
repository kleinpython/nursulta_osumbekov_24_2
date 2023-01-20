from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modifate_date = models.DateField(auto_now=True)
