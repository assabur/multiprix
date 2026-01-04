from core.parsing import parse_price_to_int



def test_parse_price_to_int_handles_comma() -> None:
    assert parse_price_to_int("29,99 €") == 2999


def test_parse_price_to_int_handles_spaces() -> None:
    assert parse_price_to_int("  45,00   ") == 4500

