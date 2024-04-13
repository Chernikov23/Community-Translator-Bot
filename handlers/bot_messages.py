from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from keyboards import *
from gpytranslate import SyncTranslator, Translator
from config_reader import config
import base64
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile
import os
import json
from threading import Lock
from utils.dataWork import *


router = Router()
t = SyncTranslator()
bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
dt = Translator()

@router.callback_query()
async def proc_call(callback: CallbackQuery):
    callback_data = callback.data
    chat_id = str(callback.message.chat.id)
    
    user_data_local = load_user_data()
    
    if callback_data == 'rus':
        user_data_local[chat_id]["usLang"] = 'ru'
        save_user_data(user_data_local)
        await callback.message.edit_text(
            "Язык сменён на Русский",
            reply_markup=inline.main
        )
        
    
    
    if callback_data == 'chl':
        await callback.message.edit_text(
        f"Choose the language of translation",
        reply_markup=inline.langs
    )



@router.message()
async def procTrans(msg: Message):
    user_text = msg.text
    ln = await dt.detect(user_text)
    if ln == 'en':
        translation = t.translate(text=user_text, targetlang='ru')
        translated_text = translation.text
        await msg.answer(f"Word {user_text} in Russian: {translated_text}")
    elif ln == 'ru':
        translation = t.translate(text=user_text, targetlang='en')
        translated_text = translation.text
        await msg.answer(f"Word {user_text} in English: {translated_text}")
    with NamedTemporaryFile(delete=False, suffix='.ogg') as temp_file:
        t.tts(translated_text, file=temp_file)
        temp_file_path = temp_file.name


    audio_file = FSInputFile(temp_file_path, filename='voice.ogg')
    await bot.send_voice(chat_id=msg.chat.id, voice=audio_file)


    os.unlink(temp_file_path)
    
    