import os

from flask import Response, redirect, render_template, request
from report_of_monaco_racing import get_racer, groper

from my_app import app
from my_app.functions_view import form_racers


@app.route("/")
@app.route("/report")
def report() -> str:
    return render_template("report.html")


@app.route("/report/drivers")
def drivers() -> str:
    args = request.args.to_dict()

    if args.get("order") == "desc":
        return render_template("drivers.html", racers=form_racers(True))

    if not args or args.get("order") == "asc":
        return render_template("drivers.html", racers=form_racers())


@app.route("/report/drivers/driver_id=<driver_name>")
def single_driver(driver_name: str) -> str:
    racer_info = str(get_racer(groper(os.environ["TARGET_DIR"]), driver_name))
    return render_template("driver_info.html", racer_info=racer_info)


@app.route("/report/drivers/driver_handle", methods=["POST"])
def handle_data() -> Response:
    fullname = request.form["fullname"]
    return redirect(f"/report/drivers/driver_id={fullname}")
