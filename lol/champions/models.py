from django.db import models


class Champion(models.Model):
    name = models.CharField(max_length=30)


class Skill(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    count_down = models.IntegerField()
