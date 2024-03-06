from aiogram import types
from loader import dp


@dp.callback_query_handler(text=["In_First_button", "In_Second_button"])
async def check_button(call: types.CallbackQuery):
    if call.data == "In_First_button":
        await call.message.answer('https://darslik-api.sport.uz/media/icons/teakvando.png')
    if call.data == "In_Second_button":
        await call.message.reply("Hi! This is the second inline keyboard button.")
    await call.answer()

