#!/usr/bin/env python3


from flask import Flask, render_template
import logging

from R_jenkins.blueprint import jenkins_routes
from R_docker.blueprint import docker_routes
from R_gitlab.blueprint import gitlab_routes
from R_ldap.blueprint import ldap_routes


app=Flask(__name__)

app.register_blueprint(jenkins_routes)
app.register_blueprint(docker_routes)
app.register_blueprint(gitlab_routes)
app.register_blueprint(ldap_routes)
app.secret_key = "mySecretKey"

logging.basicConfig(
    filename= "app.log",
    level= logging.INFO,
    format= "%(asctime)s [ %(levelname)s ] %(name)s [ %(funcName)s ] [ %(filename)s, %(lineno)s ] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]"
)


@app.route('/')
def index():
    return render_template('index.html', title='Lista de nomes:')

if __name__ == '__main__':
    app.run(debug=False)
