"""ClickHouse persistence for scraped offers."""

from __future__ import annotations

import json
import os
from typing import Iterable

import clickhouse_driver

from core.models import Offer


class ClickhouseOfferRepository:
    """Stores offers in ClickHouse with a simple schema."""

    def __init__(
        self,
        host: str = "localhost",
        user: str | None = None,
        password: str | None = None,
    ) -> None:
        ch_user = user or os.getenv("CLICKHOUSE_USER", "default")
        ch_password = (
            password if password is not None else os.getenv("CLICKHOUSE_PASSWORD", "")
        )
        self._client = clickhouse_driver.Client(host, user=ch_user, password=ch_password)

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
