from aiogram.dispatcher.filters.state import StatesGroup, State

class kursgaYozilish(StatesGroup):
    fullName = State()
    yosh = State()
    kurs = State()
    bilim = State()
    nomer = State()
    check = State()