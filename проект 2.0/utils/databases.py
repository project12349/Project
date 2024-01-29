import aiosqlite

# Определяем класс "UsersDataBase" для работы с базой данных пользователей.
class UsersDataBase:
    def __init__(self):
        self.name = 'data/users.db'  # Указываем путь к базе данных.

    # Метод "create_table" создает таблицу "users" и "everyday_quest" в базе данных, если она не существует.
    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                number_class INTEGER,
                victory_zadanie INTEGER,
                falls_zadanie INTEGER,
                zadanie INTEGER
            );
            CREATE TABLE IF NOT EXISTS everyday_quest (
                admin_id INTEGER PRIMARY KEY,
                predmet TEXT,
                clas INTEGER,
                quest TEXT,
                otvet TEXT
            );
            '''
            await cursor.executescript(query)
            await db.commit()

    # Метод "get_user" получает данные пользователя из базы данных по его ID.       
    async def get_user(self, user_id):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user_id,))
            return await cursor.fetchone()


    # Метод "add_user" добавляет пользователя в базу данных, если его там нет.
    async def add_user(self, user_id, name, number):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user_id):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, name, number_class, victory_zadanie, falls_zadanie, zadanie) VALUES (?, ?, ?, ?, ?, ?)'
                await cursor.execute(query, (user_id, f'{name}', int(number), 0, 0, 0))
                await db.commit()

    # Метод "get_quest" проверяет есть ли задание по классам. 
    async def get_quest(self, clas):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM everyday_quest WHERE clas = ?'
            await cursor.execute(query, (clas,))
            return await cursor.fetchone()

    # Метод "add_quest" добавляет задания для класса.
    async def add_quest(self, user_id, predmet, clas, text, text2):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_quest(clas):
                cursor = await db.cursor()
                query = 'INSERT INTO everyday_quest (admin_id, predmet, clas, quest, otvet) VALUES (?, ?, ?, ?, ?)'
                await cursor.execute(query, (user_id, f'{predmet}', int(clas), f'{text}', f'{text2}'))
                await db.commit()

    async def update_quest(self, clas, predmet, text, text2):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE everyday_quest SET predmet = ?, quest = ?, otvet = ? WHERE clas = ?'
            await cursor.execute(query, (f'{predmet}', f'{text}', f'{text2}', clas))
            await db.commit()

    # Метод "update_class" обновляет класс ученика.
    async def update_class(self, user, number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET number_class = ? WHERE id = ?'
            await cursor.execute(query, (number, user))
            await db.commit()

    # Метод "plus_zadanie" обновляет выполненные задания.
    async def plus_zadanie(self, user, number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET victory_zadanie = victory_zadanie + ? WHERE id = ?'
            await cursor.execute(query, (number, user))
            await db.commit()

    # Метод "minus_zadanie" обновляет невыполненные задания.
    async def minus_zadanie(self, user, number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET falls_zadanie = falls_zadanie + ? WHERE id = ?'
            await cursor.execute(query, (number, user))
            await db.commit()

    async def minus_zadani(self, user, number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET zadanie = zadanie + ? WHERE id = ?'
            await cursor.execute(query, (number, user))
            await db.commit()

    async def minus_zadan(self, number):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET zadanie = ?'
            await cursor.execute(query, (number, ))
            await db.commit()