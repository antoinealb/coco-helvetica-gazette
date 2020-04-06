from django.core.management.base import BaseCommand, CommandError

from pages.models import TextTestimonial
from pages.tags import ALLOWED_TAGS


TEXT = """Il n'y avait pas un mot à répondre.
Je remontai dans ma chambre.  Graüben me suivit.
Ce fut elle qui se chargea de mettre en ordre, dans une petite valise, les objets nécessaires à mon voyage.
Elle n'était pas plus émue que s'il se fût agi d'une promenade à Lubeck ou à Heligoland; ses petites mains allaient et venaient sans précipitation; elle causait avec calme; elle me donnait les raisons les plus sensées en faveur de notre expédition.
Elle m'enchantait, et je me sentais une grosse colère contre elle.
Quelquefois je voulais m'emporter, mais elle n'y prenait garde et continuait méthodiquement sa tranquille besogne.
Enfin la dernière courroie de la valise fut bouclée.  Je descendis au rez-de-chaussée.
Pendant cette journée les fournisseurs d'instruments de physique, d'armes, d'appareils électriques s'étaient multipliés.
La bonne Marthe en perdait la tête.
"""


class Command(BaseCommand):
    help = "Creates a set of predefined contents"

    def handle(self, *args, **options):
        for t in TEXT.splitlines():
            TextTestimonial.objects.create(text=t)
