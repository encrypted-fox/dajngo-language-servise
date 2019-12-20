from django.db import models
from countries.models import Country


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    district = models.CharField(max_length=20)
    population = models.IntegerField(default=0)
