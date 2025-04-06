from django.core.management.base import BaseCommand

from commands.tasks import async_init_admin


class Command(BaseCommand):
    def handle(self, *args, **options):
        async_init_admin.delay()
