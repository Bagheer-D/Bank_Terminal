import re
import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("1234", None),
        ("", None),
    ],
)
def test_mask_account_card(string, expected):
    assert mask_account_card(string) == expected


@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"


def test_get_date(date):
    assert get_date(date) == "11.07.2018"
