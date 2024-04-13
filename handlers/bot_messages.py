from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import *

router = Router()


@router.callback_query()
async def proc_call(call: CallbackQuery):
    calb = call.data
    if calb == 'chl':
        await call.message.edit_text(
        f"Choose the language of translation",
        reply_markup=inline.langs
    )
