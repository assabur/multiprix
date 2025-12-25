"""Définit la strurtrue de la donnée à recuper."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Offer:
    """Represents a scraped offer in a normalized shape."""

    offre: str
    prix: int
    prix_promo: int
    debit: str

    def to_dict(self) -> dict:
        return {
            "offre": self.offre,
            "prix": self.prix,
            "prix_promo": self.prix_promo,
            "debit": self.debit,
        }
