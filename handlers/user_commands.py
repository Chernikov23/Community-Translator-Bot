from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards import *
from utils.dataWork import *

router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    chat_id = str(msg.chat.id)
    user_data_local = load_user_data()
    if chat_id not in user_data_local:
        user_data_local[chat_id] = {
            "usLang": "en"
        }
        save_user_data(user_data_local)
    await msg.answer(
        f'Hi! I am Community translator bot. Everyone can help in developing by the link https://github.com/Chernikov23/Community-Translator-Bot!\nChoose language of bot',
        reply_markup=inline.chlang
    )