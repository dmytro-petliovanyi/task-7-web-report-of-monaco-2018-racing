from flask import render_template, request

from my_app import app
from my_app.functions_view import form_racers, racer_to_str


@app.route("/")
@app.route("/report")
def report() -> str:
    return render_template("report.html")


@app.route("/report/drivers")
def drivers() -> str:
    args = request.args.to_dict()

    if args.get("order") == "desc":
        order = True

    if not args or args.get("order") == "asc":
        order = False

    return render_template("drivers.html", racers=form_racers(order))


@app.route("/report/drivers/driver_id=<driver_id>")
def single_driver(driver_id: str) -> str:
    racer_info = racer_to_str(driver_id)
    return render_template("driver_info.html", racer_info=racer_info)
