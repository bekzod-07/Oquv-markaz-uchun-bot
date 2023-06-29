from loader import dp
from aiogram import types

@dp.message_handler(text="📞 Aloqa")
async def aloqa(message: types.Message):
    await message.answer("Biz bilan bog'lanish: \n\n📞 Tel.: +998(99) 123 45 67\n\n📧 E-mail: bekzodsindorov0@gmail.com\n\nYou tube: http://youtube.com/sindorov_bekhzod\n\nIjtimoiy tarmoqlar:\n\nTelegram: t.me/foydali_2024\n\nInstagram: instagram.com/_sindorov")