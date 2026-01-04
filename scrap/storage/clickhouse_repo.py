"""ClickHouse persistence for scraped offers."""

from __future__ import annotations

import hashlib
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
    offer_key String,
    datetime DateTime default now(),
    data String
)
ENGINE=MergeTree
ORDER BY (offer_key, datetime)
"""
        )
        self._client.execute(
            f"ALTER TABLE {table_name} ADD COLUMN IF NOT EXISTS offer_key String"
        )

    def insert(self, table_name: str, offers: Iterable[Offer]) -> None:
        payloads = [
            [self._offer_key(table_name, offer), json.dumps(offer.to_dict())]
            for offer in offers
        ]
        if payloads:
            self._client.execute(
                f"insert into {table_name}(offer_key, data) values", payloads
            )

    @staticmethod
    def _offer_key(table_name: str, offer: Offer) -> str:
        raw = (
            f"{table_name}|{offer.offre}|{offer.debit}|"
            f"{offer.prix}|{offer.prix_promo}"
        )
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
