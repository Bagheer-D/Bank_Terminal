import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "string, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726759", "7158 30** **** 6759"),
        ("3456127834871", None),
        ("", None),
    ],
)
def test_get_mask_card_number(string: str, expected: str) -> None:
    assert get_mask_card_number(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [("73654108430135874305", "**4305"), ("00000111112222266666", "**6666"), ("40702810530000000", None), ("", None)],
)
def test_get_mask_account(string: str, expected: str) -> None:
    assert get_mask_account(string) == expected
