import os
import uuid

import os
import pytest

from core.models import Offer
from storage.clickhouse_repo import ClickhouseOfferRepository


pytestmark = pytest.mark.integration


def test_clickhouse_repository_roundtrip() -> None:
    host = os.getenv("CLICKHOUSE_HOST")
    if not host:
        pytest.skip("CLICKHOUSE_HOST is not set")

    clickhouse_driver = pytest.importorskip("clickhouse_driver")
    client = clickhouse_driver.Client(
        host,
        user=os.getenv("CLICKHOUSE_USER", "default"),
        password=os.getenv("CLICKHOUSE_PASSWORD", ""),
    )
    table_name = f"test_offers_{uuid.uuid4().hex}"
    repository = ClickhouseOfferRepository(host=host)

    try:
        repository.ensure_table(table_name)
        repository.insert(
            table_name,
            [Offer(offre="fibre test", prix=1999, prix_promo=999, debit="1 Gb/s")],
        )
        rows = client.execute(f"select count() from {table_name}")
        assert rows[0][0] == 1
    finally:
        client.execute(f"drop table if exists {table_name}")
