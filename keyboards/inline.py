from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Notebook of model creation",
                url="https://github.com/EkaterinShitik/Blindness_detection/tree/main",
            )
        ],
        [
            InlineKeyboardButton(
                text="Telegram bot code",
                url="https://github.com/glitchheadgit/tgbot_ird_prediction",
            )
        ],
    ]
)
