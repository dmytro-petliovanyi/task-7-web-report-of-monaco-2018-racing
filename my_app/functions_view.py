import os

from flask import request
from report_of_monaco_racing import groper, sort_racers


def upload_files() -> None:
    if request.method == 'POST':
        files = request.files.getlist('files[]')

        target_dir = f"{os.getcwd()}/race_info"

        for file in files:
            if file:

                if not os.path.isdir(target_dir):
                    os.mkdir(target_dir)

                file.save(os.path.join(target_dir, str(file.filename)))


def form_racers(reverse: bool = False) -> list[str]:

    return list(map(lambda x: str(x), sort_racers(
        groper(f"{os.getcwd()}/race_info"), reverse
    )))
