#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

dockerAction = Blueprint('dockerAction', __name__, template_folder='templates/')


@dockerAction.route("/docker/index.html", methods=['GET', 'POST'])
def docker_index():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("docker/index.html", uUserName=uUserName)
    return redirect("/")


@dockerAction.route("/docker/detail.html", methods=['GET', 'POST'])
def docker_detail():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("docker/detail.html", uUserName=uUserName)
    return redirect("/")
