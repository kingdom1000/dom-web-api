import os, sys

PROJECT_DIR = '/var/www/dom-web-api'
VENV_DIR = '/home/ubuntu/venv/bin'

activate_this = os.path.join(VENV_DIR, 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from api import app as application