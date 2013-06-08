from fabric.api import *
from contextlib import contextmanager as _contextmanager
from conf.production import *

env.key_filename = PRIVATE_KEY_FILE
STAGING_SERVER = USER + '@' + STAGING_SERVER_HOST
PRODUCTION_SERVER = USER + '@' + PRODUCTION_SERVER_HOST

@hosts(STAGING_SERVER)
def configure_staging_server():
    sudo('apt-get update -y')
    sudo('apt-get install git nginx python-setuptools python-dev -y')
    # TODO: move package list to production_config.py
    sudo('easy_install pip')
    sudo('sudo pip install virtualenv virtualenvwrapper')
    run('echo "WORKON_HOME=' + VIRTUALENV_ROOT + '" >> ~/.bash_profile')
    run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ' \
        '~/.bash_profile')
    sudo('mkdir -p ' + VIRTUALENV_ROOT)
    sudo('chown ' + USER + ' ' + VIRTUALENV_ROOT)
    with prefix('WORKON_HOME=' + VIRTUALENV_ROOT):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            sudo('mkvirtualenv ' + PROJECT_NAME)
            with prefix('workon ' + PROJECT_NAME): 
                with cd(VIRTUALENV_ROOT + PROJECT_NAME):
                    sudo('mkdir static')
                    sudo('mkdir media')
                    sudo('mkdir logs')
                    sudo('git clone ' + REPOSITORY_READ_ONLY + ' ' + VIRTUALENV_ROOT + PROJECT_NAME + '/src')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src'):
                    sudo('pip install -r requirements.txt')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' \
                    + PROJECT_NAME + '/' + PROJECT_NAME + '/'):
                    sudo('echo "from default import *" >> settings.py')
                    sudo('echo "from production import *" >> settings.py')

