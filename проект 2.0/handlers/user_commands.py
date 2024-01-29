import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject

from keyboards import inline
from utils.databases import UsersDataBase

db = UsersDataBase()

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await db.create_table()
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = await db.get_user(user_id)
    if await db.get_user(user_id) is None:
        await message.answer(
        f"<b>Здравствуйте. Это бот-справочник по материалу 7-9 класса по математике. Выберите класс, по которому вам нужна информация ⬇️</b>", 
        reply_markup=inline.klass
        )
    else:
        if user[2] == int(9):
            main=inline.main_9
        else:
            main=inline.main
        await message.answer(
        f'<b>👤 Имя:</b> <i><a href="tg://user?id={user_id}">{name}</a></i>\n<b>🏫 Класс:</b> <i>{user[2]}</i>\n<b>🥇 Пройденные задания:</b> <i>{user[3]}</i>\n<b>🥲 Непройденные задания:</b> <i>{user[4]}</i>\n',
        reply_markup = main
        )

@router.message(Command("answer"))
async def answer(message: Message, command: CommandObject):
    user =await db.get_user(message.from_user.id)
    if user[2] == 7:
        quest = await db.get_quest(int(7))
    elif user[2] == 8:
        quest = await db.get_quest(int(8))
    elif user[2] == 9:
        quest = await db.get_quest(int(9))
    a = [str(n) for n in command.args.split()]
    if user[5] == 0:
        if str(quest[4]) == str(a[0]):
            await db.plus_zadanie(message.from_user.id, int(1))
            await db.minus_zadani(message.from_user.id, int(1))
            await message.answer("<b>Правильно</b>")
        else:
            await db.minus_zadanie(message.from_user.id, int(1))
            await db.minus_zadani(message.from_user.id, int(1))
            await message.answer("<b>Не правильно</b>")
    else:
        await message.answer("<b>Вы решали это задание.</b>")