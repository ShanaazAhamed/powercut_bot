import schedule
from tools import webscrap as ws
from bot import telegrambot as tel
import threading
import multiprocessing


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
    schedule.every().day.at("22:48").do(run_threaded, web_scrap)
    while 1:
        schedule.run_pending()


def telegram_process():
    tel.executor.start_polling(tel.dp, skip_updates=True)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=web_scrap_process)
    p2 = multiprocessing.Process(target=telegram_process)
    p1.start()
    p2.start()
