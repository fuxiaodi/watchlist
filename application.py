from flask import Flask

app = Flask(__name__)

from markupsafe import escape
from flask import url_for
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()