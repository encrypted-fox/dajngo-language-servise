from django.db import models


class Country(models.Model):
    CONTINENTS = (
        ("Asia", "Asia"),
        ("Europe", "Europe"),
        ("North America", "North America"),
        ("Africa", "Africa"),
        ("Oceania", "Oceania"),
        ("Antarctica", "Antarctica"),
        ("South America", "South America"),
    )

    code = models.CharField(max_length=3, primary_key=True, unique=True)
    code_2 = models.CharField(max_length=2)
    name = models.CharField(max_length=52)
    continent = models.CharField(max_length=13, choices=CONTINENTS)
    region = models.CharField(max_length=26, default=("Asia", "Asia"))
    surface_area = models.FloatField(max_length=12, default=0.00)
    indep_year = models.SmallIntegerField(default=None, null=True)
    population = models.IntegerField(default=0)
    life_expectancy = models.FloatField(max_length=4, null=True, default=None)
    GNP = models.FloatField(max_length=12, null=True, default=None)
    GNP_old = models.FloatField(max_length=12, null=True, default=None)
    local_name = models.CharField(max_length=45)
    government_form = models.CharField(max_length=45)
    head_of_state = models.CharField(max_length=60, null=True, default=None)
    capital = models.IntegerField(null=True, default=None)
