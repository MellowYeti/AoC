from invoke import task

@task
def lint(c):
    c.run("mypy src")
    c.run("ruff format src")
    c.run("ruff check --fix --select I src")