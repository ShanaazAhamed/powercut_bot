from os import getenv
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
import sqlite3

load_dotenv()

API_TOKEN = getenv("TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def store_in_db(id, grp):
    conn = await sqlite3.connect('users.db')
    print("Successfully Connected")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = """
    This handler will be called when user sends `/start` or `/help` command
    `/group` to To enter the group
    """
    await message.reply(text)


@dp.message_handler(commands=['group'])
async def ask_group(message: types.message):
    await message.reply(f"Please enter the Group")


@dp.message_handler(regexp='^[A-Z]$')
async def echo(message: types.Message):
    print("sds")
    await message.reply(message.text)
    conn = sqlite3.connect('users.db')
    print("Successfully Connected")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.chat.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
