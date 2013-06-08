# Edit these variables for your staging and production configuration

USER = '' # Make sure the user has root privileges
STAGING_SERVER_HOST = '' # E.g., staging.yoursite.com
PRODUCTION_SERVER_HOST = '' # E.g., www.yoursite.com

# Absolute path to your private key file if needed; otherwise leave blank
PRIVATE_KEY_FILE = '' # e.g., /path/to/key.pem

# Version control repository connection
# E.g., git://github.com/username/repo-name.git
# Must be public or accessible with a username/password; public key 
# authentication is not currently supported
REPOSITORY = ''

# Path to store virtualenvs; best to leave this as the default
VIRTUALENV_ROOT = '/var/sites/virtualenvs/'

# Project name (auto-generated; should match your Django project name)
PROJECT_NAME = '{{ project_name }}'
