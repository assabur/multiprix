"""Persistence adapters for scraped data."""

from .clickhouse_repo import ClickhouseOfferRepository

__all__ = ["ClickhouseOfferRepository"]
