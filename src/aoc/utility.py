import logging
import os
from pathlib import Path

import httpx

logger = logging.getLogger(__file__)


def get_input_path(day: str, year: str) -> Path:
    return (
        Path(__file__)
        .parent.joinpath(Path(str(f"year_{year}")))
        .joinpath(Path(f"day_{day}").joinpath("input.txt"))
    )


def get_input_from_aoc(day: str, year: str):
    session = os.getenv("SESSION_COOKIE")

    if not session:
        logger.error("SESSION_COOKIE not set")
        raise SystemExit

    result = httpx.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}
    )
    result.raise_for_status()

    input_path = get_input_path(day, year)
    with open(input_path, "w") as file:
        file.write(result.text)


def input_feed(day: str, year: str):
    input_path = get_input_path(day, year)

    if not input_path.exists():
        logger.error(f"Unable to find input for day: {day}, of {year}")
        get_input_from_aoc(day, year)

    with open(input_path) as input:
        for line in input:
            yield line
