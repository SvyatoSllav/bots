import os
from pathlib import Path
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

parent_path = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(str(parent_path), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = Bot(token=os.environ.get("BOT_TOKEN"))

dp = Dispatcher(bot=bot)


@dp.message_handler()
async def get_messsage(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text=message.text)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
