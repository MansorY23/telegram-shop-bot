from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)


class EntityCallbackFactory(CallbackData, prefix='id'):
    entity_id: int


def create_start_button() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = list()
    buttons.append(InlineKeyboardButton(
        callback_data='start',
        text='Начать'
    ))
    kb_builder.row(*buttons, width=1)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Функция для формирования инлайн-клавиатуры на лету
def create_entity_kb(data: list) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    for entity in data:
        buttons.append(InlineKeyboardButton(
            text=entity.name,
            callback_data=EntityCallbackFactory(
                entity_id=entity.id).pack())
        )

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=1)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_professions_kb(data: list) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    for profession in data:
        buttons.append(InlineKeyboardButton(
            text=f'{profession.name}',
            callback_data=EntityCallbackFactory(
                entity_id=profession.id).pack())
        )
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=1)

    kb_builder.row(InlineKeyboardButton(
        text='Вернуться в начало',
        callback_data='back'
    ))
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_profession_url_kb(profession) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    buttons.append(InlineKeyboardButton(
        text=f'Рейтинг {profession.name} ➡️',
        url=profession.url)
    )
    kb_builder.row(*buttons, width=1)
    kb_builder.row(InlineKeyboardButton(
        text='Вернуться в начало',
        callback_data='back'
    ))
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
