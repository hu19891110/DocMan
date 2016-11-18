#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

monitorAction = Blueprint('monitorAction', __name__, template_folder='templates/')


@monitorAction.route("/monitor/index.html", methods=['GET', 'POST'])
def monitor_index():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("monitor/index.html", uUserName=uUserName)
    return redirect("/")
