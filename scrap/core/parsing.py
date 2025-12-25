"""parser les valeurs les chaines de caracteres."""


def parse_price_to_int(value: str) -> int:
    """Extract the firsst numeric token and return it as int (e.g., "29,99 €" -> 2999)."""
    if value is None:
        raise ValueError("price value is required")
    token = value.strip().split()[0]
    token = token.replace(",", "")
    token = token.replace("\xa0", "")
    token = token.replace("€", "")
    return int(token)
