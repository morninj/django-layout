This is a reusable Django project template. It uses:

* [Ubuntu 12.04 LTS 64-bit Server](http://www.ubuntu.com/download/server)
* [Python 2.7.3](http://www.python.org/download/releases/2.7.3/)
* [Django 1.5](https://docs.djangoproject.com/en/dev/releases/1.5/)
* [virtualenv 1.9.1](https://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper 4.0](https://bitbucket.org/dhellmann/virtualenvwrapper/)
* [nginx 1.4.1](http://nginx.org/en/download.html)
* [Gunicorn 0.17.4](https://pypi.python.org/pypi/gunicorn/)
* [MySQL 5.6.11](http://dev.mysql.com/downloads/mysql/)

These instructions explain how to configure development, staging, and 
production environments.

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

The project should live inside a virtual environment. Virtualenvs help keep 
projects clean and portable.

First, install and configure 
[virtualenv](https://pypi.python.org/pypi/virtualenv) and 
[virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper/).

Next, configure your local virtualenv:

    $ mkvirtualenv project_name
    $ cd /path/to/virtualenvs/project_name
    $ mkdir src
    $ cd src

## Initialize Repository

The contents of `src` should be under version control. For Git, run:

    $ git init

To store your code on GitHub, create a new GitHub repository and then run:

    $ git remote add origin git@github.com:your_username/repo_name.git
    $ git push -u origin master

This is also a good place to add a `README`.

## Create New Django Project

    $ django-admin.py startproject --template=https://github.com/morninj/django-layout/archive/master.zip project_name
<!-- TODO expand-->

## Configure Development Settings

    $ cd project_name/project_name
    $ cp settings.py.sample settings.py

You should exclude `settings.py` from the repository to avoid clobbering it 
when you sync the code across servers. To do this, add `.gitignore` in your 
project's root directory (i.e., `src/`) with this line:

    settings.py

## Development Workflow

    $ cd /path/to/virtualenv/
    $ workon project_name
    $ cd src/project_name
    $ git pull origin master # Pull changes
    $ python manage.py runserver
    ... # Make changes
    $ git commit -am "Description of changes"
    $ git push origin master
<!-- TODO fab? -->

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
