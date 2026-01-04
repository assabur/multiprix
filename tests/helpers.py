from typing import Protocol


class PageSession(Protocol):
    def open(self, url: str) -> None:
        raise NotImplementedError

    def text(self, xpath: str) -> str:
        raise NotImplementedError

    def attr(self, xpath: str, name: str) -> str | None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


class FakePageSession(PageSession):
    def __init__(
        self,
        mapping: dict[str, str],
        attr_mapping: dict[tuple[str, str], str] | None = None,
    ) -> None:
        self.mapping = mapping
        self.attr_mapping = attr_mapping or {}
        self.opened_url = None
        self.closed = False

    def open(self, url: str) -> None:
        self.opened_url = url

    def text(self, xpath: str) -> str:
        return self.mapping[xpath]

    def attr(self, xpath: str, name: str) -> str | None:
        return self.attr_mapping.get((xpath, name))

    def close(self) -> None:
        self.closed = True
