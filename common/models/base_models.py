import uuid
from enum import unique

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.__str__()
