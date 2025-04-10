from django.db import models
from django.utils.text import slugify


class SlugModelMixin(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)

    slug_attr_name = "name"

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(getattr(self, self.slug_attr_name))
        super().save(*args, **kwargs)
