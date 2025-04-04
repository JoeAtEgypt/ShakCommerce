import os
from celery import Celery

# allow celery to access these settings in the Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shakcommerce.settings")

#  Register the project to celery
app = Celery("shakcommerce")

# Namespace for looking for any settings that related to Celery that's starts with "CELERY "
app.config_from_object("django.conf:settings", namespace="CELERY")

# whenever we create a new task in Celery, we will need to register that task
# to Celery.


# by using "app.task", we are registering this task with Celery, so Celery
# can find this task and then be ready to actually execute this task
# whenever it is requested


## Warning: Adding functions here in the Celery module isn't going to
# be the most flexible approach to building Celery tasks.
# we may want to integrate tasks or indicate the fact
# that we want to start tasks inside our apps, views, models, etc.
# we want a more flexible approach, so in addition to
# creating tasks with "app.task", we also have "shared_tasks"
@app.task
def add():
    return


# Better Approach to create and Register tasks
# we are now informing Celery to look in all the other apps "INSTALLED_APPS"
# and look for a file named "tasks.py"
app.autodiscover_tasks()
