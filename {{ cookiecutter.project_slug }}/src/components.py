from typing import override

from ludic.attrs import Attrs
from ludic.catalog.layouts import Box
from ludic.html import b
from ludic.types import Component, NoChildren


class HelloAttrs(Attrs):
    name: str


class Hello(Component[NoChildren, HelloAttrs]):
    classes = ["greetings"]

    @override
    def render(self) -> Box:
        return Box(f"Hello, {b(self.attrs["name"])}! This is a sample component.")
