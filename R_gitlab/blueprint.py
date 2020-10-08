from logging import error
from flask import Blueprint, render_template, session, redirect, url_for
import requests

gitlab_routes = Blueprint("gitlab", __name__, url_prefix="/gitlab")

token = "XEQYLB4d-AJgp99QJaSx"


@gitlab_routes.route("")
def index():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for("index"))
    try:
        usuarios = requests.get("http://192.168.1.9/api/v4/users?private_token={}".format(token))
        usuarios = usuarios.json()
        
        projetos = requests.get("http://192.168.1.9/api/v4/projects?private_token={}".format(token))
        projetos = projetos.json()
    except Exception as error:
        return "{}".format(error)
    return render_template("gitlab.html", users=usuarios, projects=projetos)



