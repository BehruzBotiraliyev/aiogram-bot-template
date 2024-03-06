from aiogram import types
from loader import dp
from aiogram.dispatcher import filters


@dp.message_handler(is_reply=True, commands=['user_id'])
async def show_users(message: types.Message):
    await message.answer(message.reply_to_message.from_user.id)


@dp.message_handler(content_types='contact', is_sender_contact=True)
async def show_contacts(message: types.Message):
    await message.answer('Rahmat !')


@dp.message_handler(is_forwarded=True)
async def show_forwarded(message: types.Message):
    await message.answer('Ko\'chirilgan')
