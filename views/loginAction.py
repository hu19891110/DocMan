#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, request, redirect, session

loginAction = Blueprint('loginAction', __name__, template_folder='templates/')


@loginAction.route("/", methods=['GET', 'POST'])
@loginAction.route("/index.html", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template("index.html")


@loginAction.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName = request.form.get('loginName')
        userPass = request.form.get('loginPass')
        session['uLogin'] = True
        session['uAdmin'] = 1
        return '2'
    else:
        uLogin = session.get("uLogin")
        if uLogin:
            return redirect('/home.html')
        else:
            session['uLogin'] = True
            session['uAdmin'] = 1
            return redirect('/home.html')
            # return render_template("login/login.html")


@loginAction.route("/logout.html", methods=['GET', 'POST'])
def logout():
    session.pop("uLogin", None)
    session.pop("uUserName", None)
    return redirect("/")
