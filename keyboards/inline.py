from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧Choose the lang🇷🇺", callback_data="chl"),
            InlineKeyboardButton(text="⚙️Settings🔧", callback_data="set")
        ]
    ]
)

chlang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Русский', callback_data='rus'),
            InlineKeyboardButton(text="English", callback_data="eng")
        ]
    ]
)

langs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='RU🇷🇺', callback_data='ru')
        ]
    ]
)

choosLanguage = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='RU🇷🇺', callback_data='trRu'),
            InlineKeyboardButton(text="EN🇬🇧", callback_data="trEn")
        ],
        [
            InlineKeyboardButton(text='IT🇮🇹', callback_data='trIt'),
            InlineKeyboardButton(text="CH🇨🇳", callback_data="trCh")
        ]
    ]
)