from datetime import datetime
import random

start_date = input("please enter tow data (in this format: YYYY-MM-DD)\n")
end_date = input()
start_date = start_date.split("-")
end_date = end_date.split("-")
start_date = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))-datetime(1970, 1, 1)
end_date = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2])) - datetime(1970, 1, 1)
random_epoch = random.randint(start_date.total_seconds(), end_date.total_seconds())
print(datetime.fromtimestamp(random_epoch).strftime('%Y-%m-%d'))
if random_epoch.weekday() == 2:
    print("there is no vinagrit")
