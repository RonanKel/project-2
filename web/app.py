"""
Ronan Kelly's Flask API.
"""

import os
import configparser # used for reading credentials.ini and default.ini
from flask import Flask, abort, send_from_directory

app = Flask(__name__)

@app.route("/<string:request>")

def hello(request):
    if ("~" in request) or (".." in request):
        abort(403)

    elif (os.path.isfile(f"pages/{request}")):
        return send_from_directory("pages/", request), 200

    else:
        abort(404)



@app.errorhandler(403)
def forbidden(e):
    return send_from_directory("pages/", "403.html"), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory("pages/", "404.html"), 404

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    portnum = config["SERVER"]["PORT"]

    app.run(debug=True, host='0.0.0.0', port=portnum)
