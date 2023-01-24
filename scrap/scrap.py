from orange import orange
from sosh import sosh
import clickhouse_driver
import json

ch = clickhouse_driver.Client("localhost")

##Orange
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
## Sosh
ch.execute(
    """--sql
CREATE TABLE IF NOT EXISTS sosh (
    datetime DateTime default now(),
    data String
)
ENGINE=MergeTree
ORDER BY datetime
"""
)

ch.execute(
    "insert into sosh(data) values", [[json.dumps(s)] for s in sosh()]
)