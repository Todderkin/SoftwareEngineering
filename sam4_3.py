import datetime as dt
import time as tm
from time import sleep

for i in range(5):
    print(dt.datetime.now().strftime("%H:%M:%S"))
    sleep(1)