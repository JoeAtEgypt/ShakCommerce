from .celery import app as celery_app

"""
This is the Django instance so whenever we start the Django project, this initialization file will be read, 
we will initialize access to our Celery app. 
So Whenever we try to run any tasks for example in another modules, it will now be able to find Celery in the background
and be able to then perform the task of sending the task to the Message Broker
"""
__all__ = ("celery_app",)
