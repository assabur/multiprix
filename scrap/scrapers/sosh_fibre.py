"""Scraper dédié au réseau Sosh et ses offres."""

from __future__ import annotations

from core.models import Offer
from core.parsing import parse_price_to_int
from core.scraper import BaseOfferScraper


class SoshFibreScraper(BaseOfferScraper):
    name = "sosh"
    table_name = "sosh"

    def scrape(self) -> list[Offer]:
        session = self._session_factory()
        try:
            session.open(
                "https://shop.sosh.fr/box-internet"
                "?gclid=Cj0KCQiAlKmeBhCkARIsAHy7WVuo0gBV81VxJQFCWt6RnnvZFYirlztT_QRLPDE8sQXfiTI6hDddV_gaAuTGEALw_wcB"
                "&gclsrc=aw.ds#FIBRE"
            )
            prix_promo = session.text(
                '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[2]'
            )
            debit = session.text('//*[@id="pills-fibre"]/div[2]/div/div[2]/div/div/div')
            prix = session.text(
                '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[4]/span[2]'
            )
            return [
                Offer(
                    offre="Fibre sosh",
                    prix=parse_price_to_int(prix),
                    prix_promo=parse_price_to_int(prix_promo),
                    debit=debit.split(".")[0],
                )
            ]
        finally:
            session.close()
