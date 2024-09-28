from aiogram.types import (CallbackQuery)
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from shop_bot.keyboards.inline.admin_kb import (create_admin_start_kb,
                                                  create_crud_select_kb)
from shop_bot.states import FSMAdminPanel

router = Router()


@router.callback_query(StateFilter(FSMAdminPanel.choose_action), F.data == 'manage_menu')
async def process_manage_button(callback: CallbackQuery,
                                state: FSMContext,
                                session: AsyncSession) -> None:
    await callback.message.delete()
    data = await SphereRepository(session=session).select_all()
    await callback.message.answer(text='Hi',
                                  reply_markup=create_crud_select_kb(data=data))



@router.callback_query(StateFilter(FSMAdminPanel), F.data == 'exit')
async def process_exit_button(callback: CallbackQuery,
                              state: FSMContext) -> None:
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(f'Админ-панель закрыта')
