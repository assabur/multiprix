from scrapers.sosh_fibre import SoshFibreScraper
from tests.helpers import FakePageSession



def test_sosh_scraper_builds_offers() -> None:
    mapping = {
        '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[2]': "19,99 €",
        '//*[@id="pills-fibre"]/div[2]/div/div[2]/div/div/div': "300 Mb/s.",
        '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[4]/span[2]': "29,99 €",
    }
    session = FakePageSession(mapping)

    scraper = SoshFibreScraper(lambda: session)
    offers = scraper.scrape()

    assert session.opened_url.startswith("https://shop.sosh.fr/box-internet")
    assert session.closed is True
    assert len(offers) == 1
    assert offers[0].offre == "Fibre sosh"
    assert offers[0].prix == 2999
    assert offers[0].prix_promo == 1999
    assert offers[0].debit == "300 Mb/s"
