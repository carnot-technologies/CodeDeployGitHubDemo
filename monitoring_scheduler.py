from apscheduler.schedulers.blocking import BlockingScheduler
import traceback
import datetime
import sys

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', second='0,15,30,45')
def update_metrics_cron():
    print("Updating server metrics: 60 second bucket")
    ft = datetime.datetime.utcnow()
    print(ft)


@scheduler.scheduled_job('cron', second='*/1')
def check_server_status():
    print("Checking server status ...")
    print("============ Server is up & running! ============")


if __name__ == '__main__':
    procs = []
    try:
        print("Starting the blocking monitoring scheduler")
        scheduler.start()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n', file=sys.stderr)
    except Exception:
        traceback.print_exc(file=sys.stdout)

    sys.exit(0)
