from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from ludic.html import style
from ludic.styles import themes, types
from ludic.web import LudicApp
from ludic.web.routing import Mount
from starlette.staticfiles import StaticFiles


themes.set_default_theme(
    themes.LightTheme(
        measure=types.Size(70, "ch"),
        fonts=themes.Fonts(size=types.Size(1.1, "em"))
    )
)


@asynccontextmanager
async def lifespan(_: LudicApp) -> AsyncIterator[None]:
    style.load(cache=True)
    yield


app = LudicApp(
    debug=True,
    lifespan=lifespan,
    routes=[Mount("/static", StaticFiles(directory="static"), name="static")],
)


import src.endpoints.index  # noqa
import src.endpoints.errors  # noqa
