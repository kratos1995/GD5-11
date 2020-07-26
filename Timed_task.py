
from ModuLe import Run_Algebra as run
import time
import os
from datetime import datetime
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

# def job1():
#
#     print('job1', datetime.datetime.now())
#     scheduler = BlockingScheduler()
#     # 每隔2分钟执行一次， /1：每隔1分钟执行一次
#     scheduler.add_job(job1, 'cron', minute="*/2", id='jo.b1')
#     scheduler.start()
#     Run_Algebra()
# job1()


def tick():
    run
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=30)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
        print(scheduler.get_jobs())
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown(wait=False)
        print('Exit The Job!')