"""Scraper dédié au réseau Bouygues et ses offres."""

from __future__ import annotations

from core.models import Offer
from core.parsing import parse_price_to_int
from core.scraper import BaseOfferScraper




class BouyguesFibreScraper(BaseOfferScraper):
    name = "bouygues"
    table_name = "bouygues"

    def scrape(self) -> list[Offer]:
        session = self._session_factory()
        try:
            session.open("https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement?smartphone=true")
            offers: list[Offer] = []
            for index in (1, 2, 3):
                base = f"(//div[@data-cy and starts-with(@data-cy,'plan-')])[{index}]"
                prix_promo = session.text(
                    f"{base}//div[contains(@class,'price-container')]"
                    "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
                    "and not(contains(@class,'strike'))][1]"
                )
                debit = session.text(
                    f"{base}//p[contains(@class,'title') and contains(@class,'is-level-2')][1]"
                )
                prix = session.text(
                    f"{base}//div[contains(@class,'price-container')]"
                    "//span[contains(concat(' ', normalize-space(@class), ' '), ' price ') "
                    "and contains(@class,'strike')][1]"
                )
                offers.append(
                    Offer(
                        offre=f"offre {index} bouygues",
                        prix=parse_price_to_int(prix),
                        prix_promo=parse_price_to_int(prix_promo),
                        debit=debit,
                    )
                )
            print (offers)
            return offers
        finally:
            session.close()
