# Settings for production server

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Directory where settings.py lives
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..')) # Django project root

from production_database import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': production_name,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': production_user,
        'PASSWORD': production_password, # Entered via fab command; leave blank if using SQLite
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['*']
MEDIA_ROOT = '/var/sites/virtualenvs/testproject/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/sites/virtualenvs/testproject/static/'
STATIC_URL = '/static/'

