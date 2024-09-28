from aiogram import types, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, any_state

from shop_bot.keyboards import create_user_default_kb
from shop_bot.filters import IsAdminFilter
from shop_bot.states import FSMAdminPanel


router = Router()


@router.message(Command('start'), StateFilter(any_state))
async def start_handler(message: types.Message,
                        state: FSMContext) -> None:
    await state.clear()
    if message.from_user is None:
        return
    await message.answer(f"Привет, {'user_name'}\n"
                         f"Добро пожаловать в магазин всего!",
                         reply_markup=create_user_default_kb())
    await state.set_state()


@router.message(Command('help'), StateFilter(any_state))
async def help_handler(message: types.Message) -> None:
    if message.from_user is None:
        return
    await message.answer(f'Сейчас я тебе помогу:)\n'
                         f'Есть команды /start, /cancel\n'
                         f'/start - начать снова\n'
                         f'/cancel - сбросить все действия ')


@router.message(Command('cancel'), ~StateFilter(default_state))
async def help_handler(message: types.Message, state: FSMContext) -> None:
    if message.from_user is None:
        return
    await state.clear()
    await message.answer(f'Вы сбросили все действия:)')


@router.message(Command('admin'), IsAdminFilter())
async def admin_panel_command(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(f"Выбери нужное действие")
                         #reply_markup=create_admin_start_kb())
    await state.set_state(FSMAdminPanel.choose_action)


#@router.message()
#async def warn_unknow_command(message: types.Message, state: FSMContext) -> None:
#    await message.answer(f"Такой команды не существует:)\n"
#                         f"Жми /help если запутался")
