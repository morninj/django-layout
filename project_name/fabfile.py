from fabric.api import *
from contextlib import contextmanager as _contextmanager

# Edit these variables for your staging and production configuration

# Example: user@host:port -- e.g., ubuntu@nothing.com:22
# Make sure the user has root privileges
USER = ''
STAGING_SERVER = USER + '@host.com'
PRODUCTION_SERVER = USER + ''

# Absolute path to your private key file if needed; otherwise leave blank
PRIVATE_KEY_FILE = ''
env.key_filename = PRIVATE_KEY_FILE

# Path to store virtualenvs
VIRTUALENV_ROOT = '/var/sites/virtualenvs/'

# Read-only repository connection (for staging and production servers)
# Example: git://github.com/username/repo-name.git
REPOSITORY_READ_ONLY = ''

# Project name (should match your Django project name)
PROJECT_NAME = '{{ project_name }}'

@_contextmanager
def virtualenv():
    with cd(VIRTUALENV_ROOT + PROJECT_NAME):
        with prefix('source ' + VIRTUALENV_ROOT + PROJECT_NAME + \
            '/bin/activate'):
            yield

@hosts(STAGING_SERVER)
def configure_staging_server():
    run('sudo apt-get update -y')
    run('sudo apt-get install git nginx python-setuptools python-dev -y')
    run('sudo easy_install pip')
    run('sudo pip install virtualenv virtualenvwrapper')
    run('echo "WORKON_HOME=' + VIRTUALENV_ROOT + '" >> ~/.bash_profile')
    run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ' \
        '~/.bash_profile')
    run('sudo mkdir -p ' + VIRTUALENV_ROOT)
    run('sudo chown ' + USER + ' ' + VIRTUALENV_ROOT)
    run('source ~/.bash_profile')
    run('mkvirtualenv ' + PROJECT_NAME)
    with virtualenv():
        with cd(VIRTUALENV_ROOT + PROJECT_NAME):
            run('mkdir static')
            run('mkdir media')
            run('mkdir logs')
            run('git clone ' + REPOSITORY_READ_ONLY + ' ' + VIRTUALENV_ROOT + 
                PROJECT_NAME + '/src')
        with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src'):
            run('pip install -r requirements.txt')

