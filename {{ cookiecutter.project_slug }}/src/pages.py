from typing import override

from ludic.attrs import GlobalAttrs
from ludic.catalog.layouts import Center, Stack
from ludic.catalog.pages import Body, Head, HtmlPage
from ludic.html import meta, link
from ludic.types import AnyChildren, Component


class Page(Component[AnyChildren, GlobalAttrs]):
    @override
    def render(self) -> HtmlPage:
        return HtmlPage(
            Head(
                meta(charset="utf-8"),
                link(rel="icon", href="/static/favicon.png"),
                title="{{ cookiecutter.project_name }}",
            ),
            Body(
                Center(
                    Stack(*self.children, **self.attrs),
                    style={"padding-block": self.theme.sizes.xl},
                ),
                htmx_version="latest",
            ),
        )
