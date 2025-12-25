from typing import Protocol


class PageSession(Protocol):
    def open(self, url: str) -> None:
        raise NotImplementedError

    def text(self, xpath: str) -> str:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


class FakePageSession(PageSession):
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping
        self.opened_url = None
        self.closed = False

    def open(self, url: str) -> None:
        self.opened_url = url

    def text(self, xpath: str) -> str:
        return self.mapping[xpath]

    def close(self) -> None:
        self.closed = True
