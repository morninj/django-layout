# Settings for development server

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Directory where settings.py lives
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..')) # Django project root

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'local.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []
MEDIA_ROOT = '/var/tmp/'
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
