import threading
import schedule
from tools import webscrap as ws
from bot import telegrambot as tel

# def job():
#     print("I'm running on thread %s" % threading.current_thread())


def web_scrap():
    url = "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule"
    web_scrap = ws.WebScrap(url)
    try:
        data = web_scrap.get_soup('span', 'fw-500')
        web_scrap.json_export(data)
    except:
        pass


def telegram():
    tel.executor.start(tel.dp, tel.send_message())
    tel.executor.start_polling(tel.dp, skip_updates=True)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def main_thread():
    schedule.every()
    schedule.every()

# schedule.every(2).seconds.do(run_threaded, job)
# schedule.every().day.at("04:30").do(run_threaded, web_scrap)


schedule.every().day.at("15:23").do(run_threaded, web_scrap)

while 1:

    # schedule.every()
    t = threading.Thread(target=main_thread)
    t.start()

    # time.sleep(1)
    # print("hello")
