import datetime
import time


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

mybirthday = datetime.datetime(2023,2,26,0)
datetime.timedelta
for i in range(12):
    today  = datetime.datetime.now()
    time.sleep(1)
    diff = mybirthday-today
    print (strfdelta(diff, "my birthday is in {days} days and {hours}:{minutes}:{seconds}"))