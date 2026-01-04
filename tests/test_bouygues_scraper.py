from scrapers.bouygues_fibre import BouyguesFibreScraper
from tests.helpers import FakePageSession


def test_bouygues_scraper_builds_offers() -> None:
    mapping = {
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[1]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and not(contains(@class,'strike'))][1]": "19,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[1]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and contains(@class,'strike')][1]": "29,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[1]"
        "//p[contains(@class,'title') and contains(@class,'is-level-2')][1]": "130Go",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[2]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and not(contains(@class,'strike'))][1]": "24,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[2]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and contains(@class,'strike')][1]": "34,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[2]"
        "//p[contains(@class,'title') and contains(@class,'is-level-2')][1]": "150Go",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[3]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and not(contains(@class,'strike'))][1]": "29,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[3]"
        "//div[contains(@class,'price-container')]"
        "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
        "and contains(@class,'strike')][1]": "39,99 €",
        "(//div[@data-cy and starts-with(@data-cy,'plan-')])[3]"
        "//p[contains(@class,'title') and contains(@class,'is-level-2')][1]": "200Go",
    }
    session = FakePageSession(mapping)

    scraper = BouyguesFibreScraper(lambda: session)
    offers = scraper.scrape()

    assert session.opened_url is not None
    assert session.closed is True
    assert len(offers) == 3
    assert offers[0].prix == 2999
    assert offers[0].prix_promo == 1999
