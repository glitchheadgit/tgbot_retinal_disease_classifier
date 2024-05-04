from aiogram import Router, F, Bot, types
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply, inline, fabrics


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"🌟 Greetings, {message.from_user.first_name}!", reply_markup=reply.main
    )


@router.message(F.text.in_(["/links", "Links"]))
async def links(message: Message):
    await message.answer("📖 Links", reply_markup=inline.links)


@router.message(F.text.in_(["/gallery", "Gallery"]))
async def gallery(message: Message, bot: Bot):
    text = "Choose a disease stage:\n"
    diagnosis = {0: "No DR", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Proliferative"}
    for k, v in diagnosis.items():
        text += f"{k+1} - {v}\n"
    await message.answer(text=text, reply_markup=fabrics.paginator())
