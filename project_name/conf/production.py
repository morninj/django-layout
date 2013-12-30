# Edit these variables for your staging and production configuration
# Make sure these values also appear in ALLOWED_HOSTS[] in 
# project_name/production.py and that you have pushed 
# project_name/production.py to the repo BEFORE running fab
STAGING_SERVER_HOST = '' # E.g., staging.yoursite.com
PRODUCTION_SERVER_HOST = '' # E.g., www.yoursite.com

# Credentials for the server administrator
ROOT_USER = '' # E.g., ubuntu
ROOT_USE_PASSWORD = False # False: use private key; True: use password
ROOT_PASSWORD = ''
ROOT_PRIVATE_KEY = '' # Local path to the root user's private key--e.g., ~/.aws/yourname.pem

# Credentials for the user who will be interacting with the server
# For security, this user will only be able to access the server using a SSH 
# key (see https://en.wikipedia.org/wiki/Secure_Shell#Key_management)
# This script will create the user on the server and upload your public key
ADD_NEW_USER = True
USER_PUBLIC_KEY = '' # Local path to your public key--e.g., ~/.ssh/id_dsa.pub
USER = '' # Make sure the user has root privileges

# Version control repository connection
# E.g., git://github.com/username/repo-name.git
# Must be public or accessible with a username/password; public key 
# authentication is not currently supported
REPOSITORY = ''

# Path to store virtualenvs; best to leave this as the default
VIRTUALENV_ROOT = '/var/sites/virtualenvs/'

# Project name (auto-generated; should match your Django project name)
PROJECT_NAME = '{{ project_name }}'

# Install security tools?
SECURITY_TOOLS = True

# Firewall configuration: allow traffic on these ports
ALLOWED_PORTS = ['22', '80', '443', '8000']
# TODO separate firewall for production

# Enable automatic security updates?
ENABLE_AUTOMATIC_SECURITY_UPDATES = True
