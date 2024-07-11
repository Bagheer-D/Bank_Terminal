import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "string, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158 3007 3472 6759", None),
        ("3456127834871", None),
        ("", None),
    ],
)
def test_get_mask_card_number(string, expected):
    assert get_mask_card_number(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [("73654108430135874305", "**4305"), ("0000 01111122222 66666", None), ("40702810530000000", None), ("", None)],
)
def test_get_mask_account(string, expected):
    assert get_mask_account(string) == expected
