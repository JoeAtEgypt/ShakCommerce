from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.management import CommandError


# decorator simplifies the process of creating Celery tasks within
# a Django project. it prevents us to import "celery" in using "celery.task"
# in terms of Reusability of our code, it also makes our code much more reusable resource.
@shared_task
def async_init_admin():
    try:
        created_user, created = get_user_model().objects.get_or_create(
            email="youssefaymanshaker@me.com",
            phone_number="+201010101010",
            first_name="Youssef",
            last_name="Shaker",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        if created:
            created_user.set_password("1877")
            created_user.save()
        print(f"current admin : {created_user}")

    except Exception as e:
        raise CommandError(e)


# @shared_task(name="test_celery_beat")
# def test_celery_beat():
#     print("test_celery_beat")
