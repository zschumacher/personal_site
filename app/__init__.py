from flask import Flask

app = Flask(__name__)
app.config["FREEZER_RELATIVE_URLS"] = True
from app import routes
