#!/usr/bin/env python
# encoding:utf-8
from flask import Blueprint, render_template, abort, request, redirect, session, jsonify

feedbackAction = Blueprint('feedbackAction', __name__, template_folder='templates/')


@feedbackAction.route("/feedback/index.html", methods=['GET', 'POST'])
def feedback_index():
    uLogin = session.get("uLogin")
    uUserName = session.get("uUserName")
    if uLogin:
        if request.method == 'POST':
            pass
        else:
            return render_template("feedback/index.html", uUserName=uUserName)
    return redirect("/")
