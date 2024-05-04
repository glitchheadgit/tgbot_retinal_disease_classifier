from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class Pagination(CallbackData, prefix="pag"):
    stage: int


def paginator():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="1", callback_data=Pagination(stage=1).pack()
        ),
        InlineKeyboardButton(
            text="2", callback_data=Pagination(stage=2).pack()
        ),
        InlineKeyboardButton(
            text="3", callback_data=Pagination(stage=3).pack()
        ),
        InlineKeyboardButton(
            text="4", callback_data=Pagination(stage=4).pack()
        ),
        InlineKeyboardButton(
            text="5", callback_data=Pagination(stage=5).pack()
        ),
        width=5,
    )
    builder.row(
        InlineKeyboardButton(
            text="Random", callback_data=Pagination(stage=0).pack()
        ),
        width=1,
    )
    return builder.as_markup()
