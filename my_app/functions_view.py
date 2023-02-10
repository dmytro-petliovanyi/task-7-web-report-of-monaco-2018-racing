import os

from report_of_monaco_racing import get_racer, groper, sort_racers


def racer_to_str(driver_name: str) -> str:
    return str(get_racer(groper(os.environ["TARGET_DIR"]), driver_name))


def form_racers(reverse: bool = False) -> list[str]:
    return list(map(lambda x: str(x), sort_racers(
        groper(os.environ["TARGET_DIR"]), reverse
    )))
