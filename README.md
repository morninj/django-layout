This is a reusable Django project template.

# Project Settings

By default, Django projects use a single settings file. This is fine for 
development environments, but in production you'll want different settings 
(for instance, to set `Debug = False`).

This template divides the project settings into three files:

* `global.py`: project-wide defaults (e.g., `INSTALLED_APPS`).
* `development.py`: development settings (e.g., `Debug = True`).
* `production.py`: production settings (e.g., settings for a database server 
  instead of SQLite).

The instructions below explain how to configure your development and 
production environments to load the right settings files.

# Development

    $ django-admin.py startproject --template=https://github.com/morninj/django-layout/archive/master.zip {PROJECT_NAME}
<!-- TODO -->

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
