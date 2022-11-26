from os import getenv
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
from bot.handlers.db_handler import get_group_from_db, get_all_id, store_in_db, update_db
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot.handlers.json_handler import json_handler

load_dotenv()

API_TOKEN = getenv("TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    group = State()
    edit_group = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Conversation entrypoint"""
    greenings = "Thank you for subscribing PowerCut Bot🙌😎\n"
    prefix = greenings + \
        "/help    : Get Help\n"+"/group  : Add your Group \n"+"/edit   : Edit your group📝\n" + \
        "/find : Find my group\n"+"/time : To get your Power Cut time"
    await message.reply(f"Hello, {message.chat.username}\n{prefix}")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    text = "This Bot sends the Power outage time in your area before an hour\nYou can add and edit the power cut group\n/group  : Add your Group \n/edit   : Edit your group📝\n/find : Find my group\n/time : To get your Power Cut time"
    await message.reply(text)


@dp.message_handler(commands=['time'])
async def send_welcome(message: types.Message):
    json = json_handler()
    chat_id = message.chat.id
    res = get_group_from_db(chat_id)
    if (res != -1 and len(res) > 0):
        grp = res[-1]
        time = json.get_time(grp)
        if (time != -1):
            await message.reply(f"Power outage in your area at {time}")
        else:
            await message.reply(f"Error occurs, couldn't get your time")
    elif (res == -1):
        await message.reply(f"An internal error occurs, Try again shortly")
    else:
        await message.reply(f"Your group is not stored\n If you want to add your group, try /group")


# @dp.message_handler(state='*', commands=['cancel'])
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """Allow user to cancel action via /cancel command"""

#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Cancelled.')


@dp.message_handler(commands=['group'])
async def ask_group(message: types.message):
    await Form.group.set()
    await message.reply(f"Please enter the Group")


@dp.message_handler(state=Form.group, regexp='^[A-Z]$')
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = message.chat.id
    grp = message.text.strip().upper()
    res = store_in_db(chat_id, grp)
    if (res == True):
        await message.reply(f"Your group is set as '{grp}' successfully")
    elif (res == -1):
        await message.reply(f"Your group is not set, Try again shortly")
    else:
        await message.reply(f"Your group already exists\n If you want to edit group try /edit")


@dp.message_handler(state=Form.group)
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("We couldn't recognize your input \n Enter your group like this\n Ex: A")


@dp.message_handler(commands=['edit'])
async def ask_group(message: types.message):
    chat_id = message.chat.id
    await Form.edit_group.set()
    res = get_group_from_db(chat_id)
    if (res != -1 and len(res) > 0):
        old_group = f"Your previous group is, {res[-1]}"
        await message.reply(f"{old_group} \nPlease enter the new Group")
    elif (res == -1):
        await message.reply(f"An internal error occurs, Try again shortly")
    else:
        await message.reply(f"Your group is not stored\n If you want to add your group, try /group")


@dp.message_handler(state=Form.edit_group, regexp='^[A-Z]$')
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = message.chat.id
    grp = message.text.strip().upper()
    res = update_db(chat_id, grp)
    if (res == True):
        await message.reply(f"Your group is updated as '{grp}' successfully")
    elif (res == -1):
        await message.reply(f"Your group is not updated, Please try again shortly")
    else:
        await message.reply(f"Your group is not stored\n If you want to add your group, try /group")


@dp.message_handler(state=Form.edit_group)
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("We couldn't recognize your input \n Enter your group like this\n Ex: A")


@dp.message_handler(commands=['find'])
async def ask_group(message: types.message):
    chat_id = message.chat.id
    res = get_group_from_db(chat_id)
    if (res != -1 and len(res) > 0):
        await message.reply(f"Your group is, {res[-1]}")
    elif (res == -1):
        await message.reply(f"An internal error occurs, Try again shortly")
    else:
        await message.reply(f"Your group does not  exists, Please add group by /group")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.chat.id)
    # get_group_from_db(message.chat.id)
    # print(store_in_db(23232323223, "A"))
    # print(update_db(message.chat.id, "W"))
    # print(get_all_id('W'))
    # await send_message()


async def send_message(chat_id):
    await bot.send_message(chat_id, "message")


if __name__ == '__main__':
    executor.start(dp, send_message())
    executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, send_message("Hi"), skip_updates=True)
    # asyncio.run(send_message("hi"))
