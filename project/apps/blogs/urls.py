from django.conf.urls import patterns, url

from .views import UserFeedView, BlogListView, BlogDetailView, BlogSubscribeView, PostDetailView, \
    PostCreateView, PostMarkAsReadView

urlpatterns = patterns(
    u'blogs.views',

    url(r'^$', UserFeedView.as_view(), name=u'feed'),
    url(r'^blogs/$', BlogListView.as_view(), name=u'list'),
    url(r'^blogs/(?P<pk>\d+)/$', BlogDetailView.as_view(), name=u'detail'),
    url(r'^blogs/(?P<pk>\d+)/subscription/$', BlogSubscribeView.as_view(), name=u'subscribe'),

    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name=u'post-detail'),
    url(r'^posts/(?P<pk>\d+)/done/$', PostMarkAsReadView.as_view(), name=u'post-mark-as-read'),
    url(r'^posts/new/$', PostCreateView.as_view(), name=u'post-create'),
)
