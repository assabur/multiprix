"""Backward-compatible wrapper for Sosh scrapers."""

from core.page import playwright_session_factory
from scrapers.sosh_fibre import SoshFibreScraper


def sosh() -> list[dict]:
    scraper = SoshFibreScraper(playwright_session_factory)
    return [offer.to_dict() for offer in scraper.scrape()]


if __name__ == "__main__":
    sosh()
