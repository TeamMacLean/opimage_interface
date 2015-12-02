#!/usr/bin/env python

import schedule
import os, sys
import datetime
import time
from opimage_things import cameras
from gpiozero import LED

'''Really simple job image capture script

Runs a job every X minutes from start of the script.

Goes until the script is killed

'''

work_folder = sys.argv[1]
interval = int(sys.argv[2])

def job():
    irled = LED(17)
    irled.on()
    time.sleep(2)
    base = datetime.datetime.now().isoformat()
    fname_jpg = os.path.join(work_folder, base + '.jpeg')
    fname_raw = os.path.join(work_folder, base + '.data')
    cameras.take_picture(fname_raw, fmt='rgb')
    cameras.take_picture(fname_jpg, width=640, height=480)
    irled.off()


schedule.every(interval).minutes.do(job)
while True:
    schedule.run_pending()
