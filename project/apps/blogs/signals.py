# -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from blogs.models import Post


@receiver(post_save, sender=Post)
def notify_subscribers(instance, created, *args, **kwargs):
    if not created:
        return
    user = instance.blog.user
    subscribers_emails = instance.blog.subscribers.exclude(
        Q(email__isnull=True) | Q(id=user.id)).values_list(u'email', flat=True)

    site = Site.objects.get_current()
    post_url = u'http://{}{}'.format(site, instance.get_absolute_url())

    subject = u'New post on {}'.format(site.name)

    text_content = u'Hey, check new post at {}: {}'.format(site.name, post_url)
    html_content = u'<p>Hey, check new post by {0}:<br/> <a href="{1}">{1}</a></p>'.format(user, post_url)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_SENDER, to=[], bcc=subscribers_emails)
    msg.attach_alternative(html_content, u'text/html')
    msg.send()
