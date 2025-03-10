# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Running the App

Using UV (recommended):

```
uv venv --python 3.13
uv sync
uv run uvicorn --reload src.main:app
```

Or without UV:

```
pip install -e .
uvicorn --reload src.main:app
```

## Running the Tests

Using UV (recommended):

```
uv run pytest
```

Or without UV:

```
pytest
```
