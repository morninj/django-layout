Introduction
============

This is a reusable Django project template. These instructions explain
how to configure development, staging, and production environments.

Dependencies
------------

This configuration uses these tools:

-  `Ubuntu 12.04 LTS 64-bit
   Server <http://www.ubuntu.com/download/server>`__
-  `Python 2.7.3 <http://www.python.org/download/releases/2.7.3/>`__
-  `Django
   1.5.1 <https://docs.djangoproject.com/en/dev/releases/1.5/>`__
-  `virtualenv 1.9.1 <https://pypi.python.org/pypi/virtualenv>`__
-  `virtualenvwrapper
   4.0 <https://bitbucket.org/dhellmann/virtualenvwrapper/>`__
-  `nginx 1.4.1 <http://nginx.org/en/download.html>`__
-  `Gunicorn 0.17.4 <https://pypi.python.org/pypi/gunicorn/>`__
-  `MySQL 5.6.11 <http://dev.mysql.com/downloads/mysql/>`__
- `Fabric 1.6.1 <http://docs.fabfile.org/en/1.6/>`__

You can modify this setup, but I haven't tested other configurations.

Project Settings
----------------

By default, Django projects use a single settings file. This is fine for
development environments, but in production you'll want different
settings (for instance, to set ``Debug = False``).

In this configuration, project-wide settings live in ``settings.py`` and 
settings for specific enviroments (development, staging, and production) live 
in ``config.env``. The instructions below explain how to configure settings 
for each environment.
