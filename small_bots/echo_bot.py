import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from pydantic import ValidationError
from loguru import logger

from config import load_config


config = load_config()


dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    logger.info("Пришла комманда start")
    await message.reply("Hello")


@dp.message(Command(commands=["dice"]))
async def cmd_dice(message: types.Message, bot: Bot):
    logger.info("Пришла комманда dice")
    await bot.send_dice(message.chat.id, emoji="🎲")


@dp.message()
async def echo_answer(message: types.Message):
    try:
        logger.info(f"Пришло сообщение {message.text}")
        await message.reply(message.text)
    except ValidationError:
        logger.error("Пришло сообщение не валидного типа (не текст и не смайлик).")
        await message.answer("Nice try")


async def main():
    bot = Bot(token=config.tg_bot.bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
