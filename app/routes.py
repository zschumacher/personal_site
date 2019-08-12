from app import app, render_template, Constants


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html', constants=Constants, enumerate=enumerate, isinstance=isinstance, str=str, list=list, tuple=tuple,
        len=len
    )
