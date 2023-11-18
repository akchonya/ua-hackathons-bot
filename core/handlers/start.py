from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋🏻 привіт всім! це ботік для каналу @ua_hackathons\n\n"
        "наразі він взагалі нічого не вміє робити так шо всєм *стікєр майнкрафт пока*",
        reply_markup=ReplyKeyboardRemove(),
    )
