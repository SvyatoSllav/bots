import asyncio

from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import Command, CommandObject
from aiogram.utils.markdown import hide_link

from loguru import logger

from config import load_config


config = load_config()


dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message, command: CommandObject):
    logger.info("Пришла комманда start")
    if command.args:
        name = html.bold(html.quote(command.args))
        return await message.reply(f"Hello {name}")
    await message.reply(f"Hello {message.chat.username}")


@dp.message(Command(commands=["dice"]))
async def cmd_dice(message: types.Message, bot: Bot):
    logger.info("Пришла комманда dice")
    await bot.send_dice(message.chat.id, emoji="🎲")


@dp.message(Command(commands=["hidden_link"]))
async def hidden_link(message: types.Message, bot: Bot):
    logger.info("Пришла комманда hidden_link")
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Some text\n"
        f"Another text\n"
    )


async def main():
    bot = Bot(token=config.tg_bot.bot_token, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
