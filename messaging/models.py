from django.db import models


# Create your models here.
# Example models from django
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=61)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

