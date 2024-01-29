import os

from ujson import loads
import aiofiles

async def get_json3(filename: str) -> list:
    path = f"oge15/{filename}"
    if os.path.exists(path):
        async with aiofiles.open(path, "r", encoding="utf-8") as file:
            return loads(await file.read())
    return []