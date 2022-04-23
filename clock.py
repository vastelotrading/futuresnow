import strategy
import threading
from apscheduler.schedulers.blocking import BlockingScheduler

def con():
    t1 = threading.Thread(target=strategy.run())
    t1.start()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59/15', max_instances=15, misfire_grace_time=3600) #set time for your trade, this default set the ot to run every 15minutes
def timed_job():
    con()

sched.start()
