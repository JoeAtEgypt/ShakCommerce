from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            created_user, created = get_user_model().objects.get_or_create(
                email="youssefaymanshaker@me.com",
                username="joe",
                first_name="Youssef",
                last_name="Shaker",
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
            if created:
                created_user.set_password("1877")
                created_user.save()
            print("current admin : ", created_user)

        except Exception as e:
            raise CommandError(e)
