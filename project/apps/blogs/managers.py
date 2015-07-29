from django.db import models


class PostQuerySet(models.QuerySet):
    def for_user(self, user):
        blog_ids = user.subscribed_blogs.all().values_list(u'id', flat=True)
        return self.filter(blog_id__in=blog_ids)
