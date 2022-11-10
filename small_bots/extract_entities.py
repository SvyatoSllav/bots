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
async def exctract_data(message: types.Message):
    data = {
        "url": "None",
        "email": "None",
        "code": "None"
    }
    entities = message.entities or []
    for entity in entities:
        if entity.type in data.keys():
            data[entity.type] = entity.extract_from(message.text)
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Пароль: {html.quote(data['code'])}"
    )


async def main():
    bot = Bot(token=config.tg_bot.bot_token, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
