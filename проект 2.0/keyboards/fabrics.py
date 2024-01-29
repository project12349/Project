from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from seven_class.subloader7 import get_json7
from nine_class.subloader9 import get_json9
from eight_class.subloader8 import get_json8

class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=Pagination(action="next", page=page).pack()),
        InlineKeyboardButton(text="✅ Выбрать", callback_data=Pagination(action="ok", page=page).pack()),
        InlineKeyboardButton(text="🔙 Меню", callback_data = "back"),
        width=2
    )
    return builder.as_markup()

class Pagination2(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator2(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=Pagination2(action="prev2", page=page).pack()),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=Pagination2(action="next2", page=page).pack()),
        InlineKeyboardButton(text="✅ Выбрать", callback_data=Pagination2(action="ok2", page=page).pack()),
        InlineKeyboardButton(text="🔙 Меню", callback_data = "back"),
        width=2
    )
    return builder.as_markup()

def url(url):
    builder = InlineKeyboardBuilder()
    if (len(url) - 1) == 1:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    elif (len(url) - 1) == 2:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text="#2 Перейти", url=f"{url[2]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    elif (len(url) - 1) == 3:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text="#2 Перейти", url=f"{url[2]}"),
            InlineKeyboardButton(text="#3 Перейти", url=f"{url[3]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    elif (len(url) - 1) == 4:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text="#2 Перейти", url=f"{url[2]}"),
            InlineKeyboardButton(text="#3 Перейти", url=f"{url[3]}"),
            InlineKeyboardButton(text="#4 Перейти", url=f"{url[4]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    elif (len(url) - 1) == 5:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text="#2 Перейти", url=f"{url[2]}"),
            InlineKeyboardButton(text="#3 Перейти", url=f"{url[3]}"),
            InlineKeyboardButton(text="#4 Перейти", url=f"{url[4]}"),
            InlineKeyboardButton(text="#5 Перейти", url=f"{url[5]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    elif (len(url) - 1) == 6:
        builder.row(
            InlineKeyboardButton(text="#1 Перейти", url=f"{url[1]}"),
            InlineKeyboardButton(text="#2 Перейти", url=f"{url[2]}"),
            InlineKeyboardButton(text="#3 Перейти", url=f"{url[3]}"),
            InlineKeyboardButton(text="#4 Перейти", url=f"{url[4]}"),
            InlineKeyboardButton(text="#5 Перейти", url=f"{url[5]}"),
            InlineKeyboardButton(text="#6 Перейти", url=f"{url[6]}"),
            InlineKeyboardButton(text = "🔙 Меню", callback_data="back"),
            width=2
        )
    return builder.as_markup()

class Pagination3(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator3(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=Pagination3(action="prev3", page=page).pack()),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=Pagination3(action="next3", page=page).pack()),
        InlineKeyboardButton(text="✅ Выбрать", callback_data=Pagination3(action="ok3", page=page).pack()),
        InlineKeyboardButton(text="🔙 Меню", callback_data = "back"),
        width=2
    )
    return builder.as_markup()

class Pagination4(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator4(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=Pagination4(action="prev4", page=page).pack()),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=Pagination4(action="next4", page=page).pack()),
        InlineKeyboardButton(text="✅ Выбрать", callback_data=Pagination4(action="ok4", page=page).pack()),
        InlineKeyboardButton(text="🔙 Меню", callback_data = "back"),
        width=2
    )
    return builder.as_markup()

class Pagination5(CallbackData, prefix="pag"):
    action: str
    page: int

def paginator5(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ Назад", callback_data=Pagination5(action="prev5", page=page).pack()),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=Pagination5(action="next5", page=page).pack()),
        InlineKeyboardButton(text="✅ Выбрать", callback_data=Pagination5(action="ok5", page=page).pack()),
        InlineKeyboardButton(text="🔙 Меню", callback_data = "back"),
        width=2
    )
    return builder.as_markup()