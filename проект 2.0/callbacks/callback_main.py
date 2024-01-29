
from aiogram import Router, F
from aiogram.types import CallbackQuery

from utils.databases import UsersDataBase
from keyboards import inline, fabrics
from seven_class.subloader7 import get_json7
from eight_class.subloader8 import get_json8
from oge1.subloader import get_json1
from oge2.subloader import get_json2
from oge15.subloader import get_json3
from nine_class.subloader9 import get_json9

router = Router()
db = UsersDataBase()

@router.callback_query(F.data == "7")
async def seven_class(call: CallbackQuery):
    await db.create_table()
    user_id = call.from_user.id
    name = call.from_user.first_name
    await db.add_user(int(user_id), name, int(7))
    user = await db.get_user(int(user_id))
    await call.message.edit_text(
    f'<b>👤 Имя:</b> <i><a href="tg://user?id={user_id}">{name}</a></i>\n<b>🏫 Класс:</b> <i>{user[2]}</i>\n<b>🥇 Пройденные задания:</b> <i>{user[3]}</i>\n<b>🥲 Непройденные задания:</b> <i>{user[4]}</i>\n', reply_markup = inline.main
    )

@router.callback_query(F.data == "8")
async def eight_class(call: CallbackQuery):
    await db.create_table()
    user_id = call.from_user.id
    name = call.from_user.first_name
    await db.add_user(int(user_id), name, int(8))
    user = await db.get_user(int(user_id))
    await call.message.edit_text(
    f'<b>👤 Имя:</b> <i><a href="tg://user?id={user_id}">{name}</a></i>\n<b>🏫 Класс:</b> <i>{user[2]}</i>\n<b>🥇 Пройденные задания:</b> <i>{user[3]}</i>\n<b>🥲 Непройденные задания:</b> <i>{user[4]}</i>\n', reply_markup = inline.main
    )

@router.callback_query(F.data == "9")
async def nine_class(call: CallbackQuery):
    await db.create_table()
    user_id = call.from_user.id
    name = call.from_user.first_name
    await db.add_user(int(user_id), name, int(9))
    user = await db.get_user(int(user_id))
    await call.message.edit_text(
    f'<b>👤 Имя:</b> <i><a href="tg://user?id={user_id}">{name}</a></i>\n<b>🏫 Класс:</b> <i>{user[2]}</i>\n<b>🥇 Пройденные задания:</b> <i>{user[3]}</i>\n<b>🥲 Непройденные задания:</b> <i>{user[4]}</i>\n', reply_markup = inline.main_9
    )

@router.callback_query(F.data == "predmets")
async def predmets(call: CallbackQuery):
    await db.create_table()
    await call.message.edit_text("<b>Выбери предмет, по которому ищешь тему⬇️</b>", reply_markup=inline.predmet)

@router.callback_query(F.data == "everyday_quest")
async def predmets(call: CallbackQuery):
    await db.create_table()
    user = await db.get_user(call.from_user.id)
    if user[2] == 7:
        quest = await db.get_quest(int(7))
    elif user[2] == 8:
        quest = await db.get_quest(int(8))
    elif user[2] == 9:
        quest = await db.get_quest(int(9))
    await call.message.edit_text(f"<b>Задание по предмету {quest[1]}:</b>\n\n<i>{quest[3]}</i>\n\n<i>Чтобы написать ответ, напиши команду: /answer [ответ]</i>")

@router.callback_query(F.data == "algebra")
async def predmets(call: CallbackQuery):
    await db.create_table()
    user = await db.get_user(call.from_user.id)
    if user[2] == 7:
        algebra = await get_json7("algebra7.json")
    elif user[2] == 8:
        algebra = await get_json8("algebra8.json")
    elif user[2] == 9:
        algebra = await get_json9("algebra9.json")
    await call.message.edit_text(f"<b>{algebra[0][0]}</b>", reply_markup = fabrics.paginator2())

@router.callback_query(F.data == "geometry")
async def predmets(call: CallbackQuery):
    await db.create_table()
    user = await db.get_user(call.from_user.id)
    if user[2] == 7:
        geometry = await get_json7("geometry7.json")
    elif user[2] == 8:
        geometry = await get_json8("geometry8.json")
    elif user[2] == 9:
        geometry = await get_json9("geometry9.json")
    await call.message.edit_text(f"<b>{geometry[0][0]}</b>", reply_markup = fabrics.paginator())

@router.callback_query(F.data=="oge")
async def oge(call: CallbackQuery):
    await call.message.edit_text("<b>Выбери какие части заданий хотите разобрать</b>", reply_markup=inline.oge)

@router.callback_query(F.data=="oge1")
async def oge1(call: CallbackQuery):
    geometry = await get_json1("oge1.json")
    await call.message.edit_text(f"<b>{geometry[0][0]}</b>", reply_markup = fabrics.paginator3())

@router.callback_query(F.data=="oge2")
async def oge1(call: CallbackQuery):
    geometry = await get_json2("oge.json")
    await call.message.edit_text(f"<b>{geometry[0][0]}</b>", reply_markup = fabrics.paginator4())

@router.callback_query(F.data=="oge3")
async def oge1(call: CallbackQuery):
    geometry = await get_json3("oge.json")
    await call.message.edit_text(f"<b>{geometry[0][0]}</b>", reply_markup = fabrics.paginator5())