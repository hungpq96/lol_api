from django.core.management.base import BaseCommand

from champions.models import Champion, Skill
from items.models import BigItem, PartialItem
from runes.models import Rune
from spells.models import Spell


class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO: add real data
        # ref:
        # https://docs.djangoproject.com/en/3.1/topics/db/queries/
        runes = Rune.objects.all()

        if not runes.exists():
            runes_data = [
                {'name': 'Press The Attack', 'count_down': 6},
                {'name': 'Lethal Tempo', 'count_down': 6},
            ]
            for rune_data in runes_data:
                rune = Rune(
                    name=rune_data['name'],
                    count_down=rune_data['count_down'],
                )
                rune.save()
