"""Application wiring for scraping tasks."""

import os

from core.page import playwright_session_factory
from core.runner import ScrapeRunner
from scrapers.orange_fibre import OrangeFibreScraper
from scrapers.sosh_fibre import SoshFibreScraper
from scrapers.bouygues_fibre import BouyguesFibreScraper
from storage.clickhouse_repo import ClickhouseOfferRepository


def run() -> None:
    repository = ClickhouseOfferRepository(
        host=os.getenv("CLICKHOUSE_HOST", "localhost"),
        user=os.getenv("CLICKHOUSE_USER", "default"),
        password=os.getenv("CLICKHOUSE_PASSWORD", ""),
    )
    scrapers = [
        OrangeFibreScraper(playwright_session_factory),
        SoshFibreScraper(playwright_session_factory),
        BouyguesFibreScraper(playwright_session_factory)
    ]
    ScrapeRunner(scrapers, repository).run()
