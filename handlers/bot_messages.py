from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import *

router = Router()

async def chosLang(msg: Message, call: CallbackQuery):
    calld = call.data
    
    await call.message.edit_text(
        f"Choose the language of translation",
        reply_markup=inline.langs
    )