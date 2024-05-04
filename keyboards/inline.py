from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Google', url='https://google.com'),
            InlineKeyboardButton(text='Wiki', url='https://wikipedia.org')
        ]
    ]
)