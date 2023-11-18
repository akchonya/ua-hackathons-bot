import datetime

from aiogram import Bot, Router, html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.utils.request_func import make_async_request
from core.filters.basic import isAdmin

router = Router()


async def job(bot: Bot):
    response = await make_async_request(
        "https://hackathons-scrapper.onrender.com/hackathons"
    )
    for ad in response:
        text = (
            f"{html.bold(ad['title'])}\n\n"
            + f"📝 {ad['description']}\n\n📅 дата: {ad['date']}\n\n"
            + f"{html.link('ℹ️ дізнатися більше', ad['link'])}{html.link('&#8204', ad['image_url'])}"
        )
        await bot.send_message(chat_id="@ua_hackathons", text=text)


@router.message(Command("schedule_api"), isAdmin())
async def schedule_api_handler(message: Message, bot: Bot, scheduler: AsyncIOScheduler):
    scheduler.add_job(
        job,
        "interval",
        name="api_parser",
        id="1",
        hours=5,
        start_date=datetime.datetime.now() + datetime.timedelta(0, 5),
        kwargs={"bot": bot},
    )  # Set the interval as needed
    scheduler.start()
    await message.answer(
        "Scheduler started. Use /stop_api to stop the scheduler.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("stop_api"), isAdmin())
async def stop_api_handler(message: Message, scheduler: AsyncIOScheduler):
    scheduler.remove_all_jobs()
    await message.answer("Scheduler stopped.", reply_markup=ReplyKeyboardRemove())


@router.message(Command("check_jobs"), isAdmin())
async def check_jobs_handler(message: Message, scheduler: AsyncIOScheduler):
    jobs = scheduler.get_jobs()
    if len(jobs):
        for job in jobs:
            await message.answer(
                f"Job '{job.name}' with ID {job.id} \n\nscheduled at: {job.next_run_time}"
            )
    else:
        await message.answer(
            "а ви ще не запускали работягу..", reply_markup=ReplyKeyboardRemove()
        )
