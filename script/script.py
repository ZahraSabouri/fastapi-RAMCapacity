import psutil as _psutil
import schedule as _schedule
import datetime as _dt
import time as _time
import requests as _requests


url = 'http://127.0.0.1:8000/ram_capacity/'

def job():
    new_record = {"date": str(_dt.datetime.utcnow()),
                  "total": str(_psutil.virtual_memory().total),
                  "free": str(_psutil.virtual_memory().free),
                  "used": str(_psutil.virtual_memory().used)}
    x = _requests.post(url, json=new_record)
    print(x.text)
    print(new_record)

_schedule.every(1).seconds.do(job)

while True:
    # Checks whether a scheduled task is pending to run or not
    _schedule.run_pending()
    _time.sleep(1)
