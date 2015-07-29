# -*- coding:utf-8 -*-
import sys
import os
from configurations import Settings

from config.django.database import DevelopmentDatabaseSettings, StagingDatabaseSettings
from config.django.i18n import LocaleSettings
from config.django.media import MediaSettings, StagingMediaSettings
from config.django.middleware import MiddlewareSetings
from config.django.logging import LoggingSettings
from config.django.template import TemplateSettings
from config.django.email import EmailSettings


class BaseSettings(LocaleSettings, MiddlewareSetings, LoggingSettings, TemplateSettings, EmailSettings,
                   Settings):
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    ADMINS = MANAGERS = []

    ALLOWED_HOSTS = [u'', ]

    SITE_ID = 1

    SECRET_KEY = u'n_uhb^=bmab9i)(rda6fn-m33!c9i%rb(d*o5!5vk)nsrw=6e+'

    ROOT_URLCONF = 'project.urls'

    WSGI_APPLICATION = 'project.wsgi.application'

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',

        'gunicorn',
        'raven.contrib.django.raven_compat',
        'django',

        'blogs',
        'users',
    )

    LOGIN_URL = u'/users/login/'
    LOGIN_REDIRECT_URL = u'/'
    LOGOUT_URL = u'/users/logout/'




class Development(DevelopmentDatabaseSettings, MediaSettings, BaseSettings):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


class Staging(StagingDatabaseSettings, StagingMediaSettings, BaseSettings):
    RAVEN_CONFIG = {
        u'dsn': u'',
    }
