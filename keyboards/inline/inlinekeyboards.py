from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardButton('button1', callback_data='In_First_button')
button2 = InlineKeyboardButton('button2', callback_data='In_Second_button')
button3 = InlineKeyboardButton('button3', callback_data='In_Third_button')
button4 = InlineKeyboardButton('button4', callback_data='In_Fourth_button')
button5 = InlineKeyboardButton('button5', callback_data='In_Fifth_button')
button6 = InlineKeyboardButton('button6', callback_data='In_Sixth_button')
button7 = InlineKeyboardButton('button7', callback_data='In_Seventh_button')
button8 = InlineKeyboardButton('button8', callback_data='In_Eighth_button')

inline_keyboard = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8)



