Introduction
============

This is a reusable Django project template. These instructions explain
how to configure development, staging, and production environments.

This setup uses:

- `Ubuntu Server 12.04.03 LTS 64-bit 
  <http://www.ubuntu.com/download/server>`__
- `Python 2.7.3 <http://www.python.org/download/releases/2.7.3/>`__
- `Django
  1.6.1 <https://docs.djangoproject.com/en/dev/releases/1.6/>`__

See ``requirements.txt`` for other dependencies. You can modify this setup, 
but I haven't tested other configurations.

Project Settings
----------------

By default, Django projects use a single settings file. This is fine for
development environments, but in production you'll want different
settings (for instance, to set ``Debug = False``).

In this configuration, project-wide settings live in ``default.py`` and 
settings for specific enviroments (development, staging, and production) live 
in ``development.py`` and ``production.py``. The instructions below explain 
how to configure settings for each environment.
