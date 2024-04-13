from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import *

router = Router()


@router.callback_query()
async def proc_call(callback: CallbackQuery):
    callback_data = callback.data
    if callback_data == 'chl':
        await callback.message.edit_text(
        f"Choose the language of translation",
        reply_markup=inline.langs
    )
