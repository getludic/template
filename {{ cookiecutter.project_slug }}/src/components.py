from typing import override

from ludic import Attrs, Component
from ludic.catalog.layouts import Box
from ludic.html import b
from ludic.types import NoChildren


class HelloAttrs(Attrs):
    name: str


class Hello(Component[NoChildren, HelloAttrs]):
    classes = ["greetings"]

    @override
    def render(self) -> Box:
        return Box(f"Hello, {b(self.attrs["name"])}! This is a sample component.")
