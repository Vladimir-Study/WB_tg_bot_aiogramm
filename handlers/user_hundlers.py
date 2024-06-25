from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from keyboards.inline_keyboards import top_menu, start_kb
from lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def proccess_start_command(message: Message) -> None:
    await message.answer(LEXICON_RU["/start"], reply_markup=start_kb)
