from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from core.utils.config import ADMIN_ID


MODER = ADMIN_ID[1]
ADMIN = ADMIN_ID[0]

user_commands = [
    BotCommand(command="start", description="старт ботіка"),
]

moderator_commands = user_commands + [
    BotCommand(command="/schedule_api", description="запустити атомне"),
    BotCommand(command="/stop_api", description="стопанути атомне"),
    BotCommand(command="/check_jobs", description="перевірити атомне"),
]


admin_commands = moderator_commands


async def set_commands(bot: Bot):
    await bot.set_my_commands(user_commands, BotCommandScopeDefault())
    await bot.set_my_commands(
        moderator_commands, scope=BotCommandScopeChat(chat_id=MODER)
    )
    await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=ADMIN))
