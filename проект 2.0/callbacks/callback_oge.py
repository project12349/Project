from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import BufferedInputFile

from keyboards import fabrics, inline
from oge1.subloader import get_json1
from oge15.subloader import get_json3
from oge2.subloader import get_json2
from utils.databases import UsersDataBase

router = Router()
db = UsersDataBase()

@router.callback_query(fabrics.Pagination3.filter(F.action.in_(["prev3", "next3"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination3):
    geometry = await get_json1("oge1.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next3":
        page = page_num + 1 if page_num < (len(geometry) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>{geometry[page][0]}</b>",
        reply_markup=fabrics.paginator3(page)
        )
        
@router.callback_query(fabrics.Pagination3.filter(F.action.in_(["ok3"])))
async def pagination_ok(call: CallbackQuery, callback_data: fabrics.Pagination3):
    page_num = int(callback_data.page)
    geometry = await get_json1("oge1.json")
    if callback_data.action == "ok3":
        page = page_num
        
    with suppress(TelegramBadRequest):
        file_ids = []
        await call.message.edit_text(
        f"<b>Файл к теме:</b> <i>{geometry[page][0]}</i>",
        reply_markup = inline.back)
        with open(f"oge1/{geometry[page][1]}", "rb") as image_from_buffer:
            result = await call.message.answer_document(
            BufferedInputFile(
                image_from_buffer.read(),
                filename=f"{geometry[page][1]}"
            ),
        )
    await call.answer()

@router.callback_query(fabrics.Pagination4.filter(F.action.in_(["prev4", "next4"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination4):
    geometry = await get_json2("oge.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next4":
        page = page_num + 1 if page_num < (len(geometry) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>{geometry[page][0]}</b>",
        reply_markup=fabrics.paginator4(page)
        )
        
@router.callback_query(fabrics.Pagination4.filter(F.action.in_(["ok4"])))
async def pagination_ok(call: CallbackQuery, callback_data: fabrics.Pagination4):
    page_num = int(callback_data.page)
    geometry = await get_json2("oge.json")
    if callback_data.action == "ok4":
        page = page_num
        
    with suppress(TelegramBadRequest):
        file_ids = []
        await call.message.edit_text(
        f"<b>Файл к теме:</b> <i>{geometry[page][0]}</i>",
        reply_markup = inline.back)
        with open(f"oge2/{geometry[page][1]}", "rb") as image_from_buffer:
            result = await call.message.answer_document(
            BufferedInputFile(
                image_from_buffer.read(),
                filename=f"{geometry[page][1]}"
            ),
        )
    await call.answer()

@router.callback_query(fabrics.Pagination5.filter(F.action.in_(["prev5", "next5"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination5):
    geometry = await get_json3("oge.json")
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next5":
        page = page_num + 1 if page_num < (len(geometry) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
        f"<b>{geometry[page][0]}</b>",
        reply_markup=fabrics.paginator5(page)
        )
        
@router.callback_query(fabrics.Pagination5.filter(F.action.in_(["ok5"])))
async def pagination_ok(call: CallbackQuery, callback_data: fabrics.Pagination4):
    page_num = int(callback_data.page)
    geometry = await get_json3("oge.json")
    if callback_data.action == "ok5":
        page = page_num
        
    with suppress(TelegramBadRequest):
        file_ids = []
        await call.message.edit_text(
        f"<b>Файл к теме:</b> <i>{geometry[page][0]}</i>",
        reply_markup = inline.back)
        with open(f"oge15/{geometry[page][1]}", "rb") as image_from_buffer:
            result = await call.message.answer_document(
            BufferedInputFile(
                image_from_buffer.read(),
                filename=f"{geometry[page][1]}"
            ),
        )
    await call.answer()