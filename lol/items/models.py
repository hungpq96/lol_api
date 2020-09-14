from django.db import models
from champions.models import Champion


class BigItem(models.Model):
    champions = models.ManyToManyField(Champion)

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'name: {self.name}'


class PartialItem(models.Model):
    champions = models.ManyToManyField(Champion)

    name = models.CharField(max_length=50)
    is_recipe = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.name}, is_recipe: {self.is_recipe}'
