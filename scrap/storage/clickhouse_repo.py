"""ClickHouse persistence for scraped offers."""

from __future__ import annotations

import json
from typing import Iterable

import clickhouse_driver

from core.models import Offer


class ClickhouseOfferRepository:
    """Stores offers in ClickHouse with a simple schema."""

    def __init__(self, host: str = "localhost") -> None:
        self._client = clickhouse_driver.Client(host)

    def ensure_table(self, table_name: str) -> None:
        self._client.execute(
            f"""--sql
CREATE TABLE IF NOT EXISTS {table_name} (
    datetime DateTime default now(),
    data String
)
ENGINE=MergeTree
ORDER BY datetime
"""
        )

    def insert(self, table_name: str, offers: Iterable[Offer]) -> None:
        payloads = [[json.dumps(offer.to_dict())] for offer in offers]
        if payloads:
            self._client.execute(f"insert into {table_name}(data) values", payloads)
