import json
import sys

from flask import Flask, render_template
from flask_flatpages import pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG

app = Flask(__name__)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def index():
    with open('settings.json', encoding='utf8') as config:
        data = config.read()
        settings = json.loads(data)
    return render_template('index.html', bigheader=True, **settings)


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', port=8000, debug=True)
