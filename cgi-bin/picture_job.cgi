#!/usr/bin/env python

import schedule
import os, sys
import datetime
import time
from opimage_things import cameras

'''Really simple job image capture script

Runs a job every X minutes from start of the script.

Goes until the script is killed

'''

work_folder = sys.argv[1]
interval = int(sys.argv[2])

def job():
    base = datetime.datetime.now().isoformat()
    fname_jpg = os.path.join(work_folder, base + '.jpeg')
    fname_raw = os.path.join(work_folder, base + '.data')
    cameras.take_picture(fname_raw, fmt='rgb', width=1280, height=720)
    cameras.take_picture(fname_jpg)



schedule.every(interval).minutes.do(job)
while True:
    schedule.run_pending()
