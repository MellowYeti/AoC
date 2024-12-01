import logging
from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path

from aoc.utility import input_feed

logging.basicConfig()
logger = logging.getLogger(__file__)


def run_puzzle(year: int, day: int):
    try:
        solution_module = import_module(f"aoc.{year}.day_{day}.solution")
        solution_instance = solution_module.Solution()
    except ImportError as e:
        logger.error(
            "Could not import solution module, check `year` and `day` arguments"
        )

    input_path = (
        Path(__file__)
        .parent.joinpath(Path(str(year)))
        .joinpath(Path(f"day_{day}").joinpath("input.txt"))
    )

    print(f"-= Advent of Code {year}: Day {day} =-")
    print(f" - 🥈 Silver solution: {solution_instance.silver(input_feed(input_path))}")
    print(f" - 🥇 Gold solution: {solution_instance.gold(input_feed(input_path))}")


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="AoC by MellowYeti",
        description="Executes Advent of Code solutions",
        epilog="Merry Christmas",
    )

    parser.add_argument("-y", "--year", default=2024, help="Solution year, eg: 2024")
    parser.add_argument("-d", "--day", required=True, help="Solution day (1-25), eg: 1")

    args = parser.parse_args()

    run_puzzle(args.year, args.day)
