# -*- coding: utf-8 -*-
# from ModuLe import Run_Algebra as run
from requestGD511 import page_url as page
import time
import os
from datetime import datetime
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import Send_mail
from ModuLe import Run_Algebra





def tick():
    page(1)
    time.sleep(30)
    Run_Algebra.run_algebra()
    print('''
    ************************************************************************************
    ************************************************************************************
    ***********************************定时任务运行成功***********************************
    ************************************************************************************
    ************************************************************************************
    ''',
    "*****************************************    现在的时间是: %s" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=300)
    print('按 Ctrl+{0} 退出'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
        print(scheduler.get_jobs())
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    except (KeyboardInterrupt, SystemExit,BaseException) as e:
        scheduler.shutdown(wait=False)
        Send_mail.send_mail(subject="警报：‘Timed_Task’ 模块错误，请以 nohup 重新运行程序",
                            content_text=e+scheduler.get_jobs(),attachments=None)
        print('退出工作!')