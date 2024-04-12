from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards import *
router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(
        f'Hi, {msg.from_user.full_name}! I am Community translator bot. Everyone can help in developing by the link https://github.com/Chernikov23/Community-Translator-Bot! ',
        reply_markup=inline.main
    )