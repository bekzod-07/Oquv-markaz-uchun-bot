from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu_btn import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Salom, {message.from_user.full_name}!</b> Sizga qanday yordam bera olishim mumkin?", reply_markup=menu)