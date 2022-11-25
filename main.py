import schedule
from tools import webscrap as ws
from bot import telegrambot as tel
from controller.json_controller import get_interrupt_times
import threading
import multiprocessing
from datetime import datetime

available_times = []


def web_scrap():
    url = "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule"
    web_scrap = ws.WebScrap(url)
    try:
        data = web_scrap.get_soup('span', 'fw-500')
        web_scrap.json_export(data)
    except:
        pass


def get_interrupt():
    global available_times
    available_times = get_interrupt_times()


def send_message(chat_id):
    pass


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def web_scrap_process():
    global available_times
    schedule.every().day.at("04:30").do(run_threaded, web_scrap)
    schedule.every().day.at("05:00").do(run_threaded, get_interrupt)

    while 1:
        schedule.run_pending()
        if len(available_times) != 0:
            for i in available_times:
                now = datetime.today().strftime("%H:%M%p")
                hour = int(now.split(":")[0])
                if hour < 10:
                    now = now[0:]
                if i == now:
                    """
                    TODO: get the list of groups id by their id & grp
                    TODO : iterate through the list & implement send message for each of them 
                    TODO: <optional> Maintain thread pool for above
                    """
                    print(i)


def telegram_process():
    tel.executor.start_polling(tel.dp, skip_updates=True)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=web_scrap_process)
    p2 = multiprocessing.Process(target=telegram_process)
    p1.start()
    p2.start()
