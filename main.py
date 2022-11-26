import schedule
from tools import webscrap as ws
from bot import telegrambot as tel
from controller.json_controller import get_interrupt_times, get_groups_by_time
from controller.time_controller import to_twenty_four, before_an_hour
from bot.handlers.db_handler import get_list_of_id
import threading
import multiprocessing
from datetime import datetime
import time

from aiogram import Bot
from dotenv import load_dotenv
from os import getenv
import logging


def send_message(chat_id):
    load_dotenv()
    API_TOKEN = getenv("TOKEN")
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    bot.send_message(chat_id, "Message")


available_times = []


def get_interrupt():
    global available_times
    interrupt_times = get_interrupt_times()
    available_times = interrupt_times
    # print(available_times)


def web_scrap():
    url = "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule"
    web_scrap = ws.WebScrap(url)
    try:
        data = web_scrap.get_soup('span', 'fw-500')
        web_scrap.json_export(data)
    except:
        pass


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def web_scrap_process():
    global available_times

    schedule.every().day.at("04:30").do(run_threaded, web_scrap)
    schedule.every().day.at("01:22").do(run_threaded, get_interrupt)

    while 1:
        schedule.run_pending()
        now = datetime.today().strftime("%H:%M")
        if len(available_times) != 0:
            for i in available_times:
                temp = before_an_hour(i)
                i_std = to_twenty_four(temp)
                if i_std == now:
                    groups = get_groups_by_time(i)
                    chat_ids = get_list_of_id(groups)
                    for i in chat_ids:
                        send_message(int(i))
                    time.sleep(60)


def telegram_process():
    tel.executor.start_polling(tel.dp, skip_updates=True)


if __name__ == "__main__":
    # tel.bot.send_message(705621896, "Hello")
    p1 = multiprocessing.Process(target=web_scrap_process)
    p2 = multiprocessing.Process(target=telegram_process)
    p1.start()
    p2.start()
