from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import inlinekeyboards

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=inlinekeyboards.inline_keyboard)
