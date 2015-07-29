import os


class LocaleSettings(object):
    TIME_ZONE = os.getenv(u'TZ', u'Europe/Moscow')

    LANGUAGE_CODE = u'ru-RU'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
