from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

from blogs.managers import PostQuerySet
from main.models import BaseModel


class Blog(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name=u'subscribed_blogs', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(u'blogs:detail', args=(self.pk,))


class Post(BaseModel):
    blog = models.ForeignKey(u'blogs.Blog', related_name=u'posts')

    title = models.CharField(max_length=255)
    text = models.TextField()

    objects = PostQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    @property
    def user(self):
        return self.blog.user.username

    def get_absolute_url(self):
        return reverse(u'blogs:post-detail', args=(self.pk,))


class PostReadMark(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=u'post_read_marks')
    post = models.ForeignKey(u'blogs.Post', related_name=u'post_read_marks')
    is_read = models.BooleanField(default=True)

    class Meta:
        unique_together = (u'user', u'post')

    def __unicode__(self):
        return u'{} read {}'.format(self.user, self.post)


from .signals import *
