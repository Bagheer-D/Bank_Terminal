from typing import Any

dict_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dict_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Принимаем список словарей и значение для ключа, возвращаем новый список словарей,
    где ключ содержит переданное в функцию значение."""
    return [d for d in dict_list if d.get("state") == state]


def sort_by_date(dict_list: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Принимаем на вход список словарей, и возвращаем новый список, где словари отсортированы по убыванию даты"""
    sorted_list = sorted(dict_list, key=lambda new_dict_list: new_dict_list["date"], reverse=reverse)
    return sorted_list
