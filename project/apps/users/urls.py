from django.conf.urls import patterns, url
from django.contrib.auth import views

urlpatterns = patterns(
    u'',
    url(r'^login/$', views.login, name=u'login'),
    url(r'^logout/$', views.logout, {u'next_page': u'/'}, name=u'logout'),

)
