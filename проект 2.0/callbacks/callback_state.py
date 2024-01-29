from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboards.inline import clas, main
from utils.databases import UsersDataBase

router = Router()
db = UsersDataBase()

@router.callback_query(F.data == "settings")
async def state_start(call: Message, state: FSMContext):
    await db.create_table()
    await state.set_state(Form.Класс)
    await call.message.answer("<b>Выберете класс</b>", reply_markup=clas)

@router.callback_query(F.data == "seven")
async def klass(call: Message, state: FSMContext):
    await db.create_table()
    await state.update_data(Класс="7")
    data = await state.get_data()
    await db.update_class(int(call.from_user.id), int(data['Класс']))
    await call.message.edit_text("<b>Изменение класса прошла успешно!</b>")
    await state.clear()

@router.callback_query(F.data == "eight")
async def klass(call: Message, state: FSMContext):
    await db.create_table()
    await state.update_data(Класс="8")
    data = await state.get_data()
    await db.update_class(int(call.from_user.id), int(data['Класс']))
    await call.message.edit_text("<b>Изменение класса прошла успешно!</b>")
    await state.clear()

@router.callback_query(F.data == "nine")
async def klass(call: Message, state: FSMContext):
    await db.create_table()
    await state.update_data(Класс="9")
    data = await state.get_data()
    await db.update_class(int(call.from_user.id), int(data['Класс']))
    await call.message.edit_text("<b>Изменение класса прошла успешно!</b>")
    await state.clear()

