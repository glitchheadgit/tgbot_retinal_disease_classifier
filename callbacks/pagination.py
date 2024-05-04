from contextlib import suppress
from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from keyboards import fabrics
from utils.model import choose_image_by_stage


router = Router()


@router.callback_query(fabrics.Pagination.filter(F.stage.in_([0, 1, 2, 3, 4, 5])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    with suppress(TelegramBadRequest):
        path = choose_image_by_stage(callback_data.stage)
        image = types.FSInputFile(path)
        await call.message.answer_photo(
            image,
            caption='Choose a disease stage:',
            reply_markup=fabrics.paginator(),
        )
    await call.answer()
