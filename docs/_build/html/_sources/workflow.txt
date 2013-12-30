Workflow
========

Development
-----------

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

Staging
-------

::

    $ fab deploy_staging

Production
----------

TODO
