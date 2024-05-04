from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply, inline, fabrics


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Greetings, {message.from_user.first_name}!', reply_markup=reply.main)


@router.message(F.text.in_(['/links', 'Links']))
async def links(message: Message):
    await message.answer('Links:', reply_markup=inline.links)


@router.message(F.text.in_(['/gallery', 'Gallery']))
async def gallery(message: Message):
    await message.answer('Gallery:', reply_markup=fabrics.paginator())