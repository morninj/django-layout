This is a reusable Django project template. It uses:

* Ubuntu 12.04 LTS
* Python 2.7.3
* Django 1.5
* NGINX
* Green Unicorn
* MySQL
<!-- TODO add versions -->

# Project Settings

By default, Django projects use a single settings file. This is fine for 
development environments, but in production you'll want different settings 
(for instance, to set `Debug = False`).

This template divides the project settings into three files:

* `default.py`: project-wide defaults (e.g., `INSTALLED_APPS`).
* `development.py`: development settings (e.g., `Debug = True`).
* `production.py`: production settings (e.g., settings for a database server).

The instructions below explain how to configure your development and 
production environments to load the right settings files.

# Development

These instructions assume your project is called `project_name`. You can call 
it whatever you want, but be sure to replace `project_name` with your 
project's name.

## Configure Virtualenv

<!-- TODO install virtualenv and virtualenvwrapper -->

    $ django-admin.py startproject --template=https://github.com/morninj/django-layout/archive/master.zip project_name
<!-- TODO expand-->

## Configure Development Settings

    $ cd project_name/project_name
    $ cp settings.py.sample settings.py

By default, `.gitignore` excludes `settings.py` from the repository. 
This keeps the settings file from getting clobbered when you sync the 
code across servers.

# Staging

<!-- TODO -->

# Production

<!-- TODO -->

# Credits

[Joseph Mornin](http://www.mornin.org/) is the main author.

This project builds on parts of [Lincoln Loop's 
django-layout](https://github.com/lincolnloop/django-layout).

<!-- TODO: pokayoke and 12-factor -->
<!-- TODO: add south -->
