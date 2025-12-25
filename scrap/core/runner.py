"""Orchestrates scraping and persistence."""

from __future__ import annotations

from typing import Iterable, Protocol

from core.models import Offer
from core.scraper import BaseOfferScraper


class OfferRepository(Protocol):
    def ensure_table(self, table_name: str) -> None:
        raise NotImplementedError

    def insert(self, table_name: str, offers: Iterable[Offer]) -> None:
        raise NotImplementedError


class ScrapeRunner:
    """Coordinates scraper execution and storage."""

    def i__init__(self, scrapers: Iterable[BaseOfferScraper], repository: OfferRepository) -> None:
        self._scrapers = list(scrapers)
        self._repository = repository

    def run(self) -> None:
        for scraper in self._scrapers:
            self._repository.ensure_table(scraper.table_name)
            offers = scraper.scrape()
            self._repository.insert(scraper.table_name, offers)
