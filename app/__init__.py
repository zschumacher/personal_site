from flask import Flask, url_for, render_template
from .constants import Constants

app = Flask(__name__)

from app import routes
