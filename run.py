#!/usr/bin/env python
# encoding:utf-8
from flask import Flask, render_template

from views.loginAction import loginAction
from views.homeAction import homeAction
from views.dockerAction import dockerAction
from views.feedbackAction import feedbackAction
from views.imagesAction import imagesAction
from views.logAction import logAction
from views.monitorAction import monitorAction

app = Flask(__name__)
app.secret_key = '\x81,j\xd5\xdc:8\xcdi\xc8\xbd\xe8\x9ex\xb6\x8f\xfcG\xcc:"\x97S\x1f'

app.register_blueprint(loginAction)
app.register_blueprint(homeAction)
app.register_blueprint(dockerAction)
app.register_blueprint(feedbackAction)
app.register_blueprint(imagesAction)
app.register_blueprint(logAction)
app.register_blueprint(monitorAction)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=8088, host='0.0.0.0')
