import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7001928591:AAFlpoHiF_JVehv6A6cxYp8BrUVHSDXMudw")
# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
dp.start_polling(bot, mylist=[1, 2, 3])

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /test1
@dp.message(Command("addtolist"))
async def cmd_addtolist(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")

# Хэндлер на команду /test2
@dp.message(Command("showlist"))
async def cmd_showlist(message: types.Message, mylist: list[int]):
    await message.answer(f"Мой лист {mylist}")

@dp.message(Command("info"))
async def cmd_dice(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



