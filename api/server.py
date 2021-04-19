from api.utility import struct_msg
from flask import Flask, render_template, request, jsonify, render_template, redirect, url_for
from config import api_configuration
import datetime
import vonage


app = Flask(__name__, template_folder="../templates")
api_config = api_configuration()
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
client = vonage.Client(key=api_config["vonage_key"], secret=api_config["vonage_secret"])
sms = vonage.Sms(client)
Phno = None
hours = 0

@app.errorhandler(400)
def error_400(error):
    """
    handle 400 error
    Args:
        error: the flask error
    Returns:
        400 JSON error
    """
    return jsonify(
        struct_msg(status="error", msg=error.description)
    ), 400


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/updateNumber", methods=["POST"])
def updateNumber():
    try:
        if request.form["phno"] is not None:
            global Phno
            Phno = request.form["phno"]
            return redirect(url_for('index'))
    except KeyError:
        return render_template('index.html', error="Phone Number Not Updated Successfully. Try Again")


@app.route("/hoursRunning", methods=["GET"])
def getHours():
    global hours
    return {"hours": hours}

@app.route("/sendMessage", methods=["POST"])
def sendMsg():
    global hours
    hours = hours + 1
    global Phno
    if Phno is not None:
        time = request.get_data().decode("utf-8").strip('\"')
        datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
        for i in range(0,5):
            responseData = sms.send_message (
                {
                "from": "ReminderApp",
                "to": Phno,
                "text": "Hi, wake up",
                }
            )
            if responseData["messages"][0]["status"] == "0":
                break
            else:
                app.logger.info('Failed Message Attempt:  %s', {responseData['messages'][0]['error-text']})
    return ('', 204)
