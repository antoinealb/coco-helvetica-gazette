from django.core.management.base import BaseCommand, CommandError

from pages.models import Tag
from pages.tags import ALLOWED_TAGS


class Command(BaseCommand):
    help = "Creates a set of predefined hashtags"

    def handle(self, *args, **options):
        self.stdout.write("creatings tags:\n")

        for t, _ in ALLOWED_TAGS:
            self.stdout.write("- " + t)

        for t, _ in ALLOWED_TAGS:
            Tag.objects.create(name=t)
