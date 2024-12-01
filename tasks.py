from pathlib import Path

from invoke import task


@task
def lint(c):
    c.run("mypy src")
    c.run("ruff format src")
    c.run("ruff check --fix --select I src")


@task(optional=["year"])
def new_solution(c, day, year="2024"):
    module_path = (
        Path(__file__)
        .parent.joinpath(Path("src/aoc/2024"))
        .joinpath(Path(f"day_{day}"))
    )
    module_path.mkdir()

    c.run(f"cp solution_template {module_path.joinpath(Path("solution.py"))}")
