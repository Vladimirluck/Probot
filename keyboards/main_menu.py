from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🔍 Покупатель"),
        KeyboardButton("📤 Продавец"),
        KeyboardButton("📸 Агент")
    )
    return kb
