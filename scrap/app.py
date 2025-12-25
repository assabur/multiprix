"""Application wiring for scraping tasks."""

from core.page import playwright_session_factory
from core.runner import ScrapeRunner
from scrapers.orange_fibre import OrangeFibreScraper
from scrapers.sosh_fibre import SoshFibreScraper
from storage.clickhouse_repo import ClickhouseOfferRepository


def run() -> None:
    repository = ClickhouseOfferRepository(host="localhost")
    scrapers = [
        OrangeFibreScraper(playwright_session_factory),
        SoshFibreScraper(playwright_session_factory),
    ]
    ScrapeRunner(scrapers, repository).run()
