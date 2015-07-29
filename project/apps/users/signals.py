# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from blogs.models import Blog


@receiver(post_save, sender=User)
def create_user_blog(instance, created, *args, **kwargs):
    if created:
        Blog.objects.create(user=instance, title=u'{}\'s blog'.format(instance.username))
