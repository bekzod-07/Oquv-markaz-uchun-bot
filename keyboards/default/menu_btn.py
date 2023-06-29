from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("ℹ Biz haqimizda"),
        ],
        [
            KeyboardButton("🎓 Kurslar"),
            KeyboardButton("📞 Aloqa"),
        ],
        [
            KeyboardButton("📍 Manzil"),
        ],
        [
            KeyboardButton("®️ Kursga yozilish"),
        ],
    ], resize_keyboard=True
)