from aiogram import types
from loader import dp


@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def change_photo(message: types.Message):
    await message.answer('Rasm almashtiramizmi?')

