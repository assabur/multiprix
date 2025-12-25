"""Abstract base class for offer scrapers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, TYPE_CHECKING

from core.models import Offer

if TYPE_CHECKING:
    from core.page import PageSession


class BaseOfferScraper(ABC):
    """Base scraper contract shared by all operators."""

    name: str
    table_name: str

    def __init__(self, session_factory: Callable[[], "PageSession"]) -> None:
        self._session_factory = session_factory

    @abstractmethod
    def scrape(self) -> list[Offer]:
        raise NotImplementedError
