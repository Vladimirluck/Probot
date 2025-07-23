from aiogram import Dispatcher, types
from keyboards.main_menu import get_main_menu

async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Привет! Я — ProBot, помощник по недвижимости.\nКто вы?",
        reply_markup=get_main_menu()
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
