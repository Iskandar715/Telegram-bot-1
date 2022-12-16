CATEGORIES = [
    "ЎЗБЕКИСТОН",
    "ЖАХОН",
    "ИКТИСОДИЁТ",
    "ЖАМИЯТ",
    "ФАН-ТЕХНИКА",
    "СПОРТ",
    "BUSINESS CLASS",
    "АУДИО"
]


def get_category(category_name):
    if category_name == 'ЎЗБЕКИСТОН':
        return 'uzbekiston'
    elif category_name == 'ЖАХОН':
        return 'the world'
    elif category_name == 'ИКТИСОДИЁТ':
        return 'economy'
    elif category_name == 'ЖАМИЯТ':
        return 'society'
    elif category_name == 'ФАН-ТЕХНИКА':
        return 'science technology'
    elif category_name == 'СПОРТ':
        return 'sport'
    elif category_name == 'BUSINESS CLASS':
        return 'business class'
    elif category_name == 'АУДИО':
        return 'audio'