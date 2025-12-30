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
            session.open("https://www.bouyguestelecom.fr/offres-internet")
            offers: list[Offer] = []
            for index in (1, 2, 3):
                prix_promo = session.text(
                    f"//div[{index}]/section/div/div[1]/div[2]/div/p/span[1]"
                )
                debit = session.text(
                    f"//div[{index}]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span"
                )
                prix = session.text(
                    f"//div[{index}]/section/div/div[1]/div[2]/div/p/span[3]/span[2]"
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
