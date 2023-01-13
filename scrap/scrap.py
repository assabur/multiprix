from orange import orange
import clickhouse_driver
import json

ch = clickhouse_driver.Client("localhost")

ch.execute(
    """--sql
CREATE TABLE IF NOT EXISTS orange (
    datetime DateTime default now(),
    data String
)
ENGINE=MergeTree
ORDER BY datetime
"""
)

ch.execute("insert into orange(data) values", [[json.dumps(o)] for o in orange()])
