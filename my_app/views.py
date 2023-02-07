import os

from flask import render_template, request
from report_of_monaco_racing import get_racer, groper

from my_app import app
from my_app.functions_view import form_racers, upload_files


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/report", methods=["POST", "GET"])
def report() -> str:
    upload_files()

    return render_template("report.html")


@app.route("/report/drivers")
def drivers() -> str:
    racers = form_racers()
    return render_template("drivers.html", racers=racers)


@app.route("/report/drivers_desc")
def drivers_desc() -> str:
    racers = form_racers(True)
    return render_template("drivers.html", racers=racers)


@app.route("/handle_data", methods=["POST"])
def handle_data() -> str:
    fullname = request.form["fullname"]
    racer_info = str(get_racer(groper(f"{os.getcwd()}/race_info"), fullname))
    return render_template("driver_info.html", racer_info=racer_info)
