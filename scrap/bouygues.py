"""Backward-compatible wrapper for Orange scrapers."""

from core.page import playwright_session_factory
from scrapers.bouygues_fibre import BouyguesFibreScraper


def bouygue() -> list[dict]:
    scraper = BouyguesFibreScraper(playwright_session_factory)
    return [offer.to_dict() for offer in scraper.scrape()]


if __name__ == "__main__":
    bouygue()
