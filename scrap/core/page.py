"""implmentation de l'abstraction d'une page"""

from __future__ import annotations

from typing import Protocol

from playwright.sync_api import sync_playwright


class PageSession(Protocol):
    """Todo : """

    def open(self, url: str) -> None:
        raise NotImplementedError

    def text(self, xpath: str) -> str:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


class PlaywrightPageSession:
    """Playwright basé sure session afin de rcupere le  texte Du dociment object model par XPath."""

    def __init__(self) -> None:
        self._playwright = sync_playwright().start()
        self._browser = None
        self._context = None
        self._page = None

    def open(self, url: str) -> None:
        self._browser = self._playwright.chromium.launch(headless=True)
        self._context = self._browser.new_context()
        self._page = self._context.new_page()
        self._page.goto(url)

    def text(self, xpath: str) -> str:
        if self._page is None:
            raise RuntimeError("page is not initialized; call open() first")
        return self._page.locator(f"xpath={xpath}").first.text_content()

    def close(self) -> None:
        if self._context is not None:
            self._context.close()
        if self._browser is not None:
            self._browser.close()
        self._playwright.stop()


def playwright_session_factory() -> PageSession:
    """L'usine la factory pour creer un nouveau Playwright session pour l'execution de cahque runn."""
    return PlaywrightPageSession()
