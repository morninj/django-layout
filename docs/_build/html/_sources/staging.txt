Staging
=======

First, commit all local changes to the repository.

Next, launch a new staging server. On Amazon Web Services, for instance, 
launch a new EC2 instance. Remember that this configuration uses Ubuntu 12.04 
LTS 64-bit (though other Debian-based Linux distributions should work fine).

Add Staging Settings
--------------------

::

    $ cd /path/to/virtualenvs/project_name/src/project_name

Edit the following variables in ``fabfile.py`` to match your deployment 
server:

-  ``USER``
-  ``STAGING_SERVER``
-  ``PRIVATE_KEY_FILE``
-  ``VIRTUALENV_ROOT``
-  ``REPOSITORY_READ_ONLY``


Configure Staging Server
------------------------

Configure the server with Fabric:

::

    $ cd /path/to/virtualenvs/project_name/src/project_name
    $ fab configure_staging_server

Connect to the server via SSH, create ``config.env``, and update it with your 
deployment settings:

::

    $ cd /path/to/virtualenvs/ # default: /var/sites/virtualenvs/
    $ cd project_name/src/
    $ cp config.env.sample config.env
    $ vim config.env # make any necessary changes


