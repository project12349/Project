from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards import fabrics, inline
from seven_class.subloader7 import get_json7
from nine_class.subloader9 import get_json9
from eight_class.subloader8 import get_json8
from utils.databases import UsersDataBase

router = Router()
db = UsersDataBase()

@router.callback_query(fabrics.Pagination2.filter(F.action.in_(["prev2", "next2"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination2):
    await db.create_table()
    user = await db.get_user(call.from_user.id)
    if user[2] == 7:
        algebra = await get_json7("algebra7.json")
    elif user[2] == 8:
        algebra = await get_json8("algebra8.json")
    elif user[2] == 9:
        algebra = await get_json9("algebra9.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next2":
        page = page_num + 1 if page_num < (len(algebra) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>{algebra[page][0]}</b>",
        reply_markup=fabrics.paginator2(page)
        )
        
@router.callback_query(fabrics.Pagination2.filter(F.action.in_(["ok2"])))
async def pagination_ok(call: CallbackQuery, callback_data: fabrics.Pagination2):
    user = await db.get_user(call.from_user.id)
    page_num = int(callback_data.page)
    if user[2] == 7:
        algebra = await get_json7("algebra7.json")
    elif user[2] == 8:
        algebra = await get_json8("algebra8.json")
    elif user[2] == 9:
        algebra = await get_json9("algebra9.json")
    if callback_data.action == "ok2":
        page = page_num
        
    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>Ссылка(и) к теме:</b> <i>{algebra[page][0]}</i>",
        reply_markup = fabrics.url(algebra[page]))
        print(int(page))
    await call.answer()

@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    await db.create_table()
    user = await db.get_user(call.from_user.id)
    if user[2] == 7:
        geometry = await get_json7("geometry7.json")
    elif user[2] == 8:
        geometry = await get_json8("geometry8.json")
    elif user[2] == 9:
        geometry = await get_json9("geometry9.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(geometry) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>{geometry[page][0]}</b>",
        reply_markup=fabrics.paginator(page)
        )

@router.callback_query(fabrics.Pagination.filter(F.action.in_(["ok"])))
async def pagination_ok(call: CallbackQuery, callback_data: fabrics.Pagination):
    user = await db.get_user(call.from_user.id)
    page_num = int(callback_data.page)
    if user[2] == 7:
        geometry = await get_json7("geometry7.json")
    elif user[2] == 8:
        geometry = await get_json8("geometry8.json")
    elif user[2] == 9:
        geometry = await get_json9("geometry9.json")
    if callback_data.action == "ok":
        page = page_num
        
    with suppress(TelegramBadRequest):
        await call.message.edit_text(
       f"<b>Ссылка(и) к теме:</b> <i>{geometry[page][0]}</i>",
        reply_markup = fabrics.url(geometry[page]))
        print(int(page))
    await call.answer()

@router.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    await db.create_table()
    user_id = call.from_user.id
    name = call.from_user.first_name
    user = await db.get_user(user_id)
    if user[2] == int(9):
        main=inline.main_9
    else:
        main=inline.main
    await call.message.edit_text(
        f'<b>👤 Имя:</b> <i><a href="tg://user?id={user_id}">{name}</a></i>\n<b>🏫 Класс:</b> <i>{user[2]}</i>\n<b>🥇 Пройденные задания:</b> <i>{user[3]}</i>\n<b>🥲 Непройденные задания:</b> <i>{user[4]}</i>\n',
        reply_markup = main
        )
    await call.answer()