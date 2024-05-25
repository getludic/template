from ludic.catalog.headers import H1
from ludic.catalog.typography import Paragraph

from src.pages import Page
from src.main import app


@app.exception_handler(404)
async def not_found() -> Page:
    return Page(
        H1("Page Not Found"),
        Paragraph("The page you are looking for was not found."),
    )


@app.exception_handler(500)
async def server_error() -> Page:
    return Page(
        H1("Server Error"),
        Paragraph("Server encountered an error during processing."),
    )
