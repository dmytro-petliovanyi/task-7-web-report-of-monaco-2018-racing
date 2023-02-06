from flask import render_template, request
from report_of_monaco_racing.groper_and_printer import groper
from report_of_monaco_racing.processing_functions import get_racer, sort_racers

from my_app import app


@app.route("/")
@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/report/drivers")
def drivers():
    racers = list(map(lambda x: str(x), sort_racers(
        groper(
            "C:/Users/petli/PycharmProjects/task-7-web-report-of-monaco-2018-racing/race_info"
        )
    )))
    return render_template("drivers.html", racers=racers)


@app.route("/handle_data", methods=["POST"])
def handle_data():
    fullname = request.form["fullname"]
    racer_info = str(get_racer(groper(
        "C:/Users/petli/PycharmProjects/task-7-web-report-of-monaco-2018-racing/race_info"
    ), fullname))
    return render_template("driver_info.html", racer_info=racer_info)


if __name__ == "__main__":
    app.run(debug=True)
