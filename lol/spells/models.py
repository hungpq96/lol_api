from django.db import models
from champions.models import Champion


class Spell(models.Model):
    champions = models.ManyToManyField(Champion)

    name = models.CharField(max_length=50)
    count_down = models.IntegerField()
