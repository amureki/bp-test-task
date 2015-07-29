from django.template import Library

from blogs.models import PostReadMark

register = Library()


@register.filter
def read_post(user, post):
    try:
        post_read_mark = PostReadMark.objects.get(user=user, post=post)
        return post_read_mark.is_read
    except PostReadMark.DoesNotExist:
        return False
