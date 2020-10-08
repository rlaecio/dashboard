from flask import Blueprint, render_template, redirect, url_for, session, current_app, flash
import docker


docker_routes = Blueprint("docker", __name__, url_prefix="/docker")

@docker_routes.route("") 
def index():
    
    if not "logged" in session or not session["logged"]:
        return redirect(url_for("index"))
    try:
        docker_con = docker.DockerClient("tcp://192.168.1.10:2376")
        container = docker_con.containers.get("flask-app")
        flask_app = {
            "id": container.short_id,
            "imagem": container.image.tags[0],
            "nome": container.name,
            "status": container.status  
        }
        current_app.logger.info("Container encontrado com sucesso")
    except Exception as e:
        flask_app = None
        current_app.logger.info("Container não  encontrado")
    return render_template("docker.html", container=flask_app)

@docker_routes.route("/start") 
def start():
    
    if not "logged" in session or not session["logged"]:
        return redirect(url_for("index"))
    try:
        docker_con = docker.DockerClient("tcp://192.168.1.10:2376")
        container = docker_con.containers.get("flask-app")
        container.start()
        current_app.logger.info("Container iniciado com sucesso")
        flash("Container iniciado com sucesso", "success")
    except docker.errors.NotFound:
        current_app.logger.info("Container não foi iniciado")
        flash("Container não foi iniciado", "danger")
    return redirect(url_for('docker.index'))

@docker_routes.route("/stop") 
def stop():
    
    if not "logged" in session or not session["logged"]:
        return redirect(url_for("index"))
    try:
        docker_con = docker.DockerClient("tcp://192.168.1.10:2376")
        container = docker_con.containers.get("flask-app")
        container.stop()
        current_app.logger.info("Container parado com sucesso")
        flash("Container parado com sucesso", "success")
    except docker.errors.NotFound:
        current_app.logger.info("Container não foi parado")
        flash("Container não foi parado", "danger")
    return redirect(url_for('docker.index'))