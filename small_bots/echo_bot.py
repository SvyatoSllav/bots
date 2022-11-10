import asyncio

from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import Command, CommandObject

from pydantic import ValidationError
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


@dp.message()
async def echo_answer(message: types.Message):
    try:
        logger.info(f"Пришло сообщение {message.text}")
        await message.reply(message.html_text)
    except ValidationError:
        logger.error(
            "Пришло сообщение не валидного типа (не текст и не смайлик)."
        )
        await message.answer("Nice try")


async def main():
    bot = Bot(token=config.tg_bot.bot_token, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
