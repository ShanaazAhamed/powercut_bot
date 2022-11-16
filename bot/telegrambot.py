from os import getenv
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

load_dotenv()

API_TOKEN = getenv("TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    name = State()
    group = State()


def store_in_db(id):
    conn = sqlite3.connect('users.db')
    print("Successfully Connected")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Conversation entrypoint"""
    await Form.name.set()
    await message.reply("Send me your name")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    text = """
    This handler will be called when user sends `/start` or `/help` command
    `/group` to To enter the group
    """
    await message.reply(text)


@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""

    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return

    # Cancel state and inform user about it
    await state.finish()
    await message.reply('Cancelled.')


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    """Process user name"""

    # Finish our conversation
    await state.finish()
    await message.reply(f"Hello, {message.text}")  # <-- Here we get the name


@dp.message_handler(commands=['group'])
async def ask_group(message: types.message):
    await Form.group.set()
    await message.reply(f"Please enter the Group")


@dp.message_handler(state=Form.group)
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    # <-- Here we get the name
    await message.reply(f"Your group is, {message.text}")


@dp.message_handler(regexp='^[A-Z]$')
async def echo(message: types.Message):
    await message.reply(message.text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.chat.id)


async def send_message(message):

    await bot.send_message(705621896, message)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(send_message("Hi"))
    # loop.close()
    asyncio.run(send_message("hi"))
    executor.start_polling(dp, skip_updates=True)
