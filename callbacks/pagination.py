from contextlib import suppress
from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from keyboards import fabrics


router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    smiles = []
    pn = int(callback_data.page)
    if callback_data.action == "next":
        page = pn + 1 if pn < len(smiles) - 1 else pn
    else:
        page = pn - 1 if pn > 0 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{smiles[page][0]} {smiles[page][1]}", reply_markup=fabrics.paginator(page)
        )
    await call.answer()
