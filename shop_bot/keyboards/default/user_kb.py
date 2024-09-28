from aiogram.utils.keyboard import KeyboardBuilder
from aiogram.types import (KeyboardButton,
                           ReplyKeyboardMarkup)


def create_user_default_kb() -> ReplyKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = KeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[KeyboardButton] = []
    buttons.append(KeyboardButton(text='Магазин', data='shop'))
    buttons.append(KeyboardButton(text='Баланс', data='balance'))
    buttons.append(KeyboardButton(text='Аккаунт', data='shop'))
    buttons.append(KeyboardButton(text='Поддержка', data='support'))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=2)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()