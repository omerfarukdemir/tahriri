import os

from flask import Flask, render_template
from stem.control import Controller

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

with Controller.from_port() as controller:
  password = os.environ.get("TOR_PASSWORD")

  controller.authenticate(password)

  data_directory = controller.get_conf("DataDirectory", "/tmp") + "/tahriri"

  service = controller.create_hidden_service(data_directory, 80, target_port = 5000)

  if service.hostname:
    print(" * Address: " + service.hostname)
  else:
    print("Something wrong!")

  try:
    app.run()
  finally:
    controller.remove_hidden_service(data_directory)

