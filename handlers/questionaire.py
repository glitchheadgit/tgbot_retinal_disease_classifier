import torch

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from utils.states import Images
from utils.model import prediction_wrapper
from keyboards import reply


router = Router()
classifier = torch.load('data/7_resnet152_whole_model.pt', map_location=torch.device('cpu'))


@router.message(F.text.in_(['/predict', 'Предсказания']))
async def get_photo(message: Message, state: FSMContext):
    await state.set_state(Images.user_images)
    await message.answer("Upload an image to analyze", reply_markup=reply.cancel)


@router.message(Images.user_images, F.photo)
async def get_prediction(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    file = await message.bot.download(file_id)
    diagnosis, prob = prediction_wrapper(classifier, file)
    prob = str(prob).replace('.', ',')
    await message.reply(f'Diagnosis: <b>{diagnosis}</b>\nProbability: <b>{prob}</b>', reply_markup=reply.main)
    await state.clear()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('what are you interested in?', reply_markup=reply.main)


@router.message(Images.user_images, ~F.photo)
async def wrong_format_handler(message: Message, state: FSMContext):
    if message.text.lower() == 'cancel request':
        await state.clear()
        await message.answer('what are you interested in?', reply_markup=reply.main)
    else:
        await message.answer('Send <b>images</b>\!')