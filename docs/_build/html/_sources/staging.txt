Staging Configuration
=====================

First, commit all local changes to the repository.

Next, launch a new staging server. On Amazon Web Services, for instance, 
launch a new EC2 instance. Remember that this configuration uses Ubuntu Server 
12.04.03 LTS 64-bit (though other Debian-based Linux distributions should work 
fine).

The staging server will be almost identical to the production server. Most of 
the settings below will also apply in production.

Edit Configuration Settings
---------------------------

Change to the settings directory:

::

    $ cd /path/to/virtualenvs/project_name/src/project_name/project_name

Edit the settings in ``production.py`` to match the settings for your staging 
server. For instance, you may want to add credentials for a database server. 
Also, don't forget to add your staging and production domains to 
``ALLOWED_HOSTS``--e.g.:

::

    ALLOWED_HOSTS = ['staging.example.com', 'www.example.com']

Next, change to the ``conf`` directory:

::

    $ cd ../conf

Edit the following files and make sure the values are correct:

-  ``production.py``: production deployment configuration
-  ``nginx.staging.conf``: nginx virtual host configuration
-  ``launch.sh``: a shell script to launch the Gunicorn server
-  ``livesite.conf``: an Upstart configuration to launch Gunicorn on boot

Commit your changes and push them to the repository.

Configure Staging Server
------------------------

Once you've specified the settings above, Fabric will automatically configure 
the server environment. To configure the staging server, run:

::

    $ cd .. # you should now be in the same directory as fabfile.py
    $ fab configure_staging

Fabric will show the output of each command. You may be prompted for passwords 
(e.g., to log into the server or to clone the repository).

Verify
------

Navigate to the staging server address. You should see ``Hello, world!``

If you see "Bad Request (400)", it's probably because ``ALLOWED_HOSTS`` is set
incorrectly. Make sure your domain is in ``ALLOWED_HOSTS`` in
``src/project_name/project_name/production.py``.
