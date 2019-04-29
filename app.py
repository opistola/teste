import os
from api import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app(basedir+"/tests/config.py")