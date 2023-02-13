import os

from report_of_monaco_racing import Racer, groper, sort_racers


def racer_to_str(driver_id: str) -> str:
    drivers = groper(os.environ["TARGET_DIR"])
    for driver in drivers:
        driver_abbr = get_abbr(driver)
        if driver_abbr == driver_id:
            return str(driver)


def form_racers(reverse: bool = False) -> (list[str], list[str]):
    racers_list = sort_racers(
        groper(os.environ["TARGET_DIR"]), reverse
    )
    racers_dict = {get_abbr(racer): str(racer) for racer in racers_list}
    return racers_dict


def get_abbr(driver: Racer) -> str:
    name_split = driver.fullname.split()
    driver_abbr = name_split[0][0] + name_split[1][0] + driver.team[0]
    return driver_abbr
