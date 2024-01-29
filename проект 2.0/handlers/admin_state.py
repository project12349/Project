from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.admin_states import Admin, Update_Admin
from utils.databases import UsersDataBase

router = Router()
db = UsersDataBase()

@router.message(Command("add_quest"))
async def fill_profile(message: Message, state: FSMContext):
    if message.from_user.id == 6356609598:
        await db.create_table()
        await state.set_state(Admin.Предмет)
        await message.answer("<b>Предмет задания:</b>")
    else:
        await message.answer("<b>Вы не админ!</b>")

@router.message(Admin.Предмет)
async def for_name(message: Message, state: FSMContext):
    await state.update_data(Предмет=message.text)
    await state.set_state(Admin.Задание)
    await message.answer("<b>Ваше задание:</b>")

@router.message(Admin.Задание)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Задание=message.text)
    await state.set_state(Admin.Ответ)
    await message.answer("<b>Ответ к заданию:</b>")

@router.message(Admin.Ответ)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Ответ=message.text)
    await state.set_state(Admin.Класс)
    await message.answer("<b>Для какого класса:</b>")

@router.message(Admin.Класс)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Класс=message.text)
    data = await state.get_data()
    await db.add_quest(int(message.from_user.id),  str(data['Предмет']), int(data['Класс']),  str(data['Задание']), str(data['Ответ']))
    await message.answer("<b>Задание добавлено!</b>")
    await state.clear()

@router.message(Command("update_quest"))
async def quest(message: Message, state: FSMContext):
    if message.from_user.id == 6356609598:
        await db.create_table()
        await state.set_state(Update_Admin.Класс)
        await db.minus_zadan(int(0))
        await message.answer("<b>Класс, который хотите редактировать:</b>")

@router.message(Update_Admin.Класс)
async def for_name(message: Message, state: FSMContext):
    await state.update_data(Класс=message.text)
    await state.set_state(Update_Admin.Предмет)
    await message.answer("<b>Какой предмет:</b>")

@router.message(Update_Admin.Предмет)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Предмет=message.text)
    await state.set_state(Update_Admin.Задание)
    await message.answer("<b>Задание:</b>")

@router.message(Update_Admin.Задание)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Задание=message.text)
    await state.set_state(Update_Admin.Ответ)
    await message.answer("<b>Ответ к заданию:</b>")

@router.message(Update_Admin.Ответ)
async def Admin_name(message: Message, state: FSMContext):
    await state.update_data(Ответ=message.text)
    data = await state.get_data()
    await db.update_quest(int(data['Класс']), str(data['Предмет']),   str(data['Задание']), str(data['Ответ']))
    await message.answer("<b>Задание изменено!</b>")
    await state.clear()