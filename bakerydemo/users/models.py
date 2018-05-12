from django.contrib.auth.models import AbstractUser
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel


class User(AbstractUser):
    country = models.CharField(verbose_name='country', max_length=255)

    panels = [
        FieldPanel('first_name'),
    ]
