import logging
import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from stem.control import Controller

load_dotenv(find_dotenv())

app = Flask(__name__)

app.logger.setLevel(logging.INFO)


@app.route("/")
def index():
    return render_template("index.html")


with Controller.from_port() as controller:
    password = os.environ.get("TOR_PASSWORD")

    if password is None:
        app.logger.error("Couldn't find TOR_PASSWORD")
        exit(1)

    controller.authenticate(password)

    data_directory = controller.get_conf(param="DataDirectory", default="/tmp") + "/tahriri"

    service = controller.create_hidden_service(path=data_directory, port=80, target_port=5000)

    if service.hostname is None:
        app.logger.error("Run the application in the same user as tor service!")
        controller.remove_hidden_service(path=data_directory)
        exit(1)

    app.logger.info("Address:" + service.hostname)

    try:
        app.run()
    finally:
        controller.remove_hidden_service(path=data_directory)
