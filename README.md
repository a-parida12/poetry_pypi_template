# poetry_pypi_template

> A minimal template for creating a pypi package using poetry and github actions

This template allows the creation of python projects managed by poetry to be submitted to PyPi. All the github actions have been setup too. The github actions run tests on every push and also creates and new pacakage and pushes to the pypi when a merge happens to the release branch.

Just follow the seteps below for an hassle free setup of the project.

## Create from the Project Template

- [Click here](https://github.com/a-parida12/poetry_pypi_template/generate) to create a new repo (you need to be logged in to GitHub for this link to work), and follow the instructions to create a new repo from this template.
- `git clone` your new repo

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

## Github Actions Configuration

- all the github actions are defined in the `.github/workflows` folder
- setup the `test.yml`. Update the env variables according to the project setup before. The default coverage limit is set to 90% ie the test will fail below the coverage of 90.

``` yaml
env:
  PYTHON_VERSION: "3.8.5"
  PROJECT_FOLDER: hapy_pypi
  TEST_FOLDER: tests
  COVERAGE_LIMIT: 90
```

- setup the similar env variables in `release.yml` as well.

## Setup Secrets

### Pypi Creds

These secrets are used to push releases to the pypi repository.

- Generate a pypi [api token](https://pypi.org/help/#apitoken)
- [Set Repo Secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md)
- Add `PYPI_USER` as `__token__`
- Add `PYPI_TOKEN` as the token from above step including the `pypi-` prefix

### Github Token

This secret is required to generate the `CHANGELOG.MD` and update the version by SemRel.

- Generate a [github token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Set Repo Secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md)
- Add `GH_TOKEN` as the token from github.