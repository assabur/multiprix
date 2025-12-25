"""Definitions core partagees."""

from .models import Offer
from .parsing import parse_price_to_int
from .runner import ScrapeRunner
from .scraper import BaseOfferScraper

try:
    from .page import PageSession, PlaywrightPageSession, playwright_session_factory
except ModuleNotFoundError:
    PageSession = None
    PlaywrightPageSession = None

    def playwright_session_factory():  # type: ignore[no-redef]
        raise ModuleNotFoundError("playwright is required for browser sessions")


__all__ = [
    "Offer",
    "PageSession",
    "PlaywrightPageSession",
    "playwright_session_factory",
    "parse_price_to_int",
    "ScrapeRunner",
    "BaseOfferScraper",
]
