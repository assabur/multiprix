"""Backward-compatible wrapper for Orange scrapers."""

from core.page import playwright_session_factory
from scrapers.orange_fibre import OrangeFibreScraper


def orange() -> list[dict]:
    scraper = OrangeFibreScraper(playwright_session_factory)
    return [offer.to_dict() for offer in scraper.scrape()]


if __name__ == "__main__":
    orange()
