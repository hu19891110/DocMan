#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

imagesAction = Blueprint('imagesAction', __name__, template_folder='templates/')


@imagesAction.route("/images/index.html", methods=['GET', 'POST'])
def images_index():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("images/index.html", uUserName=uUserName)
    return redirect("/")
