#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

homeAction = Blueprint('homeAction', __name__, template_folder='templates/')


@homeAction.route("/home.html", methods=['GET', 'POST'])
def home():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("home/index.html", uUserName=uUserName)
    return redirect("/")
