from django.db import models
from countries.models import Country


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=30)
    is_official = models.BooleanField(default=False)
    percentage = models.FloatField(max_length=5, default=0.0)
