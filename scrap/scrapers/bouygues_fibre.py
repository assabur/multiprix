"""Scraper dédié au réseau Orange et ses offres."""

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
            session.open("https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement")
            offers: list[Offer] = []
            for index in (1, 2, 3):
                prix_promo = session.text(
                    f"/html/body/main/section[1]/div/div/div[5]/div/div[1]/div/div/div/div/div/div[{index}]/div/div/div/div"

                )
                debit = session.text(
                    f"/html/body/main/section[1]/div/div/div[5]/div/div[1]/div/div/div/div/div/div[{index}]/div/div/div/div/div/div[1]/div/p"
                )
                prix = session.text(
                   f"/html/body/main/section[1]/div/div/div[5]/div/div[1]/div/div/div/div/div/div[{index}]/div/div/div/div/div/div[4]/div/div/span[1]/span[1]"
                )
                offers.append(
                    Offer(
                        offre=f"fibre {index} bouygues",
                        prix=parse_price_to_int(prix),
                        prix_promo=parse_price_to_int(prix_promo),
                        debit=debit,
                    )
                )
            return offers
        finally:
            session.close()
