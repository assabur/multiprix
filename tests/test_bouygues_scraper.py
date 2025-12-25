from scrapers.bouygues_fibre import BouyguesFibreScraper
from tests.helpers import FakePageSession


def test_bouygues_scraper_builds_offers() -> None:
    mapping = {
        "//div[1]/section/div/div[1]/div[2]/div/p/span[1]": "19,99 €",
        "//div[1]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "1 Gb/s",
        "//div[1]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "29,99 €",
        "//div[2]/section/div/div[1]/div[2]/div/p/span[1]": "24,99 €",
        "//div[2]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "2 Gb/s",
        "//div[2]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "34,99 €",
        "//div[3]/section/div/div[1]/div[2]/div/p/span[1]": "29,99 €",
        "//div[3]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "8 Gb/s",
        "//div[3]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "39,99 €",
    }
    session = FakePageSession(mapping)

    scraper = BouyguesFibreScraper(lambda: session)
    offers = scraper.scrape()

    assert session.opened_url is not None
    assert session.closed is True
    assert len(offers) == 3
    assert offers[0].prix == 2999
    assert offers[0].prix_promo == 1999
