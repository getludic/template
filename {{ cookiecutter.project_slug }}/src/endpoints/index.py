from ludic.catalog.headers import H1

from src.pages import Page
from src.components import Hello
from src.main import app


@app.get("/")
async def homepage() -> Page:
    return Page(
        H1("{{ cookiecutter.project_name }} Homepage"),
        Hello(name="Stranger"),
    )
