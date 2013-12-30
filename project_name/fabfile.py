from fabric.api import *
from contextlib import contextmanager as _contextmanager
from conf.production import *

# Configure server admin login credentials
if ROOT_USE_PASSWORD:
    env.password = ROOT_PASSWORD
else:
    env.key_filename = ROOT_PRIVATE_KEY

@hosts(ROOT_USER + '@' + STAGING_SERVER_HOST)
def configure_staging():
    configure_server('staging')

@hosts(ROOT_USER + '@' + PRODUCTION_SERVER_HOST)
def configure_production():
    pass
    # TODO configure_server('production')

def configure_server(deploy):
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get install ' + APT_PACKAGES + ' -y')
    if NGINX: install_nginx()
    if ADD_NEW_USER: add_new_user()
    if SECURITY_TOOLS: install_security_tools()
    sudo('easy_install pip')
    sudo('sudo pip install virtualenv virtualenvwrapper')
    # Configure virtualenvwrapper for server admin
    run('echo "WORKON_HOME=' + VIRTUALENV_ROOT + '" >> ~/.bash_profile')
    run('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ' \
        '~/.bash_profile')
    # Also configure virtualenvwrapper for main user
    sudo('echo "WORKON_HOME=' + VIRTUALENV_ROOT + '" >> /home/' + USER + '/.bash_profile')
    sudo('echo "source /usr/local/bin/virtualenvwrapper.sh" >> ' \
        '/home/' + USER + '/.bash_profile')
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
                    # TODO instead of keeping the live database password in 
                    # production.py, prompt for it here and then replace it in 
                    # the file; see fab prompt() and fab sed(); more:
                    # http://docs.fabfile.org/en/1.4.0/api/contrib/files.html
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
                # Syncdb and apply migrations
                sudo('chown ' + ROOT_USER + ' ' + VIRTUALENV_ROOT + PROJECT_NAME + ' -R')
                with cd(VIRTUALENV_ROOT + PROJECT_NAME + '/src/' + PROJECT_NAME):
                    with prefix('workon ' + PROJECT_NAME): 
                        run('python manage.py syncdb')
                        run('python manage.py migrate')
    # Set ownership permissions
    # Later interactions with the server will take place via the account of 
    # the main user, *not* the server admin (ROOT_USER)
    sudo('chown ' + USER + ' ' + VIRTUALENV_ROOT + PROJECT_NAME + ' -R')
    sudo('service nginx restart')
    # TODO reboot system?

@hosts(USER + '@' + STAGING_SERVER_HOST)
def deploy_staging():
    deploy('staging')

@hosts(USER + '@' + PRODUCTION_SERVER_HOST)
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

def add_new_user():
    sudo('adduser ' + USER)
    sudo('adduser %s sudo' % USER)
    # Upload user's private key
    put(USER_PUBLIC_KEY, '/var/tmp/public_key')
    sudo('mkdir /home/%s/.ssh/' % USER)
    sudo('cat /var/tmp/public_key >> /home/%s/.ssh/authorized_keys' % \
        USER)
    sudo('rm /var/tmp/public_key')
    sudo('chmod 700 /home/%s/.ssh' % USER)
    sudo('chmod 400 /home/%s/.ssh/authorized_keys' % USER)
    sudo('chown {0}:{0} /home/{0} -R'.format(USER))

def install_security_tools():
    # Install fail2ban to block suspicious activity
    sudo('apt-get install -y fail2ban')
    # Only allow SSH key access
    sudo('echo "PasswordAuthentication no" >> /etc/ssh/sshd_config')
    # Prevent root login
    sudo('echo "PermitRootLogin no" >> /etc/ssh/sshd_config')
    # Configure firewall
    for port in ALLOWED_PORTS:
        sudo('ufw allow ' + port)
    sudo('ufw enable')
    # TODO sudo('ufw enable -y') ?
    # Enable automatic security updates
    if ENABLE_AUTOMATIC_SECURITY_UPDATES:
        sudo('apt-get install unattended-upgrades -y')
        sudo('echo \'APT::Periodic::Update-Package-Lists "1";\' > /etc/apt/apt.conf.d/10periodic')
        sudo('echo \'APT::Periodic::Download-Upgradeable-Packages "1";\' >> /etc/apt/apt.conf.d/10periodic')
        sudo('echo \'APT::Periodic::AutocleanInterval "7";\' >> /etc/apt/apt.conf.d/10periodic')
        sudo('echo \'APT::Periodic::Unattended-Upgrade "1";\' >> /etc/apt/apt.conf.d/10periodic')

def install_nginx():
    sudo('apt-get install -y nginx')
    sudo('update-rc.d nginx defaults') # Start nginx on boot

