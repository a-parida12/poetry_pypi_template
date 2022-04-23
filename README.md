# poetry_pypi_template
A minimal template for creating a pypi package using poetry and github actions

## Install Poetry in your Environment

- activate your environment.
- install poetry `python -m  pip install poetry`

## Update the Project Toml

- Insert/Update the values in the `pyproject.toml` under `tool.poetry`
- Dont forget to update the desired python version under the `tool.poetry.dependencies`
- Dont forget to modify the release branch under `tool.semantic_release` (assumption is `main` is the release branch)
- add project dependancies. eg - if you want `numpy` as an dependancy simply run `poetry add numpy`
- install the dependancies by running `poetry install`
- More information on setting up a [project with poetry](https://realpython.com/dependency-management-python-poetry/)

## Write Code for your python package

- Create a project folder. eg. `hapi_pypi` here
- add all the code/implemenations in the folder.

## Implement the Tests

- Check the functionality of the project folder by implementing tests.
- Implement tests in the `tests` folder.
- All the tests should pass when you run the command `poetry run pytest tests/`
- Details on how to implement [tests with pytest](https://realpython.com/pytest-python-testing/).

