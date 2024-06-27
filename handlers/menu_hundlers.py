from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from lexicon import LEXICON_RU, PRICE
from keyboards import (
    top_menu,
    user_menu,
    time_menu,
    create_tz_menu,
    back_to_user_menu_kb,
    update_balance_kb,
    tariffs_menu,
)
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from envparse import Env

env = Env()
env.read_envfile()


router: Router = Router()


# @router.message()
# async def test_redis(message: Message, state: FSMContext) -> None:
#     data = {"test1": "test1", "test2": "test2"}
#     await state.set_data(data=data)
#     await state.set_state(FeedbacksState.fb_not_answer)
#     await state.set_data(data={"ret": "ter"})
#     print(await state.get_data())
#     await message.answer(data["test1"])


# was been deleted
@router.message(StateFilter(default_state))
async def proccess_view_main_menu(message: Message) -> None:
    await message.answer(LEXICON_RU["main_menu"], reply_markup=top_menu)


@router.callback_query(F.data == "main_menu")
async def proccess_view_callback_main_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=top_menu)
    await callback.answer()


@router.callback_query(F.data == "user_office")
async def proccess_view_user_office_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=user_menu)
    await callback.answer()


@router.callback_query(F.data == "set_times_send")
async def proccess_view_time_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=time_menu)
    await callback.answer()


@router.callback_query(F.data == "back_to_user_menu")
async def proccess_back_to_user_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_reply_markup(reply_markup=user_menu)
    await callback.answer()


@router.callback_query(F.data == "time_day_hight")
async def proccess_create_timezone_menu(callback: CallbackQuery) -> None:
    kb = await create_tz_menu(3)
    await callback.message.answer(LEXICON_RU["time_menu"], reply_markup=kb.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("utc"))
async def proccess_check_timezone(callback: CallbackQuery) -> None:
    val_tz = int(callback.data.split(" ")[-1])
    await callback.message.edit_reply_markup(reply_markup=back_to_user_menu_kb)
    await callback.answer()


@router.callback_query(F.data == "balance")
async def proccess_view_user_balance(callback: CallbackQuery) -> None:
    # get user balance from DB
    await callback.message.answer(
        f"Вам доступно {40} ответов на отзывы", reply_markup=update_balance_kb
    )
    await callback.answer()


@router.callback_query(F.data == "update_balance")
async def proccess_update_balance(callback: CallbackQuery) -> None:
    # get user balance from DB
    await callback.message.answer(LEXICON_RU["tariffs_menu"], reply_markup=tariffs_menu)
    await callback.answer()


@router.callback_query(F.data.startswith("pay"))
async def proccess_payment_feedbacks(callback: CallbackQuery) -> None:
    await callback.message.answer_invoice(
        title="test Title",
        description="test description",
        provider_token=env("PAYMENT_TOKEN"),
        currency="RUB",
        payload="100",
        prices=[PRICE.get(callback.data.split(" ")[-1])],
    )
    await callback.answer()
