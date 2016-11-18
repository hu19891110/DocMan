#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

logAction = Blueprint('logAction', __name__, template_folder='templates/')


@logAction.route("/log/index.html", methods=['GET', 'POST'])
def log_index():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("log/index.html", uUserName=uUserName)
    return redirect("/")
