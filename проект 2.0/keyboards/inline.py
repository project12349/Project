from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📚 Предметы", callback_data = "predmets")
        ],
        [
            InlineKeyboardButton(text="📋 Ежедневное задание", callback_data="everyday_quest"),
            InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
        ]
    ])

main_9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📚 Предметы", callback_data = "predmets"),
            InlineKeyboardButton(text = "🎈 Подготовка к ОГЭ", callback_data = "oge")
        ],
        [
            InlineKeyboardButton(text="📋 Ежедневное задание", callback_data="everyday_quest"),
            InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
        ]
    ])

klass = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📙 7 класс", callback_data = "7"),
            InlineKeyboardButton(text = "📚 8 класс", callback_data = "8")
        ],
        [
            InlineKeyboardButton(text = "🏫 9 класс", callback_data = "9")
        ]
    ])

clas = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📙 7 класс", callback_data = "seven"),
            InlineKeyboardButton(text = "📚 8 класс", callback_data = "eight")
        ],
        [
            InlineKeyboardButton(text = "🏫 9 класс", callback_data = "nine")
        ]
    ])

predmet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "🟰 Алгебра", callback_data="algebra"),
            InlineKeyboardButton(text = "📐 Геометрия", callback_data="geometry")
        ]
    ])
zadanie = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Ответить", callback_data="otvet"),
            InlineKeyboardButton(text="🔙 Меню", callback_data="back")
        ]
    ])
oge = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ОГЭ 1-5",callback_data="oge3"),
            InlineKeyboardButton(text="ОГЭ 6-19",callback_data="oge1")
        ],
        [
            InlineKeyboardButton(text="ОГЭ 20-25",callback_data="oge2")
        ]
    ]
)
back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back")
        ]
    ]
)