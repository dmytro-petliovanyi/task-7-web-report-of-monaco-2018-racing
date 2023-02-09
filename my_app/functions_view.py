import os

from report_of_monaco_racing import groper, sort_racers


def form_racers(reverse: bool = False) -> list[str]:
    return list(map(lambda x: str(x), sort_racers(
        groper(os.environ["TARGET_DIR"]), reverse
    )))
