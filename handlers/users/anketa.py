from aiogram import types

from keyboards.default.menu_btn import menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext

from keyboards.default.check import check_btn
from states.kursga_yozilish import kursgaYozilish

@dp.message_handler(text="®️ Kursga yozilish")
async def kursga_yozilish(message: types.message):
    await message.answer("Familiya Ism Sharif?\n\n(Masalan: Sindorov Bekzod Farhod o'g'li)")
    await kursgaYozilish.fullName.set()

@dp.message_handler(state=kursgaYozilish.fullName)
async def fullName(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"name": fullname})

    await message.answer("Yoshingiz?\n\n(Masalan : 17 yosh)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.yosh)
async def yosh(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"Yosh": yosh})

    await message.answer("Qaysi kursimiz bo'yicha tahsil olmoqchisiz?\n\n🎓 Kurslarimiz :\n\n❇️  KOMPYUTER SAVODXONLIGI\n\n❇️  WEB DASTURLASH  (FRONT END,  BECK END)\n\n❇️  ANDROID\n\n❇️  SMM\n\n❇️  GRAFIK DIZAYN\n\n❇️  TELEGRAM BOT\n\n❇️  PHOTOSHOP\n\n❇️  PYTHON\n\n❇️  Data Science va Sun'iy Intellekt")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.kurs)
async def kurs(message: types.message, state: FSMContext):
    kurs = message.text
    await state.update_data({"Kurs": kurs})

    await message.answer("Tanlagan yo'nalishingiz bo'yicha bilim darajangiz qanday?\n\n(Masalan : Umuman yo'q, Oz-moz bilaman, To'liq bilaman)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.bilim)
async def bilim(message: types.Message, state: FSMContext):
    bilim = message.text
    await state.update_data({"Bilim": bilim})

    await message.answer("Telefon raqamingizni kiriting?\n\n(Masalan : +99897 1234567)")
    await kursgaYozilish.next()

@dp.message_handler(state=kursgaYozilish.nomer)
async def nomer(message: types.Message, state: FSMContext):
    nomer = message.text
    await state.update_data({"Nomer": nomer})

    data = await state.get_data()
    fullname = data.get("name")
    yosh = data.get("Yosh")
    kurs = data.get("Kurs")
    bilim = data.get("Bilim")
    nomer = data.get("Nomer")

    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"🎓 Shogird: - {fullname}\n"
    msg += f"🌐 Yosh: - {yosh}\n"
    msg += f"🎓 Kurs: - {kurs}\n"
    msg += f"👨🏻‍💻 Daraja: - {bilim}\n"
    msg += f"📞 Aloqa: - {nomer}"
    await message.answer(msg)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=check_btn)
    await kursgaYozilish.next()


@dp.message_handler(state=kursgaYozilish.check)
async def chesk(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        fullname = data.get("name")
        yosh = data.get("Yosh")
        kurs = data.get("Kurs")
        bilim = data.get("Bilim")
        nomer = data.get("Nomer")

        msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
        msg += f"🎓 Shogird: - {fullname}\n"
        msg += f"🌐 Yosh: - {yosh}\n"
        msg += f"🎓 Kurs: - {kurs}\n"
        msg += f"👨🏻‍💻 Daraja: - {bilim}\n"
        msg += f"📞 Aloqa: - {nomer}"
        await message.answer(msg)
        await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=check_btn)
        await bot.send_message(chat_id=5816736795, text=msg)
        await message.answer("Barcha ma`lumotlar adminga yuborildi. Tez orada siz bilan bog`lanadi")
        await message.answer("Bosh menyu!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Qabul qilinmadi", reply_markup=menu)
        await state.finish()