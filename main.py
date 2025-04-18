import datetime as dt
import os
import time

from scheduler import Scheduler

from config import env
from wa import send_message


def scheduled_task():
    text = "Good morning"

    if os.path.exists("message.txt"):
        with open("message.txt", "r") as f:
            text = f.read()

    send_message(env.RECEPIENT_NUMBER, text)


def main():
    timezone = dt.timezone(dt.timedelta(hours=6))

    schedule = Scheduler(tzinfo=timezone)

    schedule.daily(dt.time(hour=5, minute=0, tzinfo=timezone), scheduled_task)

    print("Starting scheduler")
    print(schedule)

    while True:
        try:
            schedule.exec_jobs()
            time.sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
