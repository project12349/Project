from aiogram.fsm.state import StatesGroup, State

class Admin(StatesGroup):
    Предмет = State()
    Задание = State()
    Ответ = State()
    Класс = State()

class Update_Admin(StatesGroup):
    Предмет = State()
    Задание = State()
    Ответ = State()
    Класс = State() 