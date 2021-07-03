import logging
from datetime import datetime
from flask import Flask
from werkzeug.wrappers import response
from flask import json
app = Flask(__name__)

def get_info_log(endpoint):
    log = f"{datetime.now()}, {endpoint} was reached successfully"
    app.logger.info(log)

@app.route("/")
def hello():
    get_info_log("root")
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({
            "result": "OK - healthy"
        }),
        status = 200,
        mimetype = "application/json"
    )

    get_info_log("status")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({
            "data": {
                "UserCount": 140,
                "UserCountActive": 23
            }
        }),
        status = 200,
        mimetype = "application/json"
    )

    get_info_log("metrics")
    return response

if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        level=logging.DEBUG
    )
    app.run(host='0.0.0.0')
