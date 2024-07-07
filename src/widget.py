import re
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """Принимаем информацию о карте/счете, возвращаем маску"""
    digits = "".join(re.findall('\\d+', card_info))
    if "Счет " in card_info:
        return f"{'Счет'} {get_mask_account(digits)}"
    else:
        pay_system = re.sub(r'[0-9]', '', card_info)
        return f"{pay_system} {get_mask_card_number(digits)}"


def get_date(date_input: str) -> str:
    """Преобразуем формат даты"""
    date = date_input.split("T")[0]
    date_correct = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return date_correct


print(mask_account_card(str(input("Введите номер карты/счета: "))))
print(get_date(str(input("Введите дату: "))))