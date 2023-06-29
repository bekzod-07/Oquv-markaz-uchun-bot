from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kurslar = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton("🖥 Kompyuter savodxonligi"),
        ],
        [
            KeyboardButton("🌐 Web dasturlash"),
            KeyboardButton("📲 Android"),
        ],
        [
            KeyboardButton("🌄 Grafik dizayner")
        ],
        [
            KeyboardButton("❇️ Telegram bot"),
            KeyboardButton("📈 SMM"),
        ],
        [
            KeyboardButton("🏞 Photoshop")
        ],
        [
            KeyboardButton("🏙 Sun`iy intellekt"),
            KeyboardButton("🐍 Python")
        ],
        [
            KeyboardButton("®️ Kursga yozilish")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish"),
        ]
    ], resize_keyboard=True
)