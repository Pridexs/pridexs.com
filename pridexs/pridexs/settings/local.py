from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pridexsdotcom',
        'USER': 'pridexs',
        'PASSWORD': 'abacate22',
        'HOST': 'localhost',
        'PORT': '',
    }
}
