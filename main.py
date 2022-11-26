import schedule
from tools import webscrap as ws
from bot import telegrambot as tel
from controller.json_controller import get_interrupt_times, get_groups_by_time
from bot.handlers.db_handler import get_list_of_id
import threading
import multiprocessing
from datetime import datetime


# available_times = []
# def get_interrupt():
#     global available_times
#     available_times = get_interrupt_times()


def web_scrap():
    url = "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule"
    web_scrap = ws.WebScrap(url)
    try:
        data = web_scrap.get_soup('span', 'fw-500')
        web_scrap.json_export(data)
    except:
        pass


def send_message(chat_id):
    print('message send to', chat_id)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def web_scrap_process():
    available_times = []

    def get_interrupt():
        global available_times
        available_times = get_interrupt_times()
        print(available_times, "********************")

    schedule.every().day.at("04:30").do(run_threaded, web_scrap)
    schedule.every().day.at("11:19").do(run_threaded, get_interrupt)

    while 1:
        schedule.run_pending()
        print(available_times)
        if len(available_times) != 0:
            for i in available_times:
                now = datetime.today().strftime("%H:%M%p")
                hour = int(now.split(":")[0])
                if hour < 10:
                    now = now[0:]
                if i == now:
                    print("RUNNING")
                    """
                    TODO: get the list of groups id by time
                        1. get the groups by time <list>
                        2.get_list_of_id
                    TODO : iterate through the list & implement send message for each of them 
                    TODO: <optional> Maintain thread pool for above
                    """
                    groups = get_groups_by_time(i)
                    chat_ids = get_list_of_id(groups)
                    for i in chat_ids:
                        send_message(i)


def telegram_process():
    tel.executor.start_polling(tel.dp, skip_updates=True)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=web_scrap_process)
    p2 = multiprocessing.Process(target=telegram_process)
    p1.start()
    p2.start()
