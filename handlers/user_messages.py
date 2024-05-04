from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def echo(message: Message):
    await message.reply(f"{message.from_user.first_name}, i don't understand you :(")
