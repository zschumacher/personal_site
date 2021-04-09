from app import app
from flask import render_template
from app.constants import Constants


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html', constants=Constants, enumerate=enumerate, isinstance=isinstance, str=str, list=list, tuple=tuple,
        len=len
    )
