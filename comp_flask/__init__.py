from flask import Flask


comp_app = Flask(__name__)

from . import routes
