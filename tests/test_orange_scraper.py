from scrapers.orange_fibre import OrangeFibreScraper
from tests.helpers import FakePageSession


def test_orange_scraper_builds_offers() -> None:
    mapping = {
        "//div[1]/section/div/div[1]/div[2]/div/p/span[1]": "29,99 €",
        "//div[1]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "1 Gb/s",
        "//div[1]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "39,99 €",
        "//div[2]/section/div/div[1]/div[2]/div/p/span[1]": "34,99 €",
        "//div[2]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "2 Gb/s",
        "//div[2]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "49,99 €",
        "//div[3]/section/div/div[1]/div[2]/div/p/span[1]": "39,99 €",
        "//div[3]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span": "8 Gb/s",
        "//div[3]/section/div/div[1]/div[2]/div/p/span[3]/span[2]": "59,99 €",
    }
    session = FakePageSession(mapping)

    scraper = OrangeFibreScraper(lambda: session)
    offers = scraper.scrape()

    assert session.opened_url == "https://boutique.orange.fr/internet/offres-fibre"
    assert session.closed is True
    assert len(offers) == 3
    assert offers[0].offre == "fibre 1 orange"
    assert offers[0].prix == 3999
    assert offers[0].prix_promo == 2999
