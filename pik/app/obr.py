from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router
from app.cnop import *

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет, выбери направление", reply_markup=start_keyboard)

@router.message(F.text == 'Geeks')
async def geeks_start(message: Message):
    await message.reply("INFO GEEKS", reply_markup=geeks_keyboard)

@router.message(F.text == "Направление")
async def dir(message: Message):
    await message.reply("Наши основные направления:", reply_markup=direction_keyboard)

@router.callback_query(F.data == "front")
async def inline_frontend(callback: CallbackQuery):
    await callback.answer('Вы выбрали направление Frontend')
    await callback.message.edit_text("Frontend", reply_markup=front_keyboard)

@router.callback_query(F.data == "back")
async def inline_backend(callback: CallbackQuery):
    await callback.answer('Вы выбрали направление Backend')
    await callback.message.edit_text("Backend", reply_markup=back_keyboard)

@router.callback_query(F.data == "Android")
async def inline_android(callback: CallbackQuery):
    await callback.answer('Вы выбрали направление Android')
    await callback.message.edit_text("Android", reply_markup=android_keyboard)

@router.callback_query(F.data == "UX/UI")
async def inline_ux_ui(callback: CallbackQuery):
    await callback.answer('Вы выбрали направление UX/UI')
    await callback.message.edit_text("UX/UI", reply_markup=dizi_keyboard)
