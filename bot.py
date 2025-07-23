from database.db import init_db
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers import start

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)

if __name__ == '__main__':
    print("🤖 ProBot запущен")
    executor.start_polling(dp, skip_updates=True)
