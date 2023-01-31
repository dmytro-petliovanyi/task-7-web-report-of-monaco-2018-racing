from flask import Flask, render_template
from report_of_monaco_racing.groper_and_printer import groper
from report_of_monaco_racing.processing_functions import sort_racers

app = Flask(__name__)


@app.route("/")
@app.route("/report")
def report():
    return "jaja"


@app.route("/report/drivers")
def drivers():
    racers = list(map(lambda x: str(x), sort_racers(
        groper(
            "C:/Users/petli/PycharmProjects/task-7-web-report-of-monaco-2018-racing/race_info"
        )
    )))
    return render_template("drivers.html", racers=racers)


@app.route("/report/drivers/<string:driver_name>")
def driver_info(driver_name: str):
    return "jaja"


if __name__ == "__main__":
    app.run(debug=True)
