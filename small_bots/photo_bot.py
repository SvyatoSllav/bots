import asyncio

from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import Command, CommandObject

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
async def download_photo(message: types.Message, bot: Bot):
    logger.info(message.document)

    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    destination = "/home/slava/DEV/udemy_tg_bot/bots/small_bots/tg_bot_img.jpg"
    await bot.download_file(
        file_path=file_path,
        destination=destination
    )


async def main():
    bot = Bot(token=config.tg_bot.bot_token, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
