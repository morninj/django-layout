Staging
=======

First, commit all local changes to the repository.

Next, launch a new staging server. On Amazon Web Services, for instance, 
launch a new EC2 instance. Remember that this configuration uses Ubuntu Server 
12.04 LTS 64-bit (though other Debian-based Linux distributions should work 
fine).

The staging server will be almost identical to the production server. Most of 
the settings below will also apply in production.

Edit Configuration Settings
---------------------------

Change to the settings directory:

::

    $ cd /path/to/virtualenvs/project_name/src/project_name/project_name

Edit the settings in ``production.py`` to match the settings for your staging 
server.

Next, change to the ``conf`` directory:

::

    $ cd ../conf

Edit the following files and make sure the values are correct:

-  ``production.py``: production deployment configuration
-  ``nginx.conf``: nginx virtual host configuration
-  ``launch.sh``: a shell script to launch the Gunicorn server
- ``project_name.conf``: an Upstart configuration to launch Gunicorn on boot

Configure Staging Server
------------------------

Once you've specified the settings above, Fabric will automatically configure 
the server environment. To configure the staging server, run:

::

    $ cd .. # you should now be in the same directory as fabfile.py
    $ fab configure_staging_server

Fabric will show the output of each command. You may be prompted for passwords 
(e.g., to log into the server or to clone the repository).
