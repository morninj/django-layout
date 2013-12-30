from fabric.api import *
from contextlib import contextmanager as _contextmanager
from conf.production import *

env.key_filename = PRIVATE_KEY_FILE
STAGING_SERVER = USER + '@' + STAGING_SERVER_HOST
PRODUCTION_SERVER = USER + '@' + PRODUCTION_SERVER_HOST

@hosts(STAGING_SERVER)
def configure_staging_server():
    configure_server('staging')

@hosts(PRODUCTION_SERVER)
def configure_production_server():
    pass
    # TODO configure_server('production')

def configure_server(deploy):
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get install git nginx python-setuptools python-dev -y')
    # TODO: move package list to production_config.py
    # TODO add user
    # TODO add security tools
    sudo('easy_install pip')
    sudo('sudo pip install virtualenv virtualenvwrapper')
    run('echo "WORKON_HOME=' + VIRTUALENV_ROOT + '" >> ~/.bash_profile')
    run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ' \
        '~/.bash_profile')
    sudo('mkdir -p ' + VIRTUALENV_ROOT)
    with prefix('WORKON_HOME=' + VIRTUALENV_ROOT):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            sudo('mkvirtualenv ' + PROJECT_NAME)
            with prefix('workon ' + PROJECT_NAME): 
                with cd(VIRTUALENV_ROOT + PROJECT_NAME):
                    # Add directories for static, media, logs
                    sudo('mkdir static')
                    sudo('mkdir media')
                    sudo('mkdir logs')
                    # Clone repository
                    sudo('git clone ' + REPOSITORY + ' ' + VIRTUALENV_ROOT + PROJECT_NAME + '/src')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src'):
                    # Install pip requirements
                    sudo('pip install -r requirements.txt')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' \
                    + PROJECT_NAME + '/' + PROJECT_NAME + '/'):
                    # Enable production settings
                    sudo('echo "from default import *" >> settings.py')
                    sudo('echo "from production import *" >> settings.py')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + \
                    PROJECT_NAME + '/conf/'):
                    # Set permissions on the launch shell script
                    sudo('chmod ug+x launch.sh')
                    # Enable nginx conf
                    if deploy is 'staging':
                        sudo('ln -s ' + VIRTUALENV_ROOT + PROJECT_NAME \
                        + '/src/' + PROJECT_NAME + \
                        '/conf/nginx.staging.conf ' + \
                        '/etc/nginx/sites-enabled/' + PROJECT_NAME + '.conf')
                    else:
                        sudo('ln -s ' + VIRTUALENV_ROOT + PROJECT_NAME + \
                        '/src/' + PROJECT_NAME + \
                        '/conf/nginx.production.conf ' \
                        + '/etc/nginx/sites-enabled/' + PROJECT_NAME + '.conf')
                    # Enable Upstart service
                    sudo('cp ' + VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + 
                    PROJECT_NAME + '/conf/livesite.conf ' + \
                    '/etc/init/livesite.conf')
                    sudo('ln -s /lib/init/upstart-job /etc/init.d/livesite')
                    sudo('service livesite start')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + \
                    PROJECT_NAME):
                    # Collect static files
                    sudo('../../bin/python2.* manage.py collectstatic')
                # Set ownership permissions
                sudo('chown ' + USER + ' ' + VIRTUALENV_ROOT + PROJECT_NAME + ' -R')
                # Syncdb and apply migrations
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + PROJECT_NAME):
                    with prefix('workon ' + PROJECT_NAME): 
                        run('python manage.py syncdb')
                        run('python manage.py migrate')
                # FIXME add USER to production.py
                sudo('service nginx restart')

@hosts(STAGING_SERVER)
def deploy_staging():
    deploy('staging')

@hosts(PRODUCTION_SERVER)
def deploy_production():
    pass
    # TODO deploy('staging')

def deploy(deploy):
    if deploy is 'staging':
        with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src'):
            sudo('git pull origin master')
            with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + PROJECT_NAME):
                with prefix('workon ' + PROJECT_NAME): 
                    run('python manage.py syncdb')
                    run('python manage.py migrate')
                    run('python manage.py collectstatic')
            sudo('service livesite restart')
            sudo('service nginx restart')

