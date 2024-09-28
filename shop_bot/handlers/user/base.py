from aiogram.types import (CallbackQuery)
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from shop_bot.keyboards.inline.admin_kb import (create_crud_select_kb)
from shop_bot.states.user_state import FSMShop
from shop_bot.repository.item import ItemRepository


router = Router()


@router.callback_query(StateFilter(), F.data == 'shop')
async def process_shop_button(callback: CallbackQuery,
                                state: FSMContext,
                                session: AsyncSession) -> None:
    data = await ItemRepository(session=session).select_all()
    await callback.message.answer(text='Выбери вид товара',
                                  reply_markup=create_crud_select_kb(data=data))
    await state.set_state()


@router.callback_query(StateFilter(), F.data == 'account')
async def process_account_button(callback: CallbackQuery,
                                 state: FSMContext,
                                 session: AsyncSession) -> None:
    #data = await UserRepository(session=session).select_user_data()
    await callback.message.answer(text='Твои данные:')


@router.callback_query(StateFilter(), F.data == 'balance')
async def process_account_button(callback: CallbackQuery,
                                 state: FSMContext,
                                 session: AsyncSession) -> None:
    #data = await UserRepository(session=session).select_user_data()
    await callback.message.answer(text='Твой баланс',)
                                  #reply_markup=create_balance_kb())


@router.callback_query(StateFilter(), F.data == 'support')
async def process_account_button(callback: CallbackQuery,
                                 state: FSMContext,
                                 session: AsyncSession) -> None:
    await callback.message.answer(text='Напиши сообщение в поддержку:')