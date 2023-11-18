from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from apscheduler.schedulers.asyncio import AsyncIOScheduler

router = Router()


async def job(bot: Bot):
    await bot.send_message(chat_id="@ua_hackathons", text="testing mw")


@router.message(Command("schedule_api"))
async def schedule_api_handler(message: Message, bot: Bot, scheduler: AsyncIOScheduler):
    scheduler.add_job(
        job, "interval", seconds=5, kwargs={"bot": bot}
    )  # Set the interval as needed
    scheduler.start()
    await message.answer(
        "Scheduler started. Use /stop_api to stop the scheduler.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("stop_api"))
async def stop_api_handler(message: Message, scheduler: AsyncIOScheduler):
    scheduler.remove_all_jobs()
    await message.answer("Scheduler stopped.", reply_markup=ReplyKeyboardRemove())
