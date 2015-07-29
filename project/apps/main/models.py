# coding: utf-8
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = (u'-date_created',)
