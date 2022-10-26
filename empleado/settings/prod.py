import os
from .base import *
from pathlib import Path



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER' : 'juanpablo',
        'PASSWORD' : 'admin',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

STATIC_URL = 'static/'
#STATICFILES_DIRS = ['static/css']
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'