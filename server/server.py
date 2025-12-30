import asyncio
import os
import tornado.web
import clickhouse_driver
import pandas, tabulate

ch = clickhouse_driver.Client(
    os.getenv("CLICKHOUSE_HOST", "localhost"),
    user=os.getenv("CLICKHOUSE_USER", "default"),
    password=os.getenv("CLICKHOUSE_PASSWORD", ""),
)


def get_data():
    return {
        "orange": ch.query_dataframe(
            "select JSONExtractInt(data, 'prix') as prix,datetime from orange"
        ).to_html(),
        "sosh": ch.query_dataframe(
            "select JSONExtractInt(data, 'prix') as prix,datetime from sosh"
        ).to_html(),
        "bouygues": ch.query_dataframe(
            "select JSONExtractInt(data, 'prix') as prix,datetime from bouygues"
        ).to_html(),
    }


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.template.html", data=get_data())


async def main():
    tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        debug=True,
    ).listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
