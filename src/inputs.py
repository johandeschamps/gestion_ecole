import datetime


def date(text: str) -> datetime.date:
    val = input(text)
    val = val.replace(" ", "-").replace("/", "-")
    return datetime.date.fromisoformat(val)
