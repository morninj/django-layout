Development
===========

These instructions assume your project is called ``project_name``. You
can call it whatever you want, but be sure to replace ``project_name``
with your project's name.

Configure Virtualenv
--------------------

The project should live inside a virtual environment. Virtualenvs help
keep projects clean and portable.

First, install and configure
`virtualenv <https://pypi.python.org/pypi/virtualenv>`__ and
`virtualenvwrapper <https://bitbucket.org/dhellmann/virtualenvwrapper/>`__.

Next, configure your local virtualenv:

::

    $ mkvirtualenv -p python2.7 project_name
    $ cd /path/to/virtualenvs/project_name

Create New Django Project
-------------------------

Make sure you're in directory and that the virtualenv is activated.

First, install Django 1.5.1:

::

    $ pip install Django==1.5.1

Next, create a new Django project based on the ``django-layout`` template 
(replacing ``project_name`` with the name of your project):

::

    $ django-admin.py startproject --template=https://github.com/morninj/django-layout/archive/master.zip --extension=py,sh,conf project_name

To keep your virtualenv organized, rename the project directory as
``src``:

::

    $ mv project_name src
    $ cd src

Install dependencies:

::

    $ pip install -r requirements.txt

Initialize Repository
---------------------

The contents of ``src`` should be under version control. For Git, run:

::

    $ git init
    $ git add * .gitignore
    $ git commit -m "Create new Django project"

To store your code on GitHub, create a new GitHub repository and then
run:

::

    $ git remote add origin git@github.com:your_username/repo_name.git
    $ git push -u origin master

This is also the spot to add a ``README``.

Configure Settings
------------------

Go to the settings folder:

::

    $ cd project_name/project_name

Project-wide settings live in ``default.py``. Edit that file to match your 
configuration. The defaults should be fine for most configurations.

Development settings live in ``development.py``. The defaults should work for most development environments.

Next, activate the development settings:

::

    $ cp settings.sample.py settings.py

Create the local database:

::

    $ cd ..
    $ python manage.py syncdb

Run the development server:

::

    $ python manage.py runserver

Your project should now be available at ``http://127.0.0.1:8000/``.

Development Workflow
--------------------

::

    $ cd /path/to/virtualenv/
    $ workon project_name
    $ cd src/project_name
    $ git pull origin master # Pull changes
    $ python manage.py runserver
    ... # Make changes
    $ git commit -am "Description of changes"
    $ git push origin master

When adding an app, create the initial schema migration with South:

::

    $ python manage.py app_name --initial

When updating an app's models, use South to migrate the database schema:

::

    $ python manage.py schemamigration app_name --auto
    $ python manage.py migrate app_name
