"""parser les valeurs les chaines de caracteres."""


def parse_price_to_int(value: str) -> int:
    """Extract the firsst numeric token and return it as int (e.g., "29,99 €" -> 2999)."""
    if value is None:
        raise ValueError("price value is required")
    digits = "".join(ch for ch in value if ch.isdigit())
    if not digits:
        raise ValueError(f"price value is not numeric: {value!r}")
    return int(digits)
