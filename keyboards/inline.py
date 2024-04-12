from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧Choose the lang🇷🇺", callback_data="chl"),
            InlineKeyboardButton(text="⚙️Settings🔧", callback_data="set")
        ]
    ]
)