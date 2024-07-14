import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str | None:
    """Принимаем информацию о карте/счете, возвращаем маску"""
    digits = "".join(re.findall("\\d+", card_info))
    if "Счет " in card_info:
        return f"{'Счет '}{get_mask_account(digits)}"
    else:
        pay_system = re.sub(r"[0-9]", "", card_info)
        return f"{pay_system}{get_mask_card_number(digits)}"


def get_date(date_input: str) -> str | None:
    """Преобразуем формат даты"""
    if len(date_input) == 26:
        date = date_input.split("T")[0]
        date_correct = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
        return date_correct
    else:
        return None
