from django.db import models
# from lol.items.models import BigItem, PartialItem
# from lol.runes.models import Rune
# from lol.spells.models import Spell


class Champion(models.Model):
    # big_items = models.ManyToManyField(BigItem)
    # partial_items = models.ManyToManyField(PartialItem)
    # runes = models.ManyToManyField(Rune)
    # spells = models.ManyToManyField(Spell)

    name = models.CharField(max_length=30)


class Skill(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    count_down = models.IntegerField()
