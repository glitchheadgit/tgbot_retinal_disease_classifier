from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Prediction')],
        [KeyboardButton(text='Gallery')],
        [KeyboardButton(text='Links')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Choose one of the following options:',
    selective=True
)


cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Cancel request')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)