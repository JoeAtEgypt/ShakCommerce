from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from commands.tasks import async_init_admin


class Command(BaseCommand):
    def handle(self, *args, **options):
        async_init_admin.delay()
