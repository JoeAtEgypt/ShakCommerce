from django.db import models
from django.utils.text import slugify


class SlugModelMixin(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    slug_attr_name = "name"

    class Meta:
        abstract = True

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.slug = slugify(getattr(self, self.slug_attr_name))
        super().save(force_insert, force_update, using, update_fields)
