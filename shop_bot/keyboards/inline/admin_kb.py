from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup)
from aiogram.filters.callback_data import CallbackData


class DataCallbackFactory(CallbackData, prefix='id'):
    entity_id: int


def create_admin_start_kb() -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    buttons.append(InlineKeyboardButton(text='Cтатистика', callback_data='stats'))
    buttons.append(InlineKeyboardButton(text='Управление', callback_data='manage_menu'))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=2)
    kb_builder.row(InlineKeyboardButton(text='Выйти', callback_data='exit'))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup(resize_keyboard=True)


def create_crud_menu_kb(entity_type: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    buttons.append(InlineKeyboardButton(text='Изм.название', callback_data='update_name'))
    buttons.append(InlineKeyboardButton(text='Удалить', callback_data='delete'))
    if entity_type == 'sphere':
        buttons.append(InlineKeyboardButton(text='Ред.профессии', callback_data='edit_profession'))
    elif entity_type == 'profession':
        buttons.append(InlineKeyboardButton(text='Ред.ссылку', callback_data='update_url'))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=3)
    kb_builder.row(InlineKeyboardButton(text='В начало',
                                        callback_data='back')
                   )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_crud_professions_kb() -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    buttons.append(InlineKeyboardButton(text='Редактировать', callback_data='update'))
    buttons.append(InlineKeyboardButton(text='Удалить', callback_data='delete'))
    buttons.append(InlineKeyboardButton(text='Создать', callback_data='create'))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=2)
    kb_builder.row(InlineKeyboardButton(text='В начало',
                                        callback_data='back')
                   )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_crud_select_kb(data: list) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    for row in data:
        buttons.append(InlineKeyboardButton(
            text=row.name,
            callback_data=DataCallbackFactory(entity_id=int(row.id)).pack())
        )
    kb_builder.row(*buttons, width=2)
    kb_builder.row(InlineKeyboardButton(text='В начало',
                                        callback_data='back'),
                   InlineKeyboardButton(text='Создать',
                                        callback_data='create'))
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def crud_create_profession_kb():
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    buttons.append(InlineKeyboardButton(text='Создать профессию', callback_data='create'))
    buttons.append(InlineKeyboardButton(text='В начало', callback_data='back'))
    kb_builder.row(*buttons, width=1)

    return kb_builder.as_markup()


def create_yes_no_buttons():
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    kb_builder.row(InlineKeyboardButton(text='Да', callback_data='yes'),
                   InlineKeyboardButton(text='Нет', callback_data='no'))
    kb_builder.row(*buttons, width=2)

    return kb_builder.as_markup()
